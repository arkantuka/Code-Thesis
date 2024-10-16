import os
import customtkinter as ctk
import tkinter as tk
import openpyxl
import pages.face_recognition_page as f_rec
import pages.menu_course_data_page as menu_crs

class ChooseCourseFaceRecognition:
    
    def choose_course(window, frame, selection, file_paths, exam_time):
        for item in selection:
            new_selection = item
        studentID, studentName, time = ChooseCourseFaceRecognition.getStudentIDandName(file_paths[new_selection], exam_time)
        frame.destroy()
        f_rec.FaceRecognition(window, file_paths[new_selection], studentID, studentName, time)
        
    def getStudentIDandName(file_path, exam_time):
        studentID = []
        studentName = []
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        loadToList = list(sheet.values)
        list_of_data = []
        for row in loadToList:
            list_of_data.append(list(row))
        dict_of_data = {list_of_data[0][i]: list_of_data[1][i] for i in range(len(list_of_data[0]))}
        print(dict_of_data)
        for row in list_of_data[3:]:
            studentID.append(row[0])
            studentName.append(row[1])
        if exam_time == '1':
            time = dict_of_data.get('Midterm Start Time')
        elif exam_time == '2':
            time = dict_of_data.get('Final Start Time')
        return studentID , studentName , time
        
    def get_file_name():
        file_path = []
        for root, dirs, filenames in os.walk("version.0.5/course_data"):
            for filename in filenames:
                if filename.endswith(".xlsx"):
                    file_path.append(os.path.join(root, filename))
        return file_path
    
    def back(window, frame):
        frame.destroy()
        menu_crs.CourseMenu(window)
                    
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
            
        # Create Radio Button
        radio_frame = ctk.CTkFrame(master=master_frame)
        radio_frame.pack(pady=20)
        radio_label = ctk.CTkLabel(master=radio_frame, text="Select Exam Time: ", font=("Leelawadee", 20))
        radio_label.grid(row=0, column=0, padx=10, pady=10)
        radio_var = ctk.StringVar(master=radio_frame, value="1")
        radio_1 = ctk.CTkRadioButton(master=radio_frame, text="Midterm", font=("Leelawadee", 20), variable=radio_var, value="1")
        radio_1.grid(row=0, column=1, padx=10)
        radio_2 = ctk.CTkRadioButton(master=radio_frame, text="Final", font=("Leelawadee", 20), variable=radio_var, value="2")
        radio_2.grid(row=0, column=2, padx=10)
            
        # Create Choose Button
        choose_button = ctk.CTkButton(master=master_frame, fg_color='green',
                                       width=200, height=50, text="Choose Course",
                                       font=("Leelawadee", 25),
                                       command=lambda: ChooseCourseFaceRecognition.choose_course(window, master_frame, listbox.curselection(), file_path, radio_var.get()))
        choose_button.pack(pady=30)
        
        # Create Back Button
        back_button = ctk.CTkButton(master=master_frame, fg_color='red',
                                       width=200, height=50, text="Back",
                                       font=("Leelawadee", 25),
                                       command=lambda: ChooseCourseFaceRecognition.back(window, master_frame))
        back_button.pack(pady=30)