import customtkinter as ctk
import openpyxl
import pages.choose_course_attendance as choose_crs_att
from tkinter import ttk

class TimeAttendance:
    # Back Button Function
    def back(window, frame):
        frame.destroy()
        choose_crs_att.ChooseCourseTimeAttendance(window)
        
    # Create Button
    def createButton(frame, label_name, command):
        button = ctk.CTkButton(master=frame, fg_color="gray",
                           text=label_name, height=50, width=200,
                           font=("Leelawadee", 25),
                           command=command)
        return button
    
    # Create Main Frame
    def createMainFrame(master_frame, file_path):
        
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        loadToList = list(sheet.values)
        list_of_data = []
        for row in loadToList:
            list_of_data.append(list(row))
        
        
        # Create Table Frame
        table_frame = ctk.CTkFrame(master=master_frame)
        table_frame.pack(fill="both", expand=True)
        
        # Create Scrollbar and Table
        tree_scrollbar = ttk.Scrollbar(table_frame, orient="vertical")
        tree_scrollbar.pack(side="right", fill="y")
        table = ttk.Treeview(table_frame, height=20, show="headings",
                                     yscrollcommand=tree_scrollbar.set)
        table.pack(fill="both", expand=True)
        tree_scrollbar.config(command=table.yview)
        
        # Configure Table
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Leelawadee", 12, "bold"))
        style.configure("Treeview", font=("Leelawadee", 15), rowheight=20)

        # Insert Table
        table['columns'] = list_of_data[0]
        table.column('#0', width=0, stretch='YES')
        table.column('Student ID', anchor='center', width=130)
        table.column('Name', width=260)
        table.column('Date', anchor='center', width=100)
        table.column('Time', anchor='center', width=100)
        for header in list_of_data[0]:
            table.heading(str(header), text=str(header))
        for value in list_of_data[1:]:
            table.insert("", "end", values=value)        
    
        
    def __init__(self, window, file_path):
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        
        # Create Menu Label
        time_attendance_label = ctk.CTkLabel(master=master_frame,
                                  text="Time Attendance",
                                  font=("Leelawadee", 35, "bold"),
                                  padx=20, pady=10)
        time_attendance_label.pack(pady=(20, 0))
        
        TimeAttendance.createMainFrame(master_frame, file_path)
        
        # Exit Button
        exit_button = ctk.CTkButton(master=master_frame, fg_color='red',
                                    width=200, height=50,
                                    text="Exit",
                                    font=("Leelawadee", 25),
                                    command=window.destroy)
        exit_button.pack(side="bottom", pady=30)
        
        # Back Button
        back_button = ctk.CTkButton(master=master_frame, fg_color='green',
                                    width=200, height=50,
                                    text="Back",
                                    font=("Leelawadee", 25),
                                    command=lambda: TimeAttendance.back(window, master_frame))
        back_button.pack(side="bottom", pady=30)