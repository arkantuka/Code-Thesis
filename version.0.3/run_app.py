import main_page as mp
import datetime as dt
import customtkinter as ctk

class FaceRecognitionApp:
    #Go to main page when submit button is clicked
    def button_click(window, course_id):
        window.destroy()
        mp.MainPage(course_id)

    def runMain(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        window = ctk.CTk()
        width_window = window.winfo_screenwidth()-10
        height_window = window.winfo_screenheight()-80
        window.geometry("{0}x{1}+0+0".format(width_window, height_window))
        window.title('Test Application GUI Window Face Recognition')
        window.grid_columnconfigure(1, weight=1)
        window.grid_rowconfigure([0,1,2,3,4], weight=1)

        #Enter course label
        enter_course_label = ctk.CTkLabel(master=window, 
                                    text="Enter Your Course ID", 
                                    font=("Leelawadee", 50) ,
                                    corner_radius=8)
        enter_course_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        enter_course_label.grid(row=0, column=1, padx=20, pady=10)

        #Course ID entry
        courseID_entry = ctk.CTkEntry(master=window, 
                                      width=500,
                                      height=80,
                                      corner_radius=10,
                                      placeholder_text="Course ID",
                                      font=("Leelawadee", 30))
        courseID_entry.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        courseID_entry.bind("<Return>", lambda event: FaceRecognitionApp.button_click(window, courseID_entry.get()))
        courseID_entry.grid(row=1, column=1, padx=20, pady=10)
        
        #Radio buttons
        radio_frame = ctk.CTkFrame(master=window,
                                   corner_radius=10)
        radio_frame.grid(row=2, column=1, padx=20, pady=10)
        radio_label = ctk.CTkLabel(master=radio_frame, 
                                   text="Select Term :", 
                                   font=("Leelawadee", 25), 
                                   anchor="w")
        radio_label.grid(row=0, column=0, padx=20, pady=10)
        def setRadioResults():
            term = radio_var.get()
            print(term)
            
        radio_var = ctk.StringVar(master=radio_frame, value="1")  # Create a variable for strings, and initialize the variable
        radio_button_1 = ctk.CTkRadioButton(master=radio_frame, text="First Term", font=("Leelawadee", 20), 
                       variable=radio_var, value="1", command=setRadioResults)
        radio_button_1.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        radio_button_2 = ctk.CTkRadioButton(master=radio_frame, text="Second Term", font=("Leelawadee", 20), 
                       variable=radio_var, value="2", command=setRadioResults)
        radio_button_2.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        radio_button_3 = ctk.CTkRadioButton(master=radio_frame, text="Summer Term", font=("Leelawadee", 20), 
                       variable=radio_var, value="3", command=setRadioResults)
        radio_button_3.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        
        
        def chooseDropdown(e):
            year_selected = combobox.get()
            print(year_selected)
        #Dropdown for year
        combobox_frame = ctk.CTkFrame(master=window,
                                   corner_radius=10)
        combobox_frame.grid(row=3, column=1, padx=20, pady=10)
        combobox_label = ctk.CTkLabel(master=combobox_frame, 
                                      text="Select Year :", 
                                      font=("Leelawadee", 25), 
                                      anchor="w")
        combobox_label.grid(row=0, column=0, padx=20, pady=10)
        curretYear = dt.datetime.now().year
        combobox_var = ctk.StringVar(master=combobox_frame, value=str(curretYear))
        combobox = ctk.CTkComboBox(master=combobox_frame, 
                                values=[str(curretYear-5),
                                     str(curretYear-4), 
                                     str(curretYear-3), 
                                     str(curretYear-2),  
                                     str(curretYear-1), 
                                     str(curretYear), 
                                     str(curretYear+1), 
                                     str(curretYear+2),
                                     str(curretYear+3), 
                                     str(curretYear+4), 
                                     str(curretYear+5)],
                                     font=("Leelawadee", 20),
                                command=chooseDropdown,
                                variable=combobox_var)
        combobox.grid(row=1, column=0, padx=20, pady=10)
        
        #Submit Button 
        id_submit_button = ctk.CTkButton(master=window, fg_color='green',
                                         width=200,
                                         height=60,
                                        text="Submit",
                                        font=("Leelawadee", 35, "bold"), 
                                        corner_radius=20,
                                        command=lambda: FaceRecognitionApp.button_click(window, courseID_entry.get()))
        id_submit_button.grid(row=4, column=1, padx=20, pady=10)
        window.mainloop()
    
if __name__ == "__main__":
    app = FaceRecognitionApp()
    app.runMain()