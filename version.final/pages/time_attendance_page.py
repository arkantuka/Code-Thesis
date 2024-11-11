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
        style.configure("Treeview", font=(font, 20), rowheight=25)

        # Insert Table
        table['columns'] = list_of_data[2][:4]
        table.column('#0', width=0, stretch='YES')
        table.column('Student ID', anchor='center', width=130)
        table.column('Name', width=260)
        table.column('Date', anchor='center', width=100)
        table.column('Time', anchor='center', width=100)
        count_present = 0
        count_absent = 0
        count_all_student = 0
        for header in list_of_data[2][:4]:
            table.heading(str(header), text=str(header), command=lambda col=header: TimeAttendance.sort_column(table, col, False))
        for value in list_of_data[3:]:
            table.insert("", "end", values=value)
            count_all_student += 1
            if value[2] == None:
                count_absent += 1
            else :
                count_present += 1
        
        # Create Label
        amount_frame = ctk.CTkFrame(master=table_frame)
        amount_frame.pack(pady=(15, 2))
        all_student_label = ctk.CTkLabel(master=amount_frame, text="All Student: "+str(count_all_student), font=(font, 22))
        all_student_label.pack(padx=(10, 10), side="left")
        present_label = ctk.CTkLabel(master=amount_frame, text="Present: "+str(count_present), font=(font, 22))
        present_label.pack(padx=(10, 10), side="left")
        absent_label = ctk.CTkLabel(master=amount_frame, text="Absent: "+str(count_absent), font=(font, 22))
        absent_label.pack(padx=(10, 10), side="right")
    
        
    def __init__(self, window, file_path):
        
        course_name = str(file_path[30:-5])
        
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        
        # Create Menu Label
        time_attendance_label = ctk.CTkLabel(master=master_frame,
                                  text=course_name,
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