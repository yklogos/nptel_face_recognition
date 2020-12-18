import torch
import cv2
import os
import numpy as np
import face_recognition
import matplotlib.pyplot as plt
from utils import save_as_pickle, load_from_pickle

fr_fl = face_recognition.face_locations
fr_fe = face_recognition.face_encodings
if torch.cuda.is_available():
    fr_fl_dict = {"number_of_times_to_upsample":3, "model":"cnn"}
    fr_fe_dict = {"num_jitters":3, "model":"large"}  
else:
    fr_fl_dict = {"number_of_times_to_upsample":1, "model":"hog"}
    fr_fe_dict = {"num_jitters":1, "model":"small"} 

def predict(vedio_path, st, base_dir, ver):
    data_dir = os.path.join(base_dir, 'data')
    known_faces_dir = os.path.join(data_dir, 'known_faces'+ver)
    full_vedios_dir = os.path.join(data_dir, 'full_vedio')
    pkl_files_dir = os.path.join(data_dir, "pkl_files")

    known_face_names = load_from_pickle(os.path.join(pkl_files_dir, "known_face_names"+ver+".pkl"))
    known_face_encodings = load_from_pickle(os.path.join(pkl_files_dir, "known_face_encodings"+ver+".pkl"))
        
    st.video(vedio_path)
    video_capture = cv2.VideoCapture(vedio_path)
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    
    vst = st.number_input("time(secs) to start the vedio from",min_value = 0, max_value=5*60,value = 15,step = 1) ### 
    vet = st.number_input("time(secs) to exit" ,min_value = 0,max_value=5*60,value = 25,step = 1)
    num_frames_per_sec = st.number_input("number of frames to process per second" ,min_value = 1,max_value=fps,value = 1,step = 1)
    
    show = st.radio("show vedio",["no", "yes"], index = 1) ###
    if show=="yes":
        i=-1
        # make empty containers to repalce outputs
        image_location = st.empty()
        image_text = st.empty()
        time_text = st.empty()
        while video_capture.isOpened():           
            i+=1
            if int(i/fps) < vst:
                ret, frame = video_capture.read()
                continue

            if int(i/fps) > vet:
                break

             # Grab a single frame of video
            ret, frame = video_capture.read()

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_frame = frame[:, :, ::-1]

            # process
            if i%int(fps/num_frames_per_sec)==0:
                face_locations = fr_fl(rgb_frame, **fr_fl_dict)
                if not len(face_locations)==1:
                    image_location.image(rgb_frame)
                    time_text.text(f"time(sec): {int(i/fps)}")
                    image_text.text("no face")
                    continue

                face_encoding = fr_fe(rgb_frame, known_face_locations = face_locations, **fr_fe_dict)[0]
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                name = known_face_names[best_match_index]
                
                top, right, bottom, left = face_locations[0]
                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                    
                image_location.image(frame[:, :, ::-1])
                image_text.text(f"predicted name: {name}")
                time_text.text(f"time(sec): {int(i/fps)}")
                
            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()
        
        # clear outputs
        image_location.empty()
        time_text.empty()
        image_text.empty()
        
        
# def add_vedio(vedio_path):
    
        
        
