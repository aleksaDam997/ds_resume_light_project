from src.ds_resume_light_project.components.data_ingestion import DataIngestion
from src.ds_resume_light_project.config.configuration import ConfigurationManager
from src.ds_resume_light_project import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass

    def initiate_data_ingestion(self):

        config = ConfigurationManager()
        get_data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = get_data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"Error in stage {STAGE_NAME}")
        raise e