import os
import customtkinter as ctk
import tkinter as tk
import openpyxl
import pages.menu_course_data_page as menu_crs
import pages.time_attendance_page as t_att

class ChooseCourseTimeAttendance:
    
    def choose_course(window, frame, selection, file_paths):
        for item in selection:
            selection = item
        frame.destroy()
        t_att.TimeAttendance(window, file_paths[selection])

    def get_file_name():
        file_path = []
        for root, dirs, filenames in os.walk("version.0.5/time_attendance"):
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
        
        file_path = ChooseCourseTimeAttendance.get_file_name()
        
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
            listbox.insert('end', str(file)[29:-5])
            
        # Create Choose Button
        choose_button = ctk.CTkButton(master=master_frame, fg_color='green',
                                       width=200, height=50, text="Choose Course",
                                       font=("Leelawadee", 25),
                                       command=lambda: ChooseCourseTimeAttendance.choose_course(window, master_frame, listbox.curselection(), file_path))
        choose_button.pack(pady=30)
        
        # Create Back Button
        back_button = ctk.CTkButton(master=master_frame, fg_color='red',
                                       width=200, height=50, text="Back",
                                       font=("Leelawadee", 25),
                                       command=lambda: ChooseCourseTimeAttendance.back(window, master_frame))
        back_button.pack(pady=30)