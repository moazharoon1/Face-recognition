import cv2
import dlib
import face_recognition
import json

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    cv2.imshow("Press 'q' to take a photo", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

face_encodings = face_recognition.face_encodings(rgb_frame)

if not face_encodings:
    face_locations = face_recognition.face_locations(rgb_frame)
    face_locations_dlib = [dlib.rectangle(face[3], face[0], face[1], face[2]) for face in face_locations]
    face_encodings = face_recognition.face_encodings(rgb_frame, known_face_locations=face_locations_dlib)

if not face_encodings:
    print("No face detected in the frame!")
else:
    employee_id = input("Enter the Employee ID: ")

    face_data = {
        employee_id: [face_encoding.tolist() for face_encoding in face_encodings]
    }

    try:
        with open('face_data.json', 'r') as json_file:
            data = json.load(json_file)
            data.update(face_data)
        with open('face_data.json', 'w') as json_file:
            json.dump(data, json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open('face_data.json', 'w') as json_file:
            json.dump(face_data, json_file)

    print("Data saved!")