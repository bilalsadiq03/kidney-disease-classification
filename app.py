from flask import Flask, request, jsonify,  render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template("index.html")



@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    print("Training Started!")
    os.system("dvc repro")
    return "Training Completed!"


@app.route("/predict", methods=['POST'])
@cross_origin()
def predict():
    image = request.json['image']
    decodeImage(image, clientApp.filename)
    prediction = clientApp.classifier.predict()
    return jsonify(prediction)



if __name__ == "__main__":
    clientApp = ClientApp()
    app.run(host='0.0.0.0', port=8080, debug=True)
