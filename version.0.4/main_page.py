from pages import add_data_page as add_dt
from pages import face_collect_page as face_coll
from pages import face_training_page as face_train
from pages import face_recognition_page as face_rec
from pages import attendance_time_page as att
import run_app as icp
import customtkinter as ctk
from PIL import Image



class MainPage():
    
    def createLabel(window,label_name):
        label = ctk.CTkLabel(master=window,
                         text=label_name,
                         font=("Leelawadee", 25),
                         padx=100)
        return label
    
    def createButton(window,label_name,command):
        button = ctk.CTkButton(master=window,fg_color="gray",
                           text=label_name,height=50,width=200,
                           font=("Leelawadee", 25, "bold"),
                           command=command)
        return button
        
    def createIcon(window,image_path):
        my_image = ctk.CTkImage(light_image=Image.open(image_path),
                    dark_image=Image.open(image_path),
                    size=(200, 200))
     
        image_label = ctk.CTkLabel(master=window, image=my_image,text="")
        image_label.grid(row=0, column=0, padx=20, pady=20)
        
        return image_label

    def button_click(window,course_id,command):
        window.destroy()
        if(command == 1):
            add_dt.runCSVWrite(course_id)
        elif(command == 2):
            face_coll.chooseStudentIDpopUp(course_id)
        elif(command == 3):
            face_train.runFaceTrain(course_id)
        elif(command == 4):
            face_rec.runFaceRecognition(course_id)
        elif(command == 5):
            att.showAttendence(course_id)
        elif(command == 6):
            icp.FaceRecognitionApp().runMain()
        else:
            print("Error")
        
    def __init__(self, course_id):
        self.course_id = course_id
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        ctk.deactivate_automatic_dpi_awareness()
        ctk.set_window_scaling(1.0)
        ctk.set_widget_scaling(1.0)
        window = ctk.CTk()
        window.after(0, lambda: window.wm_state('zoomed'))
        window.title('Test Main Page')
        window.grid_columnconfigure([0,1,2], weight=1)
        window.grid_rowconfigure([0,1,2], weight=1)
        

        choose_active_label = ctk.CTkLabel(master=window, 
                              text="Choose Your Active", 
                              font=("Leelawadee", 35),
                              padx=100, pady=10)
        choose_active_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        choose_active_label.grid(row=0, column=1, padx=20, pady=10)
        
 

        #Buttons for each page
        #Buttons for add student data page
        student_data_frame = ctk.CTkFrame(master=window,)
        student_data_frame.grid(row=1, column=0, padx=20, pady=10)
        #Image
        MainPage.createIcon(student_data_frame,'C:/Users/koonk/Desktop/Code-Thesis-master/version.0.4/icons/student-icon.png')

        student_data_button = MainPage.createButton(student_data_frame,
                              "Student Data Collect",
                              command=lambda: MainPage.button_click(window,self.course_id,1))
        student_data_button.grid(row=1, column=0, padx=20, pady=(0,30))
        
        face_collect_frame = ctk.CTkFrame(master=window)
        face_collect_frame.grid(row=2, column=0, padx=20, pady=10)
        MainPage.createIcon(face_collect_frame,'C:/Users/koonk/Desktop/Code-Thesis-master/version.0.4/icons/facedata.jpg')
        face_collect_button = MainPage.createButton(face_collect_frame,
                              "Student Face Collect",
                              command=lambda: MainPage.button_click(window,self.course_id,2))
        face_collect_button.grid(row=1, column=0, padx=20, pady=(0,30))

        face_train_frame = ctk.CTkFrame(master=window)
        face_train_frame.grid(row=1, column=1, padx=20, pady=10)
        MainPage.createIcon(face_train_frame,'C:/Users/koonk/Desktop/Code-Thesis-master/version.0.4/icons/Train-icon.png')
        face_train_button = MainPage.createButton(face_train_frame,
                              "Face Train",
                              command=lambda: MainPage.button_click(window,self.course_id,3))
        face_train_button.grid(row=1, column=0, padx=20, pady=(0,30))

        face_recog_frame = ctk.CTkFrame(master=window)
        face_recog_frame.grid(row=2, column=1, padx=20, pady=10)
        MainPage.createIcon(face_recog_frame,'C:/Users/koonk/Desktop/Code-Thesis-master/version.0.4/icons/facerec.jpg')
        face_recog_button = MainPage.createButton(face_recog_frame,
                              "Face Recognition",
                              command=lambda: MainPage.button_click(window,self.course_id,4))
        face_recog_button.grid(row=1, column=0, padx=20, pady=(0,30))

        time_attempdance_frame = ctk.CTkFrame(master=window)
        time_attempdance_frame.grid(row=1, column=2, padx=20, pady=10)
        MainPage.createIcon(time_attempdance_frame,'C:/Users/koonk/Desktop/Code-Thesis-master/version.0.4/icons/time2.png')
        time_attempdance_button = MainPage.createButton(time_attempdance_frame,
                              "Time Attendance",
                              command=lambda: MainPage.button_click(window,self.course_id,5))
        time_attempdance_button.grid(row=1, column=0, padx=20, pady=(0,30))

        back_button = ctk.CTkButton(master=window,
                                    fg_color="#f8f8f8",
                                text="Back",
                                text_color="black",
                                height=60, width=200,
                                font=("Leelawadee", 30, "bold", ),
                                command=lambda: MainPage.button_click(window,self.course_id,6))
        back_button.grid(row=3, column=2, padx=20, pady=30)
        
        window.mainloop()