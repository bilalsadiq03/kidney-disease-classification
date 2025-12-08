import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from cnnClassifier.entity.config_entity import ModelEvaluationConfig
from cnnClassifier.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def _valid_generator(self):

        datagen_kwargs = dict(
            rescale=1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(**datagen_kwargs)

        self.valid_generator = valid_datagen.flow_from_directory(
            directory=self.config.tarining_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(model_path: Path) -> tf.keras.Model:
        model = tf.keras.models.load_model(model_path)
        return model
    
    def evaluate_model(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.scores = self.model.evaluate(self.valid_generator)
        self.save_scores()
    
        

    def save_scores(self):
        scores = {"loss": self.scores[0],
                  "accuracy": self.scores[1]
        }
        save_json(path=Path("scores.json"), data=scores)
    
    def log_into_mlflow(self):
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(self.config.mlflow_uri).scheme
        

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("loss", self.scores[0])
            mlflow.log_metric("accuracy", self.scores[1])

            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
            else:
                mlflow.keras.log_model(self.model, "model")


            