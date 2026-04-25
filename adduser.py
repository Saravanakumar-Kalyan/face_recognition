import csv
import os
import encoder
import cv2
from pathlib import Path

def addEntry(user):
    with open("attendance/file.csv", mode='r') as f:
        read = csv.reader(f)
        read = list(read)
        read.append([user])
        for i in range(len(read[1])-1):
            read[-1].append(str(0))
    
    with open("attendance/file.csv", mode='w') as f:
        write = csv.writer(f, lineterminator='\n')
        write.writerows(read) 

def main(user):
    #user = input("Enter the name of user: ")
    if user:
        for file in Path("training/").glob('*/*'):
            os.remove(file)
        for path in Path("training/").glob('*'):
            path.rmdir()

        Path(f"training/"+user).mkdir(exist_ok=True)
        video = cv2.VideoCapture(0)
        video.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
        video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        count = 0
        timer = 0
        print("Capturing Images")
        while True:
            result, frame = video.read()
            frame = cv2.flip(frame,1)
            keyPressed = cv2.waitKey(1) & 0xFF
            timer += 1
            if keyPressed == ord(' ') or timer%50 == 0:
                count+=1
                cv2.imwrite("training/{}/{}.jpg".format(user, count), frame)
                print("Captured image: ",count)
                frame[:] = (0,0,0)
                cv2.imshow("project", frame)
                if count==3: break
            elif keyPressed == ord('q'):
                break
            else:
                font = cv2.FONT_HERSHEY_TRIPLEX
                cv2.rectangle(frame, (0,675), (700,705), (255,0,0), cv2.FILLED)
                cv2.putText(frame, "PRESS [SPACE BAR] TO TAKE PHOTOS", (0,700), font, 1.0, (255,255,0))
                cv2.putText(frame, "Count: {}".format(count), (1000,20), font, 1.0, (0,0,0))
                cv2.imshow("project", frame)


        print("Images captured...")
        print("Encoding the faces...")
        video.release()
        cv2.destroyAllWindows()
        addEntry(user)
        encoder.encodeKnownFaces()

if __name__ == '__main__':
    main()