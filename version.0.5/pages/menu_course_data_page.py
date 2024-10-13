import customtkinter as ctk
import pages.main_page as mp
# import pages.course_data_page as crs_page
# import pages.time_attendence_page as att_page
from PIL import Image

class CourseMenu:
    # Back Button Function
    def back(window, frame):
        frame.destroy()
        mp.MainPage(window)
        
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
    
    #Click Button function
    def button_click(window, frame, order):
        frame.destroy()
        # if order == 1:
        #     crs_page.CourseDataPage(window)
        # # elif order == 2:
        # #     face_rec_page.FaceRecognitionPage(window)
        # elif order == 3:
        #     att_page.AttendencePage(window)
        # else:
        #     print("Error")
        
    


    def __init__(self, window):
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        
        # Menu Label
        menu_label = ctk.CTkLabel(master=master_frame,
                                  text="Course Menu",
                                  font=("Leelawadee", 35, "bold"),
                                  padx=100, pady=10)
        menu_label.pack(pady=(50, 0))
        
        # Main Frame
        menu_frame = ctk.CTkFrame(master=master_frame)
        menu_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)


        # Course Data Button
        course_data_frame = CourseMenu.createFrame(menu_frame, 0, 0)
        CourseMenu.createIcon(course_data_frame, 
                                      'version.0.5/icons/course-data-icon.png',
                                      lambda: CourseMenu.button_click(window, master_frame, 1))
        student_data_button = CourseMenu.createButton(course_data_frame, 
                                        "Course Data", 
                                        lambda: CourseMenu.button_click(window, master_frame, 1))
        student_data_button.grid(row=1, column=0, padx=20, pady=10)

        # Face Recognition Button
        face_Recognition_frame = CourseMenu.createFrame(menu_frame, 0, 1)
        CourseMenu.createIcon(face_Recognition_frame, 
                                      'version.0.5/icons/facerec.jpg',
                                      lambda: CourseMenu.button_click(window, master_frame, 1))
        face_Recognition_frame = CourseMenu.createButton(face_Recognition_frame, 
                                        "Face Recognition", 
                                        lambda: CourseMenu.button_click(window, master_frame, 1))
        face_Recognition_frame.grid(row=1, column=0, padx=20, pady=10)

        # Time Attempt Button
        time_attempt_frame = CourseMenu.createFrame(menu_frame, 0, 2)
        CourseMenu.createIcon(time_attempt_frame, 
                                      'version.0.5/icons/time2.png',
                                      lambda: CourseMenu.button_click(window, master_frame, 1))
        time_attempt_frame = CourseMenu.createButton(time_attempt_frame, 
                                        "Time Attempt", 
                                        lambda: CourseMenu.button_click(window, master_frame, 1))
        time_attempt_frame.grid(row=1, column=0, padx=20, pady=10)


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
                                    command=lambda: CourseMenu.back(window, master_frame))
        back_button.pack(side="bottom", pady=30)