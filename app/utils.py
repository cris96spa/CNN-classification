import os
import logging
import numpy as np
import cv2

def load_images_from_folder(folder: str):
	"""Load images from a folder. The images are resized to 224x224 and normalized.

	Args:
		folder (str): The folder containing the images.
	Returns:
		list: A list of images.

	"""
	images = []
	for filename in os.listdir(folder):
		img = cv2.imread(os.path.join(folder, filename))
		if img is not None:
			# Normalize the pixel values
			img = (img / 255.0).astype(np.float32)

			# Convert the image from BGR to RGB
			img = img[:, :, ::-1]

			# Square crop the image
			# Get min among width and height
			dim = min(img.shape[:-1])
			# Get the starting point for the crop
			start_x = (img.shape[0]-dim)//2
			start_y = (img.shape[1]-dim)//2
			# Crop the image
			img = img[start_x:(start_x+dim), start_y:(start_y+dim)]

			# Resize the image to 224x224
			img = cv2.resize(img, (224, 224))
			images.append(img)
	return np.array(images)

