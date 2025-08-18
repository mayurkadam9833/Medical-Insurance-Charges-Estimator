from src.Insurance_Claim_Severity_Prediction.config.configuration import ConfigManager
from src.Insurance_Claim_Severity_Prediction.components.data_validation import DataValidation
from src.Insurance_Claim_Severity_Prediction.logging import logger


stage_two="Data Validation"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.schema_validation()
        data_validation.data_type_validation()


if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_two} started")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"stage: {stage_two} completed")
    except Exception as e:
        logger.info(e)
        raise e
