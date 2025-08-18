import os
import joblib
import pandas as pd 
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from src.Insurance_Claim_Severity_Prediction.logging import logger
from src.Insurance_Claim_Severity_Prediction.config.configuration import ModelTrainingconfig

class ModelTrainer:
    def __init__(self,config:ModelTrainingconfig):
        self.config=config
        self.model=GradientBoostingRegressor()
    
    def model_train(self):
        try:
            train_data=pd.read_csv(self.config.train_data_path)

            train_x=train_data.drop([self.config.target_column],axis=1)
            train_y=train_data[self.config.target_column]

            model=self.model.fit(train_x,train_y)

            model_path=os.path.join(self.config.root_dir,self.config.model_name)
            joblib.dump(model,model_path)

            logger.info(f"Model trained sucessfully and saved")
        
        except Exception as e:
            logger.info(e)
            raise e

