from src.Medical_Insurance_Charges_Estimator.config.configuration import ConfigManager
from src.Medical_Insurance_Charges_Estimator.components.data_ingestion import DataIngestion
from src.Medical_Insurance_Charges_Estimator.logging import logger


# DataIngestionPipeline -> used to call data ingestion  download file and extract at defined file location
class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_file()


