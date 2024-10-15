import os
import customtkinter as ctk
import tkinter as tk
import openpyxl
import pages.face_recognition_page as f_rec

class ChooseCourseFaceRecognition:
    
    def choose_course(window, frame, selection, file_paths):
        for item in selection:
            selection = item
        studentID, studentName = ChooseCourseFaceRecognition.getStudentIDandName(file_paths[selection])
        frame.destroy()
        f_rec.FaceRecognition(window, file_paths[selection], studentID, studentName)
        
    def getStudentIDandName(file_path):
        studentID = []
        studentName = []
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        loadToList = list(sheet.values)
        list_of_data = []
        for row in loadToList:
            list_of_data.append(list(row))
        for row in list_of_data[3:]:
            studentID.append(row[0])
            studentName.append(row[1])
        return studentID , studentName
        
    def get_file_name():
        file_path = []
        for root, dirs, filenames in os.walk("version.0.5/course_data"):
            for filename in filenames:
                if filename.endswith(".xlsx"):
                    file_path.append(os.path.join(root, filename))
        return file_path
                    
    def __init__(self, window):
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        master_frame.grid_rowconfigure(0, weight=1)
        master_frame.grid_columnconfigure(0, weight=1)
        
        file_path = ChooseCourseFaceRecognition.get_file_name()
        
        # Create Listbox Frame
        listbox_frame = ctk.CTkFrame(master=master_frame)
        listbox_frame.pack(pady=50)
        
        # Create Label
        label_name = ctk.CTkLabel(master=listbox_frame, text="Course List",
                             font=("Leelawadee", 25))
        label_name.pack()
        
        # Create Listbox
        listbox = tk.Listbox(master=listbox_frame, width=50, height=10, font=("Leelawadee", 15))
        listbox.pack(padx=20, pady=20)
        for file in file_path:
            listbox.insert('end', str(file)[31:-5])
            
        # Create Choose Button
        choose_button = ctk.CTkButton(master=master_frame, fg_color='green',
                                       width=200, height=50, text="Choose Course",
                                       font=("Leelawadee", 25),
                                       command=lambda: ChooseCourseFaceRecognition.choose_course(window, master_frame, listbox.curselection(), file_path))
        choose_button.pack(pady=30)