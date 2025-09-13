from src.Insurance_Claim_Severity_Prediction.logging import logger
from src.Insurance_Claim_Severity_Prediction.config.configuration import ConfigManager
from src.Insurance_Claim_Severity_Prediction.components.model_trainer import ModelTrainer

# ModelTrainerPipeline -> used for calling model training config and methods
class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        model_training_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_training_config)
        model_trainer.model_train()

