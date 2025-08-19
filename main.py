from src.Insurance_Claim_Severity_Prediction.logging import logger
from src.Insurance_Claim_Severity_Prediction.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.Insurance_Claim_Severity_Prediction.pipeline.stage_02_data_validation import DataValidationPipeline
from src.Insurance_Claim_Severity_Prediction.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.Insurance_Claim_Severity_Prediction.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.Insurance_Claim_Severity_Prediction.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
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