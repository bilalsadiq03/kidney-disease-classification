from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path 
    updated_base_model_path: Path 
    params_images_size: Path
    params_learning_rate: float
    params_classes: int
    params_weights: str
    params_include_top: bool


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list