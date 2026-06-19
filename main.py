from network_security.components.data_ingestion import DataIngestion
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

from network_security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

if __name__=="__main__":
    try:
        training_pipeline_config=TrainingPipelineConfig()
        
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        logging.info("Data Ingestion stage started")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info(data_ingestion_artifact.trained_file_path)
        print(data_ingestion_artifact.trained_file_path)

        
    except Exception as e:
        logging.exception(e)
        raise
