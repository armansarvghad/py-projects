import cv2
import numpy as np

# Load the pre-trained face recognizer from OpenCV
face_recognizer = cv2.face.EigenFaceRecognizer_create()

# Load the face images for training
face_images = []
labels = []

# Add face images and corresponding labels to the training set
face_images.append(cv2.imread("path_to_face_image_1", cv2.IMREAD_GRAYSCALE))
labels.append(1)  # Label for face image 1
face_images.append(cv2.imread("path_to_face_image_2", cv2.IMREAD_GRAYSCALE))
labels.append(2)  # Label for face image 2
# Add more face images and labels as needed

# Train the face recognizer with the training set
face_recognizer.train(face_images, np.array(labels))

# Perform face recognition on a test image
test_image = cv2.imread("path_to_test_image", cv2.IMREAD_GRAYSCALE)
label, confidence = face_recognizer.predict(test_image)

# Print the predicted label and confidence
print("Predicted label:", label)
print("Confidence:", confidence)
