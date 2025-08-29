import os
import joblib
import pandas as pd 
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from src.Insurance_Claim_Severity_Prediction.logging import logger
from src.Insurance_Claim_Severity_Prediction.config.configuration import ModelTrainingconfig

# ModelTrainer class -> used to train model 
class ModelTrainer:
    def __init__(self,config:ModelTrainingconfig):
        self.config=config
        self.model=GradientBoostingRegressor()
    
    # method to train model 
    def model_train(self):
        try:
            train_data=pd.read_csv(self.config.train_data_path) # read train data

            train_x=train_data.drop([self.config.target_column],axis=1) # drop target column
            train_y=train_data[self.config.target_column]               # define target column

            model=self.model.fit(train_x,train_y)                       # train model

            model_path=os.path.join(self.config.root_dir,self.config.model_name)   # save model path
            joblib.dump(model,model_path)                                          # save model 

            logger.info(f"Model trained sucessfully and saved")
        
        except Exception as e:
            logger.info(e)
            raise e

