import customtkinter as ctk
import pages.main_page as mp

class CourseDataPage:
    # Back Button Function
    def back(window, frame):
        frame.destroy()
        mp.MainPage(window)
        
    def __init__(self, window):

        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        
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
                                    command=lambda: CourseDataPage.back(window, master_frame))
        back_button.pack(side="bottom", pady=30)