import numpy as np
import os
import sys
import tensorflow as tf
from tensorflow import keras as tfk
from fastapi import FastAPI
from app.utils import load_images_from_folder

# Set the environment variable to suppress warnings and logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'  # 0 = all logs, 1 = INFO, 2 = WARNING, 3 = ERROR

# Optionally, configure TensorFlow's logger
tf.get_logger().setLevel('ERROR')

model = tfk.models.load_model('app/augmented_model.keras')

class_map = {
	0: 'item',
	1: 'animal'
}

app = FastAPI()

@app.get('/')
def reed_root():
	return {'message': 'Image Classification API'}

@app.post('/predict')
def predict(image_path: str):
	""" Make a prediction for the image at the given path.
	
	Args:
		image_path (str): The path to the image to classify.
	
	Returns:
		dict: The predicted class of the image.
	"""
	try:
		images = load_images_from_folder(image_path)
	except Exception as e:
		return {'error': str(e)}
	try:
		predictions = model.predict(images)
	except Exception as e:
		return {'error during predictions': str(e)}
	try:
		y_pred = np.argmax(predictions, axis=1)
	except Exception as e:
		return {'error during argmax': str(e)}
	try:
		predicted_class = [class_map[x] for x in y_pred]
	except Exception as e:
		return {'error during class names': str(e)}
	return {'predicted_class': predicted_class}


if __name__ == '__main__':
	print('Starting server...')