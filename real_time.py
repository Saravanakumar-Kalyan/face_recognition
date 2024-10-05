import pickle
import face_recognition
import cv2
import numpy as np
from pathlib import Path
import attendance

DEFAULT_PATH = Path("output/encodings.pkl")

def encode(encodings_location: Path = DEFAULT_PATH):
    names = []
    encodings = []
    for file in Path('training').glob("*/*"):
        name = file.parent.name
        image = face_recognition.load_image_file(file)
        face_encoding = face_recognition.face_encodings(image, model="large")[0]

        names.append(name)
        encodings.append(face_encoding)
    
    encoding = {
        "names":names,
        "encodings":encodings
    }
    with encodings_location.open(mode='wb') as f:
        pickle.dump(encoding, f)

def main(location: Path = DEFAULT_PATH):
    face_locations = []
    face_encodings = []
    face_names = []
    this = True
    with location.open(mode='rb') as f:
        known_encodings = pickle.load(f)
    
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    names=[]

    while True:
        ret, frame = video.read()

        frame = cv2.flip(frame, 1)
        convertedImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(convertedImage)
        face_encodings = face_recognition.face_encodings(convertedImage, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings['encodings'], face_encoding, tolerance = 0.4)
            name = 'Unknown'

            if True in matches:
                index = matches.index(True)
                name = known_encodings['names'][index]

            #face_distances = face_recognition.face_distance(known_encodings['encodings'], face_encoding)
            #best_match_index = np.argmin(face_distances)
            #if matches[best_match_index]:
            #    name = known_encodings['names'][best_match_index]
            face_names.append(name)
        this = not this
        names.extend(face_names)

        for(top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
        cv2.imshow('Attendance System', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    attendance.takeAttendance(names)
    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    encode()
    main()