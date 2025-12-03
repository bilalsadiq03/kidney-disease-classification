import sys
sys.path.append("src")


from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionStageTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelStageTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
        data_ingestion = DataIngestionStageTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Prepare Base Model Stage"
try:
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
        prepare_base_model = PrepareBaseModelStageTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e