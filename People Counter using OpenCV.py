import cv2

# Initialize video capture
cap = cv2.VideoCapture(0)

# Read the first frame
ret, frame = cap.read()

# Select the initial ROI
bbox = cv2.selectROI(frame, False)

# Preprocess the frame
frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Initialize CAMShift tracker
roi_hist = cv2.calcHist([frame_hsv], [0], None, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    # Read the frame
    ret, frame = cap.read()

    if not ret:
        break

    # Preprocess the frame
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Apply CAMShift algorithm
    dst = cv2.calcBackProject([frame_hsv], [0], roi_hist, [0, 180], 1)
    ret, bbox = cv2.CamShift(dst, bbox, term_crit)

    # Draw rectangle around the tracked object
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Object Tracking', frame)

    # Exit if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()

# Close all windows
cv2.destroyAllWindows()
