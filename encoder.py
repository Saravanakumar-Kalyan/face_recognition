import face_recognition
from pathlib import Path
import pickle

DEFAULT_PATH = Path("output/encodings.pkl")


def encodeKnownFaces(model :str = 'hog', encodings_location: Path = DEFAULT_PATH):
    names = []
    encodings = []
    for filepath in Path('training').glob("*/*"):
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)

        face_locations = face_recognition.face_locations(image, model = model)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)
    
    with encodings_location.open(mode='rb') as f:
        loaded_encodings = pickle.load(f)
    
    loaded_encodings['names'].extend(names)
    loaded_encodings['encodings'].extend(encodings)
    
    with encodings_location.open(mode="wb") as f:
        pickle.dump(loaded_encodings, f)