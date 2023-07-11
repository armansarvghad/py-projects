import dlib
import cv2

# Initialize the correlation tracker
tracker = dlib.correlation_tracker()

def track_single_object(image):
    global tracker

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Check if the tracker is not initialized
    if not tracker.get_position():
        # Select the object to track
        bbox = cv2.selectROI("SingleObjectTracker", image)

        # Initialize the tracker with the selected object
        tracker.start_track(gray, dlib.rectangle(*bbox))
    else:
        # Update the tracker on the current frame
        tracker.update(gray)
        pos = tracker.get_position()
        x = int(pos.left())
        y = int(pos.top())
        w = int(pos.width())
        h = int(pos.height())

        # Draw a bounding box around the tracked object
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting image
    cv2.imshow("SingleObjectTracker", image)
    cv2.waitKey(1)

# Open a video capture object
video = cv2.VideoCapture("path_to_video")

while True:
    ret, frame = video.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Track a single object in the current frame
    track_single_object(frame)

# Release the video capture object and close the windows
video.release()
cv2.destroyAllWindows()
