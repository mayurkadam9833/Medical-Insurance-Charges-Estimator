from pathlib import Path
from dataclasses import dataclass 


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path 
    source_url: str
    local_data_file: Path
    unzip_dir: Path 

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_path: Path
    STATUS_FILE: str
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

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


