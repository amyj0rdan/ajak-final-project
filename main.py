from flask import Flask, render_template, request
import sys
from PIL import Image
sys.path.append('./lib')
from drawing import *
from prediction import *
import base64
import re

app = Flask(__name__)

# decoding an image from base64 into raw representation
def convertImage(imgData1):
    imgstr = re.search(r'base64,(.*)', str(imgData1)).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict/', methods=['GET', 'POST'])
def predict():

    imgData = request.get_data()
    imgData = convertImage(imgData)
    imgData = Image.open("output.png")
    drawing = Drawing(imgData)
    drawing = drawing.reshape()
    prediction = Prediction(drawing)
    return prediction.predict()

if __name__ == "__main__":
    app.run(debug=True)
