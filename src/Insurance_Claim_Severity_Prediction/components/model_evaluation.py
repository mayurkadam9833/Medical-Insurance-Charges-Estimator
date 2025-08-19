import json
import joblib 
import pandas as pd 
from pathlib import Path
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error,root_mean_squared_error
from src.Insurance_Claim_Severity_Prediction.entity.config_entity import ModelEvaluationConfig
from src.Insurance_Claim_Severity_Prediction.utils.common import save_json


class ModelEvalution:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config 

    def get_metrics(self,actual,predicted,data):
        def adjusted_r2_score(actual,predicted,data):
            r2=r2_score(actual,predicted)
            k=data.shape[1]
            n=data.shape[0]

            return 1 - (1 - r2) * (n - 1) / (n - k - 1)

        r2=r2_score(actual,predicted)
        adjusted_r2=adjusted_r2_score(actual,predicted,data)
        mse=mean_squared_error(actual,predicted)
        mae=mean_absolute_error(actual,predicted)
        rmse=root_mean_squared_error(actual,predicted)
        return r2,adjusted_r2,mse,mae,rmse
        

    def evaluation(self):
        try:
            test_data=pd.read_csv(self.config.test_data_path)
            model=joblib.load(self.config.model_path)

            test_x=test_data.drop([self.config.target_column],axis=1)
            test_y=test_data[self.config.target_column]

            prediction=model.predict(test_x)

            (r2,adj_r2,mse,mae,rmse)=self.get_metrics(test_y,prediction,test_x)

            scores={"r2_score":r2,"adjusted r2 score":adj_r2,"mean squared error":mse,"mean absolute error":mae,"root mean squared error":rmse}
            
            save_json(Path(self.config.metric_file),scores)
        
        except Exception as e:
            raise e

