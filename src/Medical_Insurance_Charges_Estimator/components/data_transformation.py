import os 
import pandas as pd 
import numpy as np 
import joblib
from src.Insurance_Claim_Severity_Prediction.logging import logger
from src.Insurance_Claim_Severity_Prediction.entity.config_entity import DataTransformationConfig
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# DataTransformation class -> used to tranform data (data preprocessing, train test split)  
class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        # store config object
        self.config=config
        # label encoders for categorical columns
        self.sex_label_encode=LabelEncoder()
        self.smoker_label_encode=LabelEncoder()
         # one-hot encoder for "region" column
        self.ohe_encode=OneHotEncoder(sparse_output=False)
        # scaler for numerical features
        self.scale=StandardScaler()

    # method to encode categorical columns
    def data_encoding(self):
        try:
            data=pd.read_csv(self.config.data_path) # read input csv
            # label encode binary categorical features
            data["sex"] = self.sex_label_encode.fit_transform(data["sex"])
            data["smoker"] = self.smoker_label_encode.fit_transform(data["smoker"])
             # one-hot encode "region" and add back to dataframe
            encode_data=pd.DataFrame(self.ohe_encode.fit_transform(data[["region"]]),columns=self.ohe_encode.get_feature_names_out())
            data=pd.concat([data.drop(["region"],axis=1),encode_data],axis=1)
            # save encoders for future use
            joblib.dump(self.sex_label_encode,os.path.join(self.config.root_dir,"sex_label_encode.joblib"))
            joblib.dump(self.smoker_label_encode,os.path.join(self.config.root_dir,"smoker_label_encode.joblib"))
            joblib.dump(self.ohe_encode,os.path.join(self.config.root_dir,"ohe_encode.joblib"))
            return data
        
        except Exception as e:
            raise e
    
    # method to scale data and split into train/test
    def scale_split_data(self):
        try:
            data=self.data_encoding()

            # split dataset into train and test
            train,test=train_test_split(data,test_size=0.2,random_state=42)
            # separate features and target
            train_x=train.drop(["charges"],axis=1)
            test_x=test.drop(["charges"],axis=1)
            train_y=train["charges"]
            test_y=test["charges"]
            
             # scale features
            scale_train_x=self.scale.fit_transform(train_x)
            scale_test_x=self.scale.transform(test_x)
             # save scaler
            joblib.dump(self.scale,os.path.join(self.config.root_dir,"scale.joblib"))

            # combine scaled features with target again
            train_data=pd.concat([pd.DataFrame(scale_train_x).reset_index(drop=True),pd.Series(train_y).reset_index(drop=True)],axis=1)
            test_data=pd.concat([pd.DataFrame(scale_test_x).reset_index(drop=True),pd.Series(test_y).reset_index(drop=True)],axis=1)
            # save train and test csv
            train_data.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
            test_data.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

            logger.info(f"train shape:{train_data.shape}")
            logger.info(f"test shape:{test_data.shape}")

        
        except Exception as e:
            raise e

            
            



