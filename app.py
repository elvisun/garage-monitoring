import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from flask import Flask
from flask import jsonify

def run_prediction():

    fileContent = tf.io.read_file('test.jpg', name="loadFile")
    image = tf.image.decode_jpeg(fileContent, name="decodeJpeg")

    resize_nearest_neighbor = tf.image.resize(image, size=[224,224], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)

    # Load TFLite model and allocate tensors.
    interpreter = tf.lite.Interpreter(model_path="model.tflite")
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    print(input_details)
    print(output_details)

    resize_nearest_neighbor = tf.compat.v2.reshape(resize_nearest_neighbor, [1, 224, 224, 3])


    interpreter.set_tensor(input_details[0]['index'], resize_nearest_neighbor)

    interpreter.invoke()

    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]

    output_data = output_data / 255

    return output_data

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/predict")
def predict():
    result = run_prediction().tolist()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
