import numpy as np
import tensorflow as tf
from sms import send_message 
import time

BOTH_OPEN = 'both_open'
CLOSED = 'closed'
LEFT_OPEN = 'left_open'
RIGHT_OPEN = 'right_open'

LABELS = [
    BOTH_OPEN, 
    CLOSED,
    LEFT_OPEN,
    RIGHT_OPEN,
]

def run_prediction():
    fileContent = tf.io.read_file('live.jpg', name="loadFile")
    image = tf.image.decode_jpeg(fileContent, name="decodeJpeg")

    resize_nearest_neighbor = tf.image.resize(image, size=[224,224], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)

    # Load TFLite model and allocate tensors.
    interpreter = tf.lite.Interpreter(model_path="model.tflite")
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    resize_nearest_neighbor = tf.compat.v2.reshape(resize_nearest_neighbor, [1, 224, 224, 3])


    interpreter.set_tensor(input_details[0]['index'], resize_nearest_neighbor)

    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]

    max_index = np.argmax(output_data)

    # Return the prediction and its confidence level
    return (LABELS[max_index], output_data[max_index] / 255.0)

def is_door_open():
    predicted_state = run_prediction()
    print(predicted_state)

    if predicted_state[0] != CLOSED:
        return True
    return False

if __name__ == "__main__":
    while True:
        if is_door_open():
            # If garage door open, check again in 5 minutes
            time.sleep(5 * 60)
            if is_door_open():
                # Still open in 5 minutes, send a message
                send_message("Hey, you left your garage door open!")
        # Sleep for 10 minutes and check again
        time.sleep(10 * 60)
