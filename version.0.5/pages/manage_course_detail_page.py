import customtkinter as ctk
import pages.menu_course_data_page as menu_crs
from PIL import Image

class CourseDetail:
    # Back Button Function
    def back(window, frame):
        frame.destroy()
        menu_crs.CourseMenu(window)
        
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

    #Create Icon
    def createIcon(window, image_path, command):
        image_icon = ctk.CTkImage(light_image=Image.open(image_path),
                                  dark_image=Image.open(image_path),
                                  size=(200, 200))
        image_button = ctk.CTkButton(master=window, image=image_icon, 
                                     text="", command=command,
                                     hover_color=None)
        image_button.grid(row=0, column=0, padx=20, pady=20)
        return image_button    
    
    def __init__(self, window):
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        
         # Menu Label
        menu_label = ctk.CTkLabel(master=master_frame,
                                  text="Course Details",
                                  font=("Leelawadee", 35, "bold"),
                                  padx=100, pady=10)
        menu_label.pack(pady=(50, 0))
        
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
                                    command=lambda: CourseDetail.back(window, master_frame))
        back_button.pack(side="bottom", pady=30)