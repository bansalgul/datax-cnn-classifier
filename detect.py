import streamlit as st
import numpy as np
import face_recognition
from PIL import Image, ImageDraw

def detect_faces(image):
    # Convert image to RGB format
    rgb_image = image.convert("RGB")
    rgb_array = np.array(rgb_image)
    # Find face locations in the image
    face_locations = face_recognition.face_locations(rgb_array)
    return face_locations

def draw_boxes(image, face_locations):
    # Draw rectangles around detected faces
    draw = ImageDraw.Draw(image)
    for top, right, bottom, left in face_locations:
        draw.rectangle(((left, top), (right, bottom)), outline="red", width=2)
    return image

def main():
    st.title("Face Detection App")
    st.write("Upload an image to detect faces")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Detect faces in the image
        face_locations = detect_faces(image)

        # Draw boxes around detected faces
        if face_locations:
            image_with_boxes = draw_boxes(image.copy(), face_locations)
            st.image(image_with_boxes, caption="Detected Faces", use_column_width=True)
        else:
            st.write("No faces detected in the image")

if __name__ == "__main__":
    main()
