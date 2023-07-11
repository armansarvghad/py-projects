import dlib
import cv2

# Initialize the correlation trackers for multiple objects
trackers = []

def track_multiple_objects(image):
    global trackers

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Check if there are any existing trackers
    if len(trackers) == 0:
        # Select the objects to track and create a new tracker for each object
        objects = cv2.selectROIs("MultiObjectTracker", image)
        for (x, y, w, h) in objects:
            tracker = dlib.correlation_tracker()
            rect = dlib.rectangle(x, y, x+w, y+h)
            tracker.start_track(gray, rect)
            trackers.append(tracker)
    else:
        # Update the trackers on the current frame
        for tracker in trackers:
            tracker.update(gray)
            pos = tracker.get_position()
            x = int(pos.left())
            y = int(pos.top())
            w = int(pos.width())
            h = int(pos.height())

            # Draw a bounding box around each tracked object
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting image
    cv2.imshow("MultiObjectTracker", image)
    cv2.waitKey(1)

# Open a video capture object
video = cv2.VideoCapture("path_to_video")

while True:
    ret, frame = video.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Track multiple objects in the current frame
    track_multiple_objects(frame)

# Release the video capture object and close the windows
video.release()
cv2.destroyAllWindows()
