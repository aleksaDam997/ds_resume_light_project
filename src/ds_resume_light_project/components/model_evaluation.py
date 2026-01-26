import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.ds_resume_light_project.entity.config_entity import ModelEvaluationConfig
from src.ds_resume_light_project.utils.common import save_json

import os
os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/aleksaDam997/ds_resume_light_project.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME'] = "aleksaDam997"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "5f1137a6498c801820d5b434ab2bf66df0bab215"

class modelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_X = test_data.drop(columns=[self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_X)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path = self.config.metric_file_name, data = scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name = "ElasticNetModel")
            else:
               mlflow.sklearn.log_model(model, "model")