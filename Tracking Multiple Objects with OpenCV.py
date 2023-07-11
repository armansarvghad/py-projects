import cv2
from random import randint

# Create MultiTracker object
multi_tracker = cv2.MultiTracker_create()

# Load the video or webcam stream
video = cv2.VideoCapture(0)  # Replace '0' with the path to the video if using a file

while True:
    # Read the current frame
    ret, frame = video.read()

    if not ret:
        break

    # Display the frame
    cv2.imshow("Frame", frame)

    # Detect objects to track (manually draw bounding boxes)
    if cv2.waitKey(1) == ord('s'):  # Press 's' to start selecting objects
        bbox = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
        multi_tracker.add(cv2.TrackerCSRT_create(), frame, bbox)

    # Update and display the tracking results
    success, boxes = multi_tracker.update(frame)

    for i, new_box in enumerate(boxes):
        p1 = (int(new_box[0]), int(new_box[1]))
        p2 = (int(new_box[0] + new_box[2]), int(new_box[1] + new_box[3]))
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        cv2.rectangle(frame, p1, p2, color, 2, 1)
        cv2.putText(frame, f"Object {i+1}", (p1[0], p1[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("Tracking", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video or webcam stream and close all windows
video.release()
cv2.destroyAllWindows()
