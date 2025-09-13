from src.Insurance_Claim_Severity_Prediction.config.configuration import ConfigManager
from src.Insurance_Claim_Severity_Prediction.components.model_evaluation import ModelEvalution
from src.Insurance_Claim_Severity_Prediction.logging import logger



# ModelEvaluationPipeline -> used for calling model evaluation config and methods
class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvalution(config=model_evaluation_config)
        model_evaluation.evaluation()
