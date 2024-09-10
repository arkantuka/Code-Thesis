import cv2
import numpy as np
from PIL import Image
import os
import main_page as mp
import tkinter as tk
from tkinter import messagebox

def getImagesData(path): 
    image_paths = [os.path.join(path,f) for f in os.listdir(path)] 
    faces = []
    ids = []
    for image_path in image_paths:
        face_image = Image.open(image_path).convert('L')
        face_np = np.array(face_image, 'uint8')
        id = os.path.split(image_path)[1].split('.')[0]
        id = int(id)
        faces.append(face_np)
        ids.append(id)
        cv2.imshow("training", face_np)
        cv2.waitKey(1)
    return ids, faces

def runFaceTrain(course_id):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = 'version.0.2/datasets/images/'+str(course_id)+'/'
    save_path = 'version.0.2/datasets/data/train_data/'

    print("====== Training Started ======")
    IDs, face_data = getImagesData(path)
    face_recognizer.train(face_data, np.array(IDs))
    face_recognizer.write(save_path+course_id+"_trainingData.yml")
    print("====== Training Complete ======")
    cv2.destroyAllWindows()
    tk.messagebox.showinfo("Complete", "Training Complete")
    mp.MainPage(course_id)
