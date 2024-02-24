import cv2
from assistant import speak
def images():
    
    # Initialize the video capture object using the default webcam
    cap = cv2.VideoCapture(0)

    # Set the width and height of the video capture object
    cap.set(3, 640) # Width
    cap.set(4, 480) # Height

    # Set the counter for the number of images captured
    name = input("Enter your name:")
    speak(name)
    while True:
        # Read the frame from the video capture object
        ret, frame = cap.read()

        # Show the image
        cv2.imshow('Camera', frame)

        # Save the image if the user presses the "s" key
        if cv2.waitKey(1) & 0xFF == ord('s'):
            # Set the file name and path for the image
            file_name = "dataset/" + name + ".png"

            # Save the image to the specified file path
            cv2.imwrite(file_name, frame)

            # Print a message to the console
            print("Image captured and saved as " + file_name)
        # Exit the loop if the user presses the "q" key or captures 10 images
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()




import face_recognition
import os, sys
import cv2
import numpy as np
import math


# Helper
def face_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'


class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True
 
    def __init__(self):
        self.encode_faces()

    def encode_faces(self):
        for image in os.listdir('dataset'):
            face_image = face_recognition.load_image_file(f"dataset/{image}")
            face_encoding = face_recognition.face_encodings(face_image)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(image)
        print(self.known_face_names)

    def run_recognition(self):
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            sys.exit('Video source not found...')

        while True:
            ret, frame = video_capture.read()

            # Only process every other frame of video to save time
            if self.process_current_frame:
                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

                # Find all the faces and face encodings in the current frame of video
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"
                    confidence = '???'

                    # Calculate the shortest distance to face
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)

                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                        confidence = face_confidence(face_distances[best_match_index])

                    self.face_names.append(f'{name} ({confidence})')
                    

                    print(f"Detected: {name} ({confidence})")
                    speak(f"Detected: {name} ({confidence})")

            self.process_current_frame = not self.process_current_frame

            if len(self.face_names) > 0:
                for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                    # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    # Create the frame with the name
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

            else:
                print('Not detected')
                speak('Not detected')
           
            # Display the resulting image
            cv2.imshow('Face Recognition', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    
    #fr = FaceRecognition()
    #fr.run_recognition()

    x = input("Do you want to add your photo to the dataset?\n yes/no\t")
    speak("Do you want to add your photo to the dataset?\n yes/no\t")

    if(x=='yes' or x=='Yes'):
       images()

    elif(x=='NO' or x=='no'):  
       exit

    y = input("Do you want to detect your face?\n yes/no\t")
    speak(y)
    if(y=='yes' or y=='Yes'):
        fr = FaceRecognition()
        fr.run_recognition()

    elif(y=='NO' or y=='no'):  
        exit

