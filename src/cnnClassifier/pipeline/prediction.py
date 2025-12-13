# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import os



# class PredictionPipeline:
#     def __init__(self,filename):
#         self.filename =filename


    
#     def predict(self):
#         # load model
#         model = load_model(os.path.join("artifacts", "training", "model.h5"))

#         imagename = self.filename
#         test_image = image.load_img(imagename, target_size = (224,224))
#         test_image = image.img_to_array(test_image)
#         test_image = np.expand_dims(test_image, axis = 0)
#         result = np.argmax(model.predict(test_image), axis=1)
#         print(result)

#         if result[0] == 1:
#             prediction = 'Tumor'
#             return [{ "image" : prediction}]
#         else:
#             prediction = 'Normal'
#             return [{ "image" : prediction}]

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        # Load & preprocess image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # 🔴 CRITICAL FIX
        test_image = preprocess_input(test_image)

        # Predict
        prediction = model.predict(test_image)
        print("Raw prediction:", prediction)

        result = np.argmax(prediction, axis=1)
        print("Class index:", result)

        if result[0] == 1:
            return [{"image": "Tumor"}]
        else:
            return [{"image": "Normal"}]
