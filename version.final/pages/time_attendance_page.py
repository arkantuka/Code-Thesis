import customtkinter as ctk
import openpyxl
import pages.choose_course_attendance as choose_crs_att
from tkinter import ttk

font = "THSarabunNew"
button_font_size = 30
header_font_size = 50

class TimeAttendance:
    
    # Back Button Function
    def back(window, frame):
        frame.destroy()
        choose_crs_att.ChooseCourseTimeAttendance(window)
        
    def sort_column(table, col, reverse):
        data = [(table.set(item, col),item) for item in table.get_children('')]
        data.sort(reverse=reverse)
        for index, (val, item) in enumerate(data):
            table.move(item, '', index)
        table.heading(col, command=lambda: TimeAttendance.sort_column(table, col, not reverse))

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
        style.configure("Treeview.Heading", font=(font, 20, "bold"))
        style.configure("Treeview", font=(font, 20), rowheight=20)

        # Insert Table
        table['columns'] = list_of_data[0]
        table.column('#0', width=0, stretch='YES')
        table.column('Student ID', anchor='center', width=130)
        table.column('Name', width=260)
        table.column('Date', anchor='center', width=100)
        table.column('Time', anchor='center', width=100)
        for header in list_of_data[0]:
            table.heading(str(header), text=str(header), command=lambda col=header: TimeAttendance.sort_column(table, col, False))
        for value in list_of_data[1:]:
            table.insert("", "end", values=value)        
    
        
    def __init__(self, window, file_path):
        
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        
        # Create Menu Label
        time_attendance_label = ctk.CTkLabel(master=master_frame,
                                  text="Time Attendance",
                                  font=(font, header_font_size, "bold"),
                                  padx=20, pady=10)
        time_attendance_label.pack(pady=(20, 0))
        
        TimeAttendance.createMainFrame(master_frame, file_path)
        
        # Exit Button
        exit_button = ctk.CTkButton(master=master_frame, fg_color='red',
                                    width=200, height=50,
                                    text="Exit",
                                    font=(font, button_font_size, "bold"),
                                    command=window.destroy)
        exit_button.pack(side="bottom", pady=30)
        
        # Back Button
        back_button = ctk.CTkButton(master=master_frame, fg_color='green',
                                    width=200, height=50,
                                    text="Back",
                                    font=(font, button_font_size, "bold"),
                                    command=lambda: TimeAttendance.back(window, master_frame))
        back_button.pack(side="bottom", pady=30)