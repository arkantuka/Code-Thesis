import customtkinter as ctk
import pages.menu_course_data_page as menu_crs
import pages.add_course_page as add_crs
import pages.manage_course_detail_page as mng_crs
import pages.train_model_page as trn_mdl
from tkinter import filedialog

class ManageCourseMenu:
    # Back Button Function
    def back(window, frame):
        frame.destroy()
        menu_crs.CourseMenu(window)
    
    # Train Model Function
    def trainModel(window, frame):
        frame.destroy()
        trn_mdl.TrainModel(window)
        
    # Add New Course Function 
    def newCourse(window, frame):
        frame.destroy()
        add_crs.AddCoursePage(window)
        
    # Create Button Function
    def createButton(frame, label_name, command):
        button = ctk.CTkButton(master=frame, fg_color="gray",
                           text=label_name, height=50, width=250,
                           font=("Leelawadee", 25),
                           command=command)
        return button
    
    # File Dialog for file path
    def fileDialog(initial_directory):
        file_path = filedialog.askopenfilename(initialdir=initial_directory,
                                        title="Select A File",
                                        filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
        return file_path
    
    def openExcelData(window, frame):
        try:
            file_path = ManageCourseMenu.fileDialog("E:/Code-Thesis/version.0.5/course_data/")
            if file_path:
                frame.destroy()
                mng_crs.CourseDetail(window, file_path)
        except:
            pass
    
    def __init__(self, window):
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        
        # Create Course Menu Label
        course_menu_label = ctk.CTkLabel(master=master_frame,
                              text="Manage Course Menu",
                              font=("Leelawadee", 35, "bold"),
                              padx=20, pady=10)
        course_menu_label.pack(pady=(20, 0))
        
        # Create Button Frame
        button_frame = ctk.CTkFrame(master=master_frame)
        button_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
        # Create New Course Button
        new_course_button = ManageCourseMenu.createButton(button_frame, 'Add New Course',
                                                    lambda: ManageCourseMenu.newCourse(window, master_frame))
        new_course_button.grid(row=0, column=0, padx=20, pady=10)
        
        # Create Open File Button
        edit_course_data = ManageCourseMenu.createButton(button_frame, 'Edit Course Data',
                                                    lambda: ManageCourseMenu.openExcelData(window, master_frame))
        edit_course_data.grid(row=1, column=0, padx=20, pady=10)
        
        # Create Train Model Button
        train_model_button = ManageCourseMenu.createButton(button_frame, 'Train Model',
                                                    lambda: ManageCourseMenu.trainModel(window, master_frame))
        train_model_button.grid(row=2, column=0, padx=20, pady=10)
        
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
                                command=lambda: ManageCourseMenu.back(window, master_frame))
        back_button.pack(side="bottom", pady=30)