from src.ds_resume_light_project.config.configuration import ConfigurationManager
from src.ds_resume_light_project.components.model_evaluation import modelEvaluation
from src.ds_resume_light_project import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = modelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()