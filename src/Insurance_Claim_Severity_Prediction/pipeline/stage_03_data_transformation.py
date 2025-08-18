from src.Insurance_Claim_Severity_Prediction.logging import logger
from src.Insurance_Claim_Severity_Prediction.config.configuration import ConfigManager
from src.Insurance_Claim_Severity_Prediction.components.data_transformation import DataTransformation


stage_three="Data Transformation"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.data_encoding()
        data_transformation.scale_split_data()

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_three} started")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f"stage: {stage_three} >>>>")
    except Exception as e:
        logger.info(e)
        raise e