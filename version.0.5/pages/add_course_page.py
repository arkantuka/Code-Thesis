import customtkinter as ctk
import datetime as dt
import tkcalendar as cal
import pages.menu_manage_coures as menu_mng_crs
from tktimepicker import AnalogPicker, AnalogThemes

class Clock:
    def updateTime(window, time, label):
        label.configure(text="{}:{}:{}".format(*time))
        window.after(200, lambda: window.destroy()) 
        
    def __init__(self, midterm_start_time_label):
        root = ctk.CTk()
        root.title('Time Picker')
        time_picker = AnalogPicker(root)
        time_picker.pack(expand=True, fill="both")        
        theme = AnalogThemes(time_picker)
        theme.setDracula()
        submit = ctk.CTkButton(root, text="Submit", command=lambda: Clock.updateTime(root, time_picker.time(), midterm_start_time_label))
        submit.pack()
        
        root.mainloop()

class AddCoursePage:
    # Create Back Function
    def back(window, master_frame):
        master_frame.destroy()
        menu_mng_crs.ManageCourseMenu(window)
        
    # Create Label
    def createLabel(frame, label_name):
        label = ctk.CTkLabel(master=frame,
                             text=label_name,
                             font=("Leelawadee", 15),
                             corner_radius=8)
        return label
        
    # Create Entry
    def createEntry(frame, hold_text, width):
        entry = ctk.CTkEntry(master=frame, width=width,
                             font=('Leelawadee', 20), text_color='black',
                             placeholder_text=hold_text,
                             fg_color="#f0f0f0")
        return entry
    
    def addData(courseID, courseName, term, year, midtermDate, finalDate):
        print(courseID, courseName, term, year, midtermDate, finalDate)
    
    def importData():
        try:
            
        except:
            pass
    
    # Create Frame 1
    def createFrame1(window, master_frame):
        # Create Sub master frame 1
        sub_master_frame_1 = ctk.CTkFrame(master=master_frame)
        sub_master_frame_1.grid(row=0, column=0, padx=(10,0), pady=10)
        sub_master_frame_1.grid_columnconfigure(0, weight=1)
        sub_master_frame_1.grid_columnconfigure(1, weight=1)
        
        # Create Add Course Data Frame
        add_data_frame = ctk.CTkFrame(master=sub_master_frame_1)
        add_data_frame.pack(padx=10, pady=10)
        
        # Create Course ID Label and Entry
        courseID_label = AddCoursePage.createLabel(add_data_frame, "Course ID")
        courseID_label.grid(row=0, column=0, padx=5, pady=0)
        courseID_entry = AddCoursePage.createEntry(add_data_frame, "Enter Course ID", 150)
        courseID_entry.grid(row=1, column=0, padx=5, pady=5)
        
        # Create Course Name Label and Entry
        courseName_label = AddCoursePage.createLabel(add_data_frame, "Course Name")
        courseName_label.grid(row=0, column=1, padx=5, pady=0)
        courseName_entry = AddCoursePage.createEntry(add_data_frame, "Enter Course Name", 400)
        courseName_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Create Radio Button Frame
        radio_frame = ctk.CTkFrame(master=add_data_frame)
        radio_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=(10,10))
        radio_label = AddCoursePage.createLabel(radio_frame, "Select Term: ")
        radio_label.grid(row=0, column=0, padx=5, pady=0)
        radio_var = ctk.StringVar(master=radio_frame, value="1")
        radio_button_1 = ctk.CTkRadioButton(master=radio_frame, text="First Term",
                                            font=("Leelawadee", 15), 
                                            variable=radio_var, value="1")
        radio_button_1.grid(row=0, column=1, padx=5, pady=0)
        radio_button_2 = ctk.CTkRadioButton(master=radio_frame, text="Second Term",
                                            font=("Leelawadee", 15),
                                            variable=radio_var, value="2")
        radio_button_2.grid(row=0, column=2, padx=5, pady=0)
        radio_button_3 = ctk.CTkRadioButton(master=radio_frame, text="Summer Term",
                                            font=("Leelawadee", 15),
                                            variable=radio_var, value="3")
        radio_button_3.grid(row=0, column=3, padx=5, pady=0)
        
        # Create Combobox
        combobox_frame = ctk.CTkFrame(master=add_data_frame)
        combobox_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=(10,10))
        combobox_label = AddCoursePage.createLabel(combobox_frame, "Select Year: ")
        combobox_label.grid(row=0, column=0, padx=5, pady=0)
        current_year = (dt.datetime.now().year)+543
        combobox_var = ctk.StringVar(master=combobox_frame, value=str(current_year))
        combobox = ctk.CTkComboBox(master=combobox_frame, 
                                values=[str(current_year-8),str(current_year-7), 
                                     str(current_year-6), str(current_year-5),  
                                     str(current_year-4), str(current_year-3), 
                                     str(current_year-2), str(current_year-1),
                                     str(current_year), str(current_year+1), 
                                     str(current_year+2)],
                                     font=("Leelawadee", 15),variable=combobox_var)
        combobox.grid(row=0, column=1, padx=5, pady=0)
        
        # Create Date Time Picker
        date_time_picker_frame = ctk.CTkFrame(master=add_data_frame)
        date_time_picker_frame.grid(row=4, column=0, padx=5, pady=(10,10), columnspan=2)
        
        date_frame = ctk.CTkFrame(master=date_time_picker_frame)
        date_frame.grid(row=0, column=0, columnspan=2)
        midterm_date_frame = ctk.CTkFrame(master=date_frame)
        midterm_date_frame.grid(row=0, column=0)
        midterm_date_picker_label = AddCoursePage.createLabel(midterm_date_frame, "Midterm Exam Date: ")
        midterm_date_picker_label.grid(row=0, column=0)
        midterm_date_picker = cal.DateEntry(midterm_date_frame, date_pattern="dd-mm-yyyy", state="readonly", font=("Leelawadee", 12))
        midterm_date_picker.grid(row=1, column=0)
        finale_date_frame = ctk.CTkFrame(master=date_frame)
        finale_date_frame.grid(row=0, column=1)
        final_date_picker_label = AddCoursePage.createLabel(finale_date_frame, "Final Exam Date: ")
        final_date_picker_label.grid(row=0, column=1)
        final_date_picker = cal.DateEntry(finale_date_frame, date_pattern="dd-mm-yyyy", state="readonly", font=("Leelawadee", 12))
        final_date_picker.grid(row=1, column=1)
        
        # Create Time Clock
        time_frame = ctk.CTkFrame(master=date_time_picker_frame)
        time_frame.grid(row=1, column=0, padx=5, pady=(0,10))
        midterm_time_frame = ctk.CTkFrame(master=time_frame)
        midterm_time_frame.grid(row=0, column=0)
        midterm_start_time_label = ctk.CTkLabel(master=midterm_time_frame, text="Midterm Exam Start Time: ", font=("Leelawadee", 15))
        midterm_start_time_label.grid(row=0, column=0)
        midterm_show_time = ctk.CTkLabel(master=midterm_time_frame, text="00:00:00", font=("Leelawadee", 15))
        midterm_show_time.grid(row=1, column=0)
        midterm_start_btn = ctk.CTkButton(master=midterm_time_frame, text="Set Time", font=("Leelawadee", 15),
                            command=lambda: Clock(midterm_show_time))
        midterm_start_btn.grid(row=2, column=0)
        final_time_frame = ctk.CTkFrame(master=time_frame)
        final_time_frame.grid(row=0, column=1, padx=5, pady=(10,10))
        final_start_time_label = ctk.CTkLabel(master=final_time_frame, text="Final Exam Start Time: ", font=("Leelawadee", 15))
        final_start_time_label.grid(row=0, column=0)
        final_show_time = ctk.CTkLabel(master=final_time_frame, text="00:00:00", font=("Leelawadee", 15))
        final_show_time.grid(row=1, column=0)
        final_start_btn = ctk.CTkButton(master=final_time_frame, text="Set Time", font=("Leelawadee", 15),
                            command=lambda: Clock(final_show_time))
        final_start_btn.grid(row=2, column=0)
        
        
        # Create Buttons Frame
        button_frame = ctk.CTkFrame(master=sub_master_frame_1)
        button_frame.pack(pady=(30,0))
        
        # Create Impoert Button
        import_button = ctk.CTkButton(master=button_frame, fg_color='gray',
                                width=200, height=50,
                                text="Import Student Data",
                                font=("Leelawadee", 25),
                                command=lambda: AddCoursePage.importData())
        import_button.grid(row=0, column=0, padx=10, pady=10)
        
        # Create Add Button
        submit_button = ctk.CTkButton(master=button_frame, fg_color='green',
                                width=200, height=50,
                                text="Submit",
                                font=("Leelawadee", 25),
                                command=lambda: AddCoursePage.addData(courseID_entry.get(), courseName_entry.get(), 
                                                                      radio_var.get(), combobox_var.get(), 
                                                                      midterm_date_picker.get_date(), final_date_picker.get_date()))
        submit_button.grid(row=1, column=0, padx=10, pady=10)
        
        # Exit Button
        exit_button = ctk.CTkButton(master=sub_master_frame_1, fg_color='red',
                                width=200, height=50,
                                text="Exit",
                                font=("Leelawadee", 25),
                                command=window.destroy)
        exit_button.pack(side="bottom", pady=(30,30))
        
        # Back Button
        back_button = ctk.CTkButton(master=sub_master_frame_1, fg_color='gray',
                                width=200, height=50,
                                text="Back",
                                font=("Leelawadee", 25),
                                command=lambda: AddCoursePage.back(window, master_frame))
        back_button.pack(side="bottom", pady=(200,0))
    
    # Create Frame 2
    def createFrame2(window, master_frame):
        # Create Sub master frame 2
        sub_master_frame_2 = ctk.CTkFrame(master=master_frame)
        sub_master_frame_2.grid(row=0, column=1, padx=(0,10), pady=10 )
        
    def __init__(self, window):
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        master_frame.grid_rowconfigure(0, weight=1)
        master_frame.grid_columnconfigure(0, weight=1)

        AddCoursePage.createFrame1(window, master_frame)
