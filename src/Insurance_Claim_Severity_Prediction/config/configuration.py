from src.Insurance_Claim_Severity_Prediction.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from src.Insurance_Claim_Severity_Prediction.constants import *
from src.Insurance_Claim_Severity_Prediction.utils.common import read_yaml,create_dir

class ConfigManager:
    def __init__(
        self,
        config_file=CONFIG_FILE_PATH,
        schema_file=SCHEMA_FILE_PATH,
        params_file=PARAMS_FILE_PATH):

        self.config=read_yaml(config_file)
        self.schema=read_yaml(schema_file)
        self.params=read_yaml(params_file)

        create_dir([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion

        create_dir([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS

        create_dir([config.root_dir])

        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_path=config.unzip_data_path,
            STATUS_FILE=config. STATUS_FILE,
            all_schema=schema)
        
        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config=self.config.data_transformation

        create_dir([config.root_dir])

        data_transforming_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transforming_config
