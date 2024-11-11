import customtkinter as ctk
import pages.manage_student_data_menu_page as mng_std_menu
import pages.manage_course_menu as mng_crs_menu
import pages.choose_course_face_recognition as choose_f_rec
import pages.choose_course_attendance as choose_crs_att
from PIL import Image

font = "THSarabunNew"
button_font_size = 30
header_font_size = 50

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
                           font=(font, button_font_size, "bold"),
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
            mng_std_menu.StudentMenu(window)
        elif order == 2:
            mng_crs_menu.ManageCourseMenu(window)
        elif order == 3:
            choose_f_rec.ChooseCourseFaceRecognition(window)
        elif order == 4:
            choose_crs_att.ChooseCourseTimeAttendance(window)
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
                                  text="Face Recognition For Attendance",
                                  font=(font, header_font_size, "bold"),
                                  padx=100, pady=10)
        menu_label.pack(pady=(50, 0))
        
        # Main Frame
        menu_frame = ctk.CTkFrame(master=master_frame)
        menu_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
        # Student Data Button
        student_data_frame = MainPage.createFrame(menu_frame, 0, 0)
        MainPage.createIcon(student_data_frame, 
                                      'version.final/icons/student-data-icon.jpg',
                                      lambda: MainPage.button_click(window, master_frame, 1))
        student_data_button = MainPage.createButton(student_data_frame, 
                                        "Manage Student Data", 
                                        lambda: MainPage.button_click(window, master_frame, 1))
        student_data_button.grid(row=1, column=0, padx=20, pady=10)
        
        # Course Detail Button
        manage_course_menu_button_frame = MainPage.createFrame(menu_frame, 0, 1)
        MainPage.createIcon(manage_course_menu_button_frame, 
                                      'version.final/icons/course-data-icon.png',
                                      lambda: MainPage.button_click(window, master_frame, 2))
        manage_course_menu_button = MainPage.createButton(manage_course_menu_button_frame, 
                                        "Manage Course Data", 
                                        lambda: MainPage.button_click(window, master_frame, 2))
        manage_course_menu_button.grid(row=1, column=0, padx=20, pady=10)

        # Face Recognition Button
        face_rec_button_frame = MainPage.createFrame(menu_frame, 0, 2)
        MainPage.createIcon(face_rec_button_frame, 
                                      'version.final/icons/facerec.jpg',
                                      lambda: MainPage.button_click(window, master_frame, 3))
        face_rec_button = MainPage.createButton(face_rec_button_frame, 
                                        "Face Recognition", 
                                        lambda: MainPage.button_click(window, master_frame, 3))
        face_rec_button.grid(row=1, column=0, padx=20, pady=10)

        # Time Attempt Button
        time_atten_button_frame = MainPage.createFrame(menu_frame, 0, 3)
        MainPage.createIcon(time_atten_button_frame, 
                                      'version.final/icons/time2.png',
                                      lambda: MainPage.button_click(window, master_frame, 4))
        time_atten_button = MainPage.createButton(time_atten_button_frame, 
                                        "Time Attendance", 
                                        lambda: MainPage.button_click(window, master_frame, 4))
        time_atten_button.grid(row=1, column=0, padx=20, pady=10)
        
        # Mode Switch Button
        switch_var = ctk.BooleanVar(value=True)
        mode_switch = ctk.CTkSwitch(master=master_frame, text="Dark Mode",
                                    font=(font, button_font_size, "bold"),
                                    variable=switch_var,
                                    switch_height=30, switch_width=60,
                                    onvalue=True, offvalue=False,
                                      command=lambda: MainPage.toggle_mode(switch_var.get()))
        mode_switch.pack(side="bottom", pady=30)
        
        # Exit Button
        exit_button = ctk.CTkButton(master=master_frame, fg_color='red',
                                    width=200, height=50,
                                    text="Exit",
                                    font=(font, button_font_size, "bold"),
                                    command=window.destroy)
        exit_button.pack(side="bottom", pady=30)