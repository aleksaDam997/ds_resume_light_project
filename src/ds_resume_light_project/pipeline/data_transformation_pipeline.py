from src.ds_resume_light_project.components.data_transformation import DataTransformation
from src.ds_resume_light_project.config.configuration import ConfigurationManager
from src.ds_resume_light_project import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:

    def __init__(self):
        pass

    def initiate_data_transformation(self):

        try:
            with open("artifacts/data_validation/status.txt", "r") as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                config = ConfigurationManager()
                get_data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config = get_data_transformation_config)
                data_transformation.train_test_split()
            else:
                logger.info(f"Data Validation is not completed. So, we cannot proceed with {STAGE_NAME}")
                raise Exception(f"Data Validation is not completed. So, we cannot proceed with {STAGE_NAME}")   
            
        except Exception as e:
            logger.exception(e)
            raise e




