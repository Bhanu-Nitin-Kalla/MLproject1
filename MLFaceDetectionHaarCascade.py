import cv2

# Initialize the Haar Cascade face detector with pre-trained data
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to perform face detection on an image
def detect_faces(image_path):
    # Load the image from the specified path
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image '{image_path}'")
        return

    # Convert the image to grayscale for the face detection algorithm
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Perform the face detection
    detected_faces = face_detector.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around each detected face
    for (x, y, width, height) in detected_faces:
        cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 2)
    
    # Display the image with detected faces
    cv2.imshow('Detected Faces', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage: Detect faces in a provided image file
detect_faces('sample_image.jpg')
