import os
from urllib import request
from src.ds_resume_light_project import logger
import zipfile

from src.ds_resume_light_project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"File : {filename} downloaded successfully with following info: \n{headers}")
        else:
            logger.info(f"File already exists of path: {self.config.local_data_file}")

    def extract_zip_file(self) -> None:
        """zip_file_path: str
            Extracts the zip file into the data directory
            Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"File extracted successfully at location: {unzip_path}")