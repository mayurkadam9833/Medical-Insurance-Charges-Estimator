from src.Medical_Insurance_Charges_Estimator.logging import logger
from src.Medical_Insurance_Charges_Estimator.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.Medical_Insurance_Charges_Estimator.pipeline.stage_02_data_validation import DataValidationPipeline
from src.Medical_Insurance_Charges_Estimator.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.Medical_Insurance_Charges_Estimator.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.Medical_Insurance_Charges_Estimator.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


# data ingestion pipeline [download data from source url and extract to defined path]
stage_one="Data Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_one} started")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"stage: {stage_one} completed >>>>\n")
    except Exception as e:
        logger.info(e)
        raise e

# data valiadtion pipeline [validated the defined schema and data type with collected data]
stage_two="Data Validation"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_two} started")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"stage: {stage_two} completed")
    except Exception as e:
        logger.info(e)
        raise e

# data transformation pipeline [preprocess data and split into tain and test]
stage_three="Data Transformation"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_three} started")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f"stage: {stage_three} >>>>")
    except Exception as e:
        logger.info(e)
        raise e
    
# model trainer pipeline [train model with train data]
stage_four="Model Trainer"

if __name__  == "__main__":
    try:
        logger.info(f"<<<< stage:{stage_four} started")
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f"stage: {stage_four} completed >>>>")
    except Exception as e:
        logger.info(e)
        raise e

# model evaluation pipeline [evaluated model and save metrics file in json folder ] 
stage_five="Model Evaluation"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_five} started")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f"stage: {stage_five}completed >>>>")
    except Exception as e:
        logger.info(e)
        raise e