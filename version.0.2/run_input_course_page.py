import tkinter as tk
import main_page as mp
import datetime as dt
from tkinter import ttk

class FaceRecognitionApp:
    #Go to main page when submit button is clicked
    def button_click(window, course_id):
        window.destroy()
        mp.MainPage(course_id)

    def runMain(self):
        window = tk.Tk()
        window.resizable(False, False)
        window.title('Test Application GUI Window Face Recognition')
        window.eval('tk::PlaceWindow . center')

        #Enter course label
        enter_course_label = tk.Label(window, 
                                    text="Enter Your Course ID", 
                                    font=("Leelawadee", 50) ,
                                    padx=100, pady=10)
        enter_course_label.pack()

        #Course ID entry
        courseID_entry = tk.Entry(window, font=("Leelawadee", 30))
        courseID_entry.pack()
        
        #Radio buttons
        radio_frame = tk.Frame(window)
        radio_frame.pack(pady=10)
        tk.Label(radio_frame, text="Select Term :").pack(anchor='w')
        def setRadioResults():
            term = var1.get()
            print(term)
            
        var1 = tk.StringVar(radio_frame, "1")  # Create a variable for strings, and initialize the variable
        tk.Radiobutton(radio_frame, text="First Term", font=("Leelawadee", 12), 
                       variable=var1, value="1", command=setRadioResults).pack(anchor='w')
        tk.Radiobutton(radio_frame, text="Second Term", font=("Leelawadee", 12), 
                       variable=var1, value="2", command=setRadioResults).pack(anchor='w')
        tk.Radiobutton(radio_frame, text="Summer Term", font=("Leelawadee", 12), 
                       variable=var1, value="3", command=setRadioResults).pack(anchor='w')
        
        def chooseDropdown(e):
            year_selected = combo.get()
            print(year_selected)
        #Dropdown for year
        tk.Label(radio_frame, text="Select Year :").pack(anchor='w')
        curretYear = dt.datetime.now().year
        combo = ttk.Combobox(radio_frame, 
                             values=[curretYear-5,
                                     curretYear-4, 
                                     curretYear-3, 
                                     curretYear-2,  
                                     curretYear-1, 
                                     curretYear, 
                                     curretYear+1, 
                                     curretYear+2,
                                     curretYear+3, 
                                     curretYear+4, 
                                     curretYear+5, ])
        combo.current(5)
        combo.bind("<<ComboboxSelected>>", chooseDropdown)
        combo.pack(anchor='w')
        
        #Submit Button 
        id_submit_button = tk.Button(window, background='black', foreground='green',
                                    text="Submit",
                                    font=("Leelawadee", 30, "bold"), 
                                    command=lambda: FaceRecognitionApp.button_click(window, courseID_entry.get()))
        id_submit_button.pack(padx=20, pady=20)

        window.mainloop()
    
if __name__ == "__main__":
    app = FaceRecognitionApp()
    app.runMain()