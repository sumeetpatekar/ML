import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

@dataclass
class DataIngestion:
    train_Data_path: str = os.path.join('artifacts', 'train.csv')
    test_Data_path: str = os.path.join('artifacts', 'test.csv')
    raw_Data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestionComponent:
    def __init__(self):
        self.ingestion_config = DataIngestion()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method started")
        try:
            df = pd.read_csv('src/notebook/data/stud.csv')
            logging.info("Dataset read as pandas dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_Data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_Data_path, index=False)
            logging.info("Raw data is saved")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_Data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_Data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_Data_path,
                self.ingestion_config.test_Data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestionComponent()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr = data_transformation.initiate_data_transformation(train_data,test_data)

    ModelTrainer = ModelTrainer()
    print(ModelTrainer.initiate_model_trainer(train_arr,test_arr))
   