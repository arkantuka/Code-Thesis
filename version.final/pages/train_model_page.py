import os
import tkinter as tk
import customtkinter as ctk
import cv2
import openpyxl
import numpy as np
import pages.manage_course_menu as mng_crs_menu
from PIL import Image

font = "THSarabunNew"
button_font_size = 30
header_font_size = 50

class TrainModel:
    def getImagesData(paths):
        faces = []
        ids = []
        all_imgs_path = []
        for id_path in paths:
            for image_path in os.listdir(id_path):
                all_imgs_path.append(os.path.join(id_path, image_path))
        for image_path in all_imgs_path:
            face_image = Image.open(image_path).convert('L')
            face_np = np.array(face_image, 'uint8')
            id = os.path.split(image_path)[1].split('-')[0]
            id = int(id)
            faces.append(face_np)
            ids.append(id)
            cv2.imshow("training", face_np)
            cv2.waitKey(1)        
        cv2.destroyAllWindows()
        print(len(ids))
        return ids, faces
        
    # Back Button Function
    def back(window, frame):
        frame.destroy()
        mng_crs_menu.ManageCourseMenu(window)
        
    def get_file_name():
        file_name = []
        file_path = []
        for root, dirs, filenames in os.walk("version.final/course_data"):
            for filename in filenames:
                if filename.endswith(".xlsx"):
                    file_name.append(filename[:-5])
                    file_path.append(os.path.join(root, filename))
        return file_name, file_path
    
    def getStudentID(file_path):
        studentID = []
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        loadToList = list(sheet.values)
        list_of_data = []
        for row in loadToList:
            list_of_data.append(list(row))
        for row in list_of_data[3:]:
            studentID.append(str(row[0]))
        return studentID
    
    def getImagePaths(ids):
        paths = []
        for id in ids:
            for root, dirs, filenames in os.walk("version.final/images"):
                for dir in dirs:
                    if id == dir:
                        paths.append(os.path.join(root, dir))
        return paths
        
    def train_model(window, selection, file_paths):
        for item in selection:
            selection = item
        studentIDs = []
        studentIDs = TrainModel.getStudentID(file_paths[selection])
        studentIDs_paths = TrainModel.getImagePaths(studentIDs)
        
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        save_path = 'version.final/training_models/'
        
        coures_name = str(file_paths[selection])[33:-5]
        IDs, face_data = TrainModel.getImagesData(studentIDs_paths)
        face_recognizer.train(face_data, np.array(IDs))
        face_recognizer.write(save_path+coures_name+".yml")
        tk.messagebox.showinfo("Complete", "Training Complete")
        
    def __init__(self, window):
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        file_name, file_path = TrainModel.get_file_name()        
        # Create Label
        label = ctk.CTkLabel(master=master_frame, text="Train Model",
                             font=(font, header_font_size, "bold"),)
        label.pack(pady=30)
        
        # Create Listbox Frame
        listbox_frame = ctk.CTkFrame(master=master_frame)
        listbox_frame.pack(pady=50)  
        
        # Create Label
        label_name = ctk.CTkLabel(master=listbox_frame, text="Course List",
                             font=(font, header_font_size, "bold"))
        label_name.pack()      
        
        # Create Listbox
        listbox = tk.Listbox(master=listbox_frame, width=50, height=10, font=(font, 20))
        listbox.pack(padx=20, pady=20)
        for file in file_name:
            listbox.insert('end', file)

        # Create Train Model Button
        train_model_button = ctk.CTkButton(master=master_frame, fg_color='green',
                                           width=200, height=50,
                                           text="Start Train Model",
                                           font=(font, button_font_size, "bold"),
                                           command=lambda: TrainModel.train_model(window, listbox.curselection(), file_path))
        train_model_button.pack(pady=30)
        
        # Exit Button
        exit_button = ctk.CTkButton(master=master_frame, fg_color='red',
                                    width=200, height=50,
                                    text="Exit",
                                    font=(font, button_font_size, "bold"),
                                    command=window.destroy)
        exit_button.pack(side="bottom", pady=20)
        
        # Back Button
        back_button = ctk.CTkButton(master=master_frame, fg_color='gray',
                                    width=200, height=50,
                                    text="Back",
                                    font=(font, button_font_size, "bold"),
                                    command=lambda: TrainModel.back(window, master_frame))
        back_button.pack(side="bottom", pady=30)
        