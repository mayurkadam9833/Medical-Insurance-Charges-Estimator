import os
import zipfile
from urllib.request import urlretrieve
from src.Medical_Insurance_Charges_Estimator.logging import logger
from src.Medical_Insurance_Charges_Estimator.entity.config_entity import DataIngestionConfig
from src.Medical_Insurance_Charges_Estimator.utils.common import get_size

# DataIngestion class -> used to download and extract dataset
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    # method to download dataset from url
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            # download file from source_url and save to local_data_file
            filename,header=urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{self.config.local_data_file} download sucessfully from folllowing header:\n{header}")

        else:
             # if file already exists, log the size of the file
            logger.info(f"{self.config.local_data_file} is already exits of size:{get_size(self.config.local_data_file)}")

    # method to unzip dataset
    def extract_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True) # create folder if not exists
        with zipfile.ZipFile(self.config.local_data_file,"r")as zipref:
            zipref.extractall(unzip_path)      # extract all files inside unzip_dir

