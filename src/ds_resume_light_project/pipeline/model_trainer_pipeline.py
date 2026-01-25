from src.ds_resume_light_project.config.configuration import ConfigurationManager
from src.ds_resume_light_project.components.model_trainer import ModelTrainer
from src.ds_resume_light_project import logger

STAGE_NAME = "Data Trainer Stage"

class ModeltrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == "__main__":
    try:
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
    except Exception as e:
        raise e


