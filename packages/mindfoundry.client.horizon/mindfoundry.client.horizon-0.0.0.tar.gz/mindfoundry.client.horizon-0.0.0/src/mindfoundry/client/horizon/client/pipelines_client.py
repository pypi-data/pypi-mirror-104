import io
import json
import time
from typing import List, Optional

import pandas as pd

from mindfoundry.client.horizon.generated import Client
from mindfoundry.client.horizon.generated.api.pipelines import (
    delete_pipeline_resource,
    get_feature_export_resource,
    get_feature_nodes_and_links_resource,
    get_pipeline_resource,
    post_on_demand_predict_resource,
    post_predict_resource,
    post_restart_pipeline_resource,
    post_run_pipeline_resource,
    put_all_pipeline_resource,
    put_pipeline_lock_resource,
    put_stage_creation_resource,
)
from mindfoundry.client.horizon.generated.models import (
    BlueprintType,
    BoolLocked,
    ExpertPredictForm,
    NodeAndLink,
    OnDemandPredictForm,
    Pipeline,
    PipelineSpecification,
    PredictResponse,
    RegressorType,
    StageSpecification,
    StageStatus,
)

from ..generated.types import File
from .utils import assert_success, return_value_or_raise_error


class PipelinesClient:
    def __init__(self, client: Client):
        self._client = client

    def get(self, pipeline_id: int) -> Pipeline:
        pipeline = get_pipeline_resource.sync_detailed(
            client=self._client,
            id_=pipeline_id,
        )
        return return_value_or_raise_error(pipeline)

    def delete(self, pipeline_id: int) -> None:
        response = delete_pipeline_resource.sync_detailed(
            client=self._client,
            id_=pipeline_id,
        )
        assert_success(response)

    def create_custom(self, dataset_id: int, name: str) -> Pipeline:
        pipeline = put_all_pipeline_resource.sync_detailed(
            client=self._client,
            json_body=PipelineSpecification(
                name=name,
                dataset_id=dataset_id,
                blueprint=BlueprintType.CUSTOM,
            ),
        )
        return return_value_or_raise_error(pipeline)

    def add_stage(self, pipeline_id: int, spec: StageSpecification) -> Pipeline:
        pipeline = put_stage_creation_resource.sync_detailed(
            client=self._client,
            id_=pipeline_id,
            json_body=spec,
        )
        return return_value_or_raise_error(pipeline)

    def run(self, pipeline_id: int, wait_for_completion: bool = False) -> None:
        post_run_pipeline_resource.sync_detailed(client=self._client, id_=pipeline_id)
        if wait_for_completion:
            self._wait_for_completion(pipeline_id)

    def restart(self, pipeline_id: int, wait_for_completion: bool = False) -> None:
        post_restart_pipeline_resource.sync_detailed(client=self._client, id_=pipeline_id)
        if wait_for_completion:
            self._wait_for_completion(pipeline_id)

    def lock(self, pipeline_id: int) -> None:
        response = put_pipeline_lock_resource.sync_detailed(
            client=self._client,
            id_=pipeline_id,
            json_body=BoolLocked(locked=True),
        )
        assert_success(response)

    def predict(
        self,
        pipeline_id: int,
        horizon: int,
        regressor: RegressorType,
        new_data: Optional[pd.DataFrame] = None,
        filter_target_names: Optional[List[str]] = None,
    ) -> List[PredictResponse]:
        filter_target_names_as_json = (
            json.dumps(filter_target_names) if filter_target_names is not None else None
        )

        if new_data is None:
            prediction_response_list = post_on_demand_predict_resource.sync_detailed(
                client=self._client,
                id_=pipeline_id,
                json_body=OnDemandPredictForm(
                    horizon=horizon,
                    regressor=regressor,
                    filter_target_names=filter_target_names_as_json,
                ),
            )

            return return_value_or_raise_error(prediction_response_list).predict_responses
        else:
            str_buffer = io.StringIO(new_data.to_csv(encoding="utf-8", index=False))
            str_buffer.seek(0)
            str_buffer.name = "new data.csv"

            prediction_responses = post_predict_resource.sync_detailed(
                client=self._client,
                id_=pipeline_id,
                multipart_data=ExpertPredictForm(
                    horizon=horizon,
                    regressor=regressor,
                    filter_target_names=filter_target_names_as_json,
                    options="{}",
                    file=File(
                        payload=str_buffer,
                        file_name=str_buffer.name,
                        mime_type="text/csv",
                    ),
                ),
            )

            return return_value_or_raise_error(prediction_responses)

    def download_features(
        self,
        pipeline_id: int,
        horizon: int,
        include_targets: bool,
    ) -> pd.DataFrame:
        pipeline = self.get(pipeline_id)
        last_stage = pipeline.stages[-1]

        features_response = get_feature_export_resource.sync_detailed(
            client=self._client,
            id_=pipeline_id,
            stage_id=last_stage.id_,
            horizon=horizon,
            include_targets=include_targets,
        )

        data_file = return_value_or_raise_error(features_response)
        return pd.read_csv(data_file.payload)

    def get_feature_graph(self, pipeline_id: int) -> List[NodeAndLink]:
        pipeline = self.get(pipeline_id)
        last_stage = pipeline.stages[-1]

        graph_response = get_feature_nodes_and_links_resource.sync_detailed(
            client=self._client,
            id_=pipeline_id,
            stage_id=last_stage.id_,
        )

        graph_data = return_value_or_raise_error(graph_response)
        return graph_data.nodes_and_links

    def _wait_for_completion(self, pipeline_id: int) -> None:
        pipeline = self.get(pipeline_id)

        while not all(stage.status == StageStatus.COMPLETE for stage in pipeline.stages):
            time.sleep(2)

            pipeline = self.get(pipeline_id)
            errored_stages = [
                stage for stage in pipeline.stages if stage.status == StageStatus.ERROR
            ]

            if len(errored_stages) > 0:
                raise RuntimeError(errored_stages[0].error_msg)
