import pandas as pd
from src.Medical_Insurance_Charges_Estimator.entity.config_entity import DataValidationConfig

# DataValidation class -> used to validate dataset schema and datatypes
class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    # method to check if dataset columns match schema columns
    def schema_validation(self):
        try:
            schema_status=True
            data=pd.read_csv(self.config.unzip_data_path)  # read dataset
            all_cols=list(data.columns)                    # get dataset column names
            all_schema=self.config.all_schema.keys()       # schema column names

            # loop through dataset columns and check against schema
            for col in all_cols:
                if col == "charges":
                    continue
                if col not in all_schema:
                    schema_status=False
                    
                with open(self.config.STATUS_FILE,"w")as file:
                    file.write(f"schema status: {schema_status}")

        except Exception as e:
            raise e
        
        return schema_status

