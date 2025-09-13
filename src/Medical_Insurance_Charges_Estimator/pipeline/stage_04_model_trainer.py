from src.Medical_Insurance_Charges_Estimator.logging import logger
from src.Medical_Insurance_Charges_Estimator.config.configuration import ConfigManager
from src.Medical_Insurance_Charges_Estimator.components.model_trainer import ModelTrainer

# ModelTrainerPipeline -> used for calling model training config and methods
class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        model_training_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_training_config)
        model_trainer.model_train()

