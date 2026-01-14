import os
import zipfile
import gdown
from pathlib import Path
from kidneyProject import logger
from kidneyProject.utils.common import get_size
from kidneyProject.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_data(self) -> str:
        
        try:
            dataset_url = self.config.sourse_url
            zip_download_path = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True) 
            logger.info(f"Downloading file from :[{dataset_url}] to :[{zip_download_path}]")
            
            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_download_path)
            
            logger.info(f"File downloaded successfully and saved at :[{zip_download_path}]")
        
        except Exception as e:
            raise e
        
        
    def extract_zip_file(self) -> None:
        
        unzip_path = Path(self.config.unzip_dir)
        os.makedirs(unzip_path, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            logger.info(f"Extracting zip file :[{self.config.local_data_file}] to :[{unzip_path}]")
            zip_ref.extractall(unzip_path)
            logger.info(f"File extracted successfully at :[{unzip_path}] and size of data is :[{get_size(unzip_path)}]")
            
            