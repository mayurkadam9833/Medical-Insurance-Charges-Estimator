from src.Medical_Insurance_Charges_Estimator.config.configuration import ConfigManager
from src.Medical_Insurance_Charges_Estimator.components.model_evaluation import ModelEvalution
from src.Medical_Insurance_Charges_Estimator.logging import logger



# ModelEvaluationPipeline -> used for calling model evaluation config and methods
class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvalution(config=model_evaluation_config)
        model_evaluation.evaluation()
