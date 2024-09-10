import tkinter as tk
from algrorithm import first_add_csv_data as add_dt
from algrorithm import second_face_data_collect as face_coll
from algrorithm import third_face_training as face_train
from algrorithm import fourth_face_recognition as face_rec
from algrorithm import fifth_attendance_time as att
import run_input_course_page as icp

class MainPage():
    
    def createLabel(window,label_name):
        label = tk.Label(window,
                         text=label_name,
                         font=("Leelawadee", 20),
                         padx=100)
        label.pack()
        
    def createButton(window,label_name,command):
        button = tk.Button(window,foreground="blue",background='gray',
                           text=label_name,height=2,width=10,
                           padx=100,
                           font=("Leelawadee", 10, "bold"),
                           command=command)
        button.pack(pady=5)
        
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
        
        window = tk.Tk()
        window.resizable(False, False)
        window.title('Test Application GUI Window Face Recognition')
        window.eval('tk::PlaceWindow . center')
        
        choose_active_label = tk.Label(window, 
                              text="Choose Your Active", 
                              font=("Leelawadee", 30) ,
                              padx=100, pady=10)
        choose_active_label.pack()
        
        #Buttons for each page
        #Buttons for add student data page
        MainPage.createLabel(window,"Student Data Collect")
        MainPage.createButton(window,
                              "Student Data Collect",
                              command=lambda: MainPage.button_click(window,self.course_id,1))
        
        MainPage.createLabel(window,"Student Face Collect")
        MainPage.createButton(window,
                              "Student Face Collect",
                              command=lambda: MainPage.button_click(window,self.course_id,2))
        MainPage.createLabel(window,"Face Train")
        MainPage.createButton(window,
                              "Face Train",
                              command=lambda: MainPage.button_click(window,self.course_id,3))
        #Buttons for face recognition page
        MainPage.createLabel(window,"Face Recognition")
        MainPage.createButton(window,
                              "Face Recognition",
                              command=lambda: MainPage.button_click(window,self.course_id,4))
        
        MainPage.createLabel(window,"Time Attemdance")
        MainPage.createButton(window,
                              "Time Attemdance",
                              command=lambda: MainPage.button_click(window,self.course_id,5))

        back_button = tk.Button(window,foreground="red",background='white',
                                text="Back To Input Course ID",
                                height=2,width=10,padx=80,
                                font=("Leelawadee", 10, "bold"),
                                command=lambda: MainPage.button_click(window,self.course_id,6))
        back_button.pack(pady=10)
        
        window.mainloop()