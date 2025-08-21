import pandas as pd
from src.Insurance_Claim_Severity_Prediction.entity.config_entity import DataValidationConfig

# DataValidation class -> used to validate dataset schema and datatypes
class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    # method to check if dataset columns match schema columns
    def schema_validation(self):
        try:
            schema_status=None
            data=pd.read_csv(self.config.unzip_data_path) # read dataset
            all_cols=list(data.columns)                   # get dataset column names
            all_schema=self.config.all_schema.keys()      # schema column names

            # loop through dataset columns and check against schema
            for col in all_cols:
                if col not in all_schema:
                    schema_status=False
                    with open(self.config.STATUS_FILE,"w")as file:
                        file.write(f"schema status: {schema_status}")
                
                else:
                    schema_status=True
                    with open(self.config.STATUS_FILE,"a")as file:
                        file.write(f"schema status: {schema_status}")
        
        except Exception as e:
            raise e
        
        return schema_status
    
    # method to check if dataset column datatypes match schema datatypes
    def data_type_validation(self):
        try:
            data_type_status=None
            data=pd.read_csv(self.config.unzip_data_path)  # read dataset
            all_data_type=list(data.dtypes)               # get datatypes of dataset columns
            all_schema=self.config.all_schema.values()    # expected datatypes from schema
            
            # loop through dataset datatypes and check against schema
            for data_type in all_data_type:
                if data_type not in all_schema:
                    data_type_status=False
                    with open(self.config.STATUS_FILE,"w")as file:
                        file.write(f"\ndata type status: {data_type_status}")
                
                else:
                    data_type_status=True
                    with open(self.config.STATUS_FILE,"a")as file:
                        file.write(f"\ndata type status: {data_type_status}")
        
        except Exception as e:
            raise e
        return data_type_status

