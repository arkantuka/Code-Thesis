import customtkinter as ctk
import pages.main_page as mp
import pages.show_student_data_page as ssdp
import pandas as pd
import openpyxl
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox

class StudentDataPage:
    
    # File Dialog for file path
    def fileDialog(initial_directory):
        file_path = filedialog.askopenfilename(initialdir=initial_directory,
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
        return file_path
    
    # Load Excel Data and save to new sheet
    def loadExcelData():
        file_path = StudentDataPage.fileDialog("/")
        xl = pd.read_excel(file_path, sheet_name=None)
        sheets = xl.keys()
        for sheet in sheets:
            xl[sheet].to_excel(f"version.0.5/students_data/{sheet}.xlsx")
        # Show Message
        CTkMessagebox(title="Information", 
                      message=f"File {file_path} loaded successfully.", 
                      icon="check", option_1="OK", option_2=None)
    
    # Open Excel Data and open new Page
    def openExcelData(window, frame):
        file_path = StudentDataPage.fileDialog("version.0.5/students_data/")
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        list_values = list(sheet.values)
        frame.destroy()
        ssdp.ShowStudentDataPage(window, list_values)
        
    # Back Button Function
    def back(window, frame):
        frame.destroy()
        mp.MainPage(window)
        
    # Create Button
    def createButton(frame, label_name, command):
        button = ctk.CTkButton(master=frame, fg_color="gray",
                           text=label_name, height=50, width=200,
                           font=("Leelawadee", 25),
                           command=command)
        return button
        
    def __init__(self, window):
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        
        # Create Menu Label
        student_data_label = ctk.CTkLabel(master=master_frame,
                                  text="Students Data",
                                  font=("Leelawadee", 35, "bold"),
                                  padx=20, pady=10)
        student_data_label.pack(pady=(20, 0))
       
        # Create Buttons Frame
        buttons_frame = ctk.CTkFrame(master=master_frame)
        buttons_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
        # Create Open Data Button
        open_data_button = StudentDataPage.createButton(buttons_frame, 'Open Data',
                                                        lambda: StudentDataPage.openExcelData(window, master_frame))
        open_data_button.grid(row=0, column=1, padx=20, pady=10)
        
        # Create Browse and Load File Button
        browse_n_load_data_button = StudentDataPage.createButton(buttons_frame, 'Browse New File', 
                                                        lambda: StudentDataPage.loadExcelData())
        browse_n_load_data_button.grid(row=1, column=1, padx=20, pady=10)
        
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
                                    command=lambda: StudentDataPage.back(window, master_frame))
        back_button.pack(side="bottom", pady=30)