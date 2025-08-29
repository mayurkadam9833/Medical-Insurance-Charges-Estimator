from src.Insurance_Claim_Severity_Prediction.config.configuration import ConfigManager
from src.Insurance_Claim_Severity_Prediction.components.data_validation import DataValidation
from src.Insurance_Claim_Severity_Prediction.logging import logger

# DataValidationPipeline -> used for calling data valiadtion config and method
class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.schema_validation()
        data_validation.data_type_validation()


