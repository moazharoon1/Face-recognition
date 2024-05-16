import cv2
import numpy as np
import face_recognition
import json

try:
    with open('face_data.json', 'r') as json_file:
        data = json.load(json_file)
    known_face_encodings = [np.array(face) for sublist in data.values() for face in sublist]
    known_face_ids = [emp_id for emp_id, face_list in data.items() for _ in face_list]
except (FileNotFoundError, json.JSONDecodeError):
    print("Error reading the JSON file or the file might be empty.")
    known_face_encodings = []
    known_face_ids = []

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    cv2.imshow("Press 'q' to take a photo", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


new_face_encodings = face_recognition.face_encodings(rgb_frame)

if not new_face_encodings:
    print("No face detected!")
else:
    matches = face_recognition.compare_faces(known_face_encodings, new_face_encodings[0], tolerance=0.5)

    for match, emp_id in zip(matches, known_face_ids):
        if match:
            print(f"Matched with Employee ID: {emp_id}")
            break
    else:
        print("No match found!")