import customtkinter as ctk
import pages.menu_student_data_page as menu_std
import pages.menu_course_data_page as menu_crs
from PIL import Image

class MainPage:
    
    # Create Frame
    def createFrame(window, row, col):
        frame = ctk.CTkFrame(master=window)
        frame.grid(row=row, column=col, padx=20, pady=10)
        return frame
    
    # Create Button
    def createButton(frame, label_name, command):
        button = ctk.CTkButton(master=frame, fg_color="gray",
                           text=label_name, height=60, width=220,
                           font=("Leelawadee", 25),
                           command=command)
        return button
    
    # Create Icon
    def createIcon(window, image_path, command):
        image_icon = ctk.CTkImage(light_image=Image.open(image_path),
                                  dark_image=Image.open(image_path),
                                  size=(200, 200))
        image_button = ctk.CTkButton(master=window, image=image_icon, 
                                     text="", command=command,
                                     hover_color=None)
        image_button.grid(row=0, column=0, padx=20, pady=20)
        return image_button
        
    # Click Button function
    def button_click(window, frame, order):
        frame.destroy()
        if order == 1:
            menu_std.StudentMenu(window)
        elif order == 2:
            menu_crs.CourseMenu(window)
        else:
            print("Error")
            
    # Toggle Appearance Mode
    def toggle_mode(bool):
        if bool==True:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
    
    def __init__(self, window):
        
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        
        # Menu Label
        menu_label = ctk.CTkLabel(master=master_frame,
                                  text="Menu",
                                  font=("Leelawadee", 35, "bold"),
                                  padx=100, pady=10)
        menu_label.pack(pady=(50, 0))
        
        # Main Frame
        menu_frame = ctk.CTkFrame(master=master_frame)
        menu_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
        # Student Data Button
        student_data_frame = MainPage.createFrame(menu_frame, 0, 0)
        MainPage.createIcon(student_data_frame, 
                                      'version.0.5/icons/student-data-icon.jpg',
                                      lambda: MainPage.button_click(window, master_frame, 1))
        student_data_button = MainPage.createButton(student_data_frame, 
                                        "Student Data", 
                                        lambda: MainPage.button_click(window, master_frame, 1))
        student_data_button.grid(row=1, column=0, padx=20, pady=10)
        
        # Course Data Button
        course_data_frame = MainPage.createFrame(menu_frame, 0, 1)
        MainPage.createIcon(course_data_frame, 
                                      'version.0.5/icons/course-data-icon.png',
                                      lambda: MainPage.button_click(window, master_frame, 2))
        course_data_button = MainPage.createButton(course_data_frame, 
                                        "Course Data", 
                                        lambda: MainPage.button_click(window, master_frame, 2))
        course_data_button.grid(row=1, column=0, padx=20, pady=10)
        
        
        
        # Mode Switch Button
        switch_var = ctk.BooleanVar(value=True)
        mode_switch = ctk.CTkSwitch(master=master_frame, text="Dark Mode",
                                    font=("Leelawadee", 25),
                                    variable=switch_var,
                                    switch_height=30, switch_width=60,
                                    onvalue=True, offvalue=False,
                                      command=lambda: MainPage.toggle_mode(switch_var.get()))
        mode_switch.pack(side="bottom", pady=30)
        
        # Exit Button
        exit_button = ctk.CTkButton(master=master_frame, fg_color='red',
                                    width=200, height=50,
                                    text="Exit",
                                    font=("Leelawadee", 25),
                                    command=window.destroy)
        exit_button.pack(side="bottom", pady=30)