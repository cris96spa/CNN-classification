# Image Classification with CNN and Data Augmentation

This project implements a Convolutional Neural Network (CNN) for image classification, specifically distinguishing between animals and items. It includes data augmentation techniques to improve model performance and is deployed using FastAPI in a Docker container.

## Project Structure

- `augmentation.ipynb`: Jupyter notebook containing the model development, training, and evaluation process.
- `Dockerfile`: Instructions for building the Docker image.
- `server.py`: FastAPI server implementation for model inference.
- `requirements.txt`: List of Python dependencies.

## Features

- CNN-based image classification
- Data augmentation techniques:
  - Random Flip
  - Random Translation
  - Random Rotation
  - Random Zoom
  - Random Brightness
  - Random Contrast
- Model comparison: vanilla CNN vs. CNN with augmentation
- FastAPI server for easy deployment and inference
- Dockerized application for portability

## Requirements

- Python 3.12
- Docker

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/image-classification-project.git
   cd image-classification-project
   ```

2. Build the Docker image:
   ```
   docker build -t image-classification-app .
   ```

3. Run the Docker container:
   ```
   docker run -p 8000:8000 image-classification-app
   ```

The FastAPI server will now be running on `http://localhost:8000`.

## Usage

### Training the Model

To train the model and experiment with data augmentation:

1. Open `augmentation.ipynb` in Jupyter Notebook or JupyterLab.
2. Run the cells to load the data, train the models, and compare performance.

### Making Predictions

Once the server is running, you can make predictions using the `/predict` endpoint:

```python
import requests

url = "http://localhost:8000/predict"
params = {"image_path": "/path/to/your/image.jpg"}

response = requests.post(url, json=params)
print(response.json())
```

## Model Performance

The notebook compares the performance of a vanilla CNN against a CNN with data augmentation. The augmented model typically shows improved validation accuracy and reduced overfitting.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

[Add your chosen license here]

## Contact

[Your Name] - [Your Email]

Project Link: https://github.com/your-username/image-classification-project
