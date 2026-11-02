import cv2

# Haar cascade: a pre-trained face detector that comes with OpenCV
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Face", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, "Faces: " + str(len(faces)), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return frame


def detect_in_image():
    path = input("Enter image file name (example: photo.jpg): ").strip().strip('"')
    img = cv2.imread(path)
    if img is None:
        print("Could not open the image. Check the file name and folder.")
        return
    height, width = img.shape[:2]
    if width > 900:
        scale = 900 / width
        img = cv2.resize(img, (900, int(height * scale)))
    img = detect_faces(img)
    cv2.imwrite("output.jpg", img)
    print("Saved the result as output.jpg")
    cv2.imshow("Face Detection - press any key to close", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_with_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open the webcam.")
        return
    print("Webcam started. Press 'q' to stop.")
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        frame = detect_faces(frame)
        cv2.imshow("Face Detection - press q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


print("=== Face Detection ===")
while True:
    print("\n1. Detect faces in an image")
    print("2. Detect faces using webcam")
    print("3. Exit")
    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        detect_in_image()
    elif choice == "2":
        detect_with_webcam()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Please choose 1, 2 or 3.")