import joblib
from pathlib import Path
import pandas as pd 


class PredictionPipeline:
    def __init__(self):
        self.sex_label_encode=joblib.load(Path("artifacts/data_transformation/sex_label_encode.joblib"))
        self.smoker_label_encode=joblib.load(Path("artifacts/data_transformation/smoker_label_encode.joblib"))
        self.ohe_encode=joblib.load(Path("artifacts/data_transformation/ohe_encode.joblib"))
        self.scale=joblib.load(Path("artifacts/data_transformation/scale.joblib"))
        self.model=joblib.load(Path("artifacts/model_trainer/model.joblib"))

    def preprocess(self,data:pd.DataFrame):
        data["sex"] = self.sex_label_encode.transform(data["sex"])
        data["smoker"] = self.smoker_label_encode.transform(data["smoker"])
        encode_data=pd.DataFrame(self.ohe_encode.transform(data[["region"]]),columns=self.ohe_encode.get_feature_names_out())
        data=pd.concat([data.drop(["region"],axis=1),encode_data],axis=1)
        data=self.scale.transform(data)
        return data
    
    def prediction(self,data:pd.DataFrame):
        processed=self.preprocess(data)
        prediction=self.model.predict(processed)
        return prediction
        

