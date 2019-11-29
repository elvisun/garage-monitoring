import numpy as np
import tensorflow as tf
from sms import send_message 

LABELS = [
    'both_open', 
    'closed',
    'left_open',
    'right_open',
]

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

    max_index = np.argmax(output_data)

    return (max_index, output_data[max_index])

if __name__ == "__main__":
    result = run_prediction()
    index = result[0]
    confidence = result[1]/255.0
    print(LABELS[index])
    print(confidence)
    send_message("door is closed!")
