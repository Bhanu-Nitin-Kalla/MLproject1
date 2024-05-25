import numpy as np
import cv2

# Capture video from the default camera
video_capture = cv2.VideoCapture(0)
# Set the width and height of the video capture
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # Read a frame from the video capture
    ret, frame = video_capture.read()
    
    # Flip the frame vertically (comment out if not needed)
    frame = cv2.flip(frame, -1)
    
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the original frame in a window
    cv2.imshow('Original Frame', frame)
    # Display the grayscale frame in a window
    cv2.imshow('Grayscale Frame', gray_frame)

    # Check if the ESC key is pressed to exit the loop
    if cv2.waitKey(30) & 0xFF == 27:
        break

# Release the video capture object and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
