from cnnClassifier.config.configuration import configurationManager
from cnnClassifier.components.model_evaluation import ModelEvaluation
from cnnClassifier import logger


STAGE_NAME = "Model Evaluation with MLflow"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManager()
        eval_config = config.get_model_evaluation_config()
        evaluation= ModelEvaluation(config=eval_config)
        evaluation.evaluate_model()
        evaluation.save_scores()
        evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e