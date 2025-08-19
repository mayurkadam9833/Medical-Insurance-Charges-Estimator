from src.Insurance_Claim_Severity_Prediction.config.configuration import ConfigManager
from src.Insurance_Claim_Severity_Prediction.components.model_evaluation import ModelEvalution
from src.Insurance_Claim_Severity_Prediction.logging import logger


stage_five="Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvalution(config=model_evaluation_config)
        model_evaluation.evaluation()

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_five} started")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f"stage: {stage_five}completed >>>>")
    except Exception as e:
        logger.info(e)
        raise e