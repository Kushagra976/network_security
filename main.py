from network_security.components.data_ingestion import DataIngestion
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.components.data_validation import DataValidation
from network_security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig,DataTransformationConfig
from network_security.components.data_transformation import DataTransformation
from network_security.entity.config_entity import ModelTrainerConfig
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
        logging.info("Data Transformation stage started")
        data_transformation_config=DataTransformationConfig(training_pipeline_config)
        data_transformation=DataTransformation(data_transformation_config,data_validation_artifact)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation stage completed")

        logging.info("Model trainer started")
        from network_security.components.model_trainer import ModelTrainer
        model_trainer_config=ModelTrainerConfig(training_pipeline_config)
        model_trainer=ModelTrainer(model_trainer_config,data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        print(model_trainer_artifact)
        logging.info("Model trainer completed")

    except Exception as e:
        logging.exception(e)
        raise
