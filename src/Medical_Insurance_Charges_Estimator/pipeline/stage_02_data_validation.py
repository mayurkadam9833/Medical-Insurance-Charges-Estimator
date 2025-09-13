from src.Medical_Insurance_Charges_Estimator.config.configuration import ConfigManager
from src.Medical_Insurance_Charges_Estimator.components.data_validation import DataValidation
from src.Medical_Insurance_Charges_Estimator.logging import logger

# DataValidationPipeline -> used for calling data valiadtion config and method
class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.schema_validation()


