import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from keras.preprocessing.image import img_to_array

# Load the saved model
model = load_model("/Users/gulbansal/Documents/dataxam/model_best.h5")


def preprocess_image(image):
    # Convert the image to RGB mode if it's not already in RGB format
    if image.mode != "RGB":
        img = image.convert("RGB")
    else:
        img = image
    # Resize the image to match the input shape of the model
    img = img.resize((224, 224))
    # Convert image to array and preprocess it
    img_array = img_to_array(img)
    img_array = img_array.astype("float") / 255.0  # Normalize pixel values to [0, 1]
    return img_array


def predict_image(img_array):
    # Preprocess the image
    threshold=0.5
    preprocessed_img = img_array
    # Make prediction
    prediction = model.predict(np.expand_dims(preprocessed_img, axis=0))
    binary_prediction = 1 if prediction[0][0] > threshold else 0
    return binary_prediction

def main():
    st.title("Image Classifier")
    st.write("Upload your images here:")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Preprocess the image
        img_array = preprocess_image(image)
        # Predict the image
        prediction = predict_image(img_array)
        st.subheader('The Uploaded Image is classified as')
        # st.subheader(prediction)
        if prediction == 0:
            st.subheader('Manga Art style')
        elif prediction == 1:
            st.subheader('Classic Art style')

if __name__ == "__main__":
    main()
