import sys
sys.path.append("src")


from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionStageTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
        data_ingestion = DataIngestionStageTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e