# Image Classifier with Streamlit

This is a simple image classifier web application built with Streamlit. It allows users to upload an image and get a prediction whether the image is classified as "Manga Art style" or "Classic Art style". The classifier is based on a pre-trained model.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Streamlit
- TensorFlow
- Keras
- PIL (Python Imaging Library)

You can install the required packages using pip:

```
pip install streamlit tensorflow keras pillow
```

### Usage

To run the application, execute the following command:

```
streamlit run app.py
```

Once the server starts, navigate to the provided URL (usually localhost) in your web browser to access the application.

## How it Works

1. **Upload Image**: Users can upload an image file (in JPG, JPEG, or PNG format) using the file uploader.

2. **Image Display**: The uploaded image is displayed on the web interface.

3. **Prediction**: The uploaded image is preprocessed and passed through a pre-trained convolutional neural network (CNN) model to make a prediction. The model classifies the image into either "Manga Art style" or "Classic Art style" based on the features learned during training.

4. **Result Display**: The prediction result is displayed below the uploaded image, indicating whether it belongs to the "Manga Art style" or "Classic Art style".

## Model Details

The model used for classification is loaded from a saved Keras model file (`model_best.h5`). It is a CNN model trained on a dataset containing images of both "Manga Art style" and "Classic Art style". The model architecture and training details can be found in the code.

## Authors

- [Gul Bansal](https://github.com/bansalgul)

