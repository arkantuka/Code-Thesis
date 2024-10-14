import customtkinter as ctk
import pages.menu_course_data_page as menu_crs

class TimeAttendence:
    # Back Button Function
    def back(window, frame):
        frame.destroy()
        menu_crs.CourseMenu(window)
        
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
        time_attendance_label = ctk.CTkLabel(master=master_frame,
                                  text="Time Attendence",
                                  font=("Leelawadee", 35, "bold"),
                                  padx=20, pady=10)
        time_attendance_label.pack(pady=(20, 0))
        
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
                                    command=lambda: TimeAttendence.back(window, master_frame))
        back_button.pack(side="bottom", pady=30)