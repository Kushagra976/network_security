from network_security.components.data_ingestion import DataIngestion
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.components.data_validation import DataValidation
from network_security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig

if __name__=="__main__":
    try:
        training_pipeline_config=TrainingPipelineConfig()
        
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        logging.info("Data Ingestion stage started")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info(data_ingestion_artifact.trained_file_path)
        print(data_ingestion_artifact.trained_file_path)
        logging.info("Data Ingestion stage completed")

        data_validation_config=DataValidationConfig(training_pipeline_config)
        data_validation=DataValidation(data_validation_config,data_ingestion_artifact)
        logging.info("Data Validation stage started")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation stage completed")
        print(data_validation_artifact)
        
    except Exception as e:
        logging.exception(e)
        raise
