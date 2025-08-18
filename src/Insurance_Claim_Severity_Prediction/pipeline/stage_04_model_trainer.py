from src.Insurance_Claim_Severity_Prediction.logging import logger
from src.Insurance_Claim_Severity_Prediction.config.configuration import ConfigManager
from src.Insurance_Claim_Severity_Prediction.components.model_trainer import ModelTrainer

stage_four="Model Trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        model_training_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_training_config)
        model_trainer.model_train()


if __name__  == "__main__":
    try:
        logger.info(f"<<<< stage:{stage_four} started")
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f"stage: {stage_four} completed >>>>")
    except Exception as e:
        logger.info(e)
        raise e