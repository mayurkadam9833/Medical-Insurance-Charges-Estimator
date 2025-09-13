from src.Medical_Insurance_Charges_Estimator.logging import logger
from src.Medical_Insurance_Charges_Estimator.config.configuration import ConfigManager
from src.Medical_Insurance_Charges_Estimator.components.data_transformation import DataTransformation

# DataTransformationPipeline -> used for calling data transformation config and method
class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.data_encoding()
        data_transformation.scale_split_data()

