import os
import urllib.request as request
from pathlib import Path
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self,) -> str:

        try:
            dataset_url = self.config.source_URL
            zip_downloaded_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading file from :[{dataset_url}] into :[{zip_downloaded_dir}]")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id, zip_downloaded_dir)

            logger.info(f"File :[{zip_downloaded_dir}] has been downloaded successfully.")
            logger.info(f"File size :[{get_size(Path(zip_downloaded_dir))}]")

        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        try:
            unzip_dir = self.config.unzip_dir
            os.makedirs(unzip_dir, exist_ok=True)

            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
            logger.info(f"Extraction completed successfully.")

        except Exception as e:
            raise e