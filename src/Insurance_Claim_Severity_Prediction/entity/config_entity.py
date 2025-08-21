from pathlib import Path
from dataclasses import dataclass 

# config class for data ingestion step -> handles downloading and unzipping data
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path 
    source_url: str
    local_data_file: Path
    unzip_dir: Path 

# config class for data validation step -> handles schema check and validation status file
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_path: Path
    STATUS_FILE: str
    all_schema: dict

# config class for data transformation step -> handles preprocessing input data
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

# config class for model training step -> stores model parameters and training/testing paths
@dataclass(frozen=True)
class ModelTrainingconfig:
     root_dir: Path
     train_data_path: Path
     test_data_path: Path
     model_name: str
     n_estimators: int
     learning_rate: float
     max_depth: int
     min_samples_leaf: int
     min_samples_split: int 
     target_column: str

# config class for model evaluation step -> used to evaluate model with metrics and schema
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path 
    test_data_path: Path
    model_path: Path
    metric_file: Path
    target_column: str 
    all_schema: dict

