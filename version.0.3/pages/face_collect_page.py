import cv2
import os
import csv
import tkinter as tk
from tkinter import ttk
import main_page as mp

# Get Student Info           
def getStudentInfo(path):
    with open(path, mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        data = []
        for row in reader:
            data.append(row)
        return data

def chooseStudentIDpopUp(course_id):
    window = tk.Tk()
    window.resizable(False, False)
    window.title('Student ID for Face Data Collection')
    window.eval('tk::PlaceWindow . center')
    path = 'version.0.3/datasets/data/student_in_course_detail/'
    course_label = tk.Label(window, 
                              text="Course : "+str(course_id), 
                              font=("Leelawadee", 30) ,
                              padx=100, pady=10)
    course_label.pack()
    order_label = tk.Label(window, 
                              text="Choose Student : ", 
                              font=("Leelawadee", 15) ,
                              padx=100, pady=10)
    order_label.pack()
    # Create Frame
    table_frame = tk.Frame(window)
    table_frame.pack(pady=20)
    # Create Scrollbar
    tree_scroll = tk.Scrollbar(table_frame)
    tree_scroll.pack(side='right', fill='y')
    table = ttk.Treeview(table_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    table.pack()
    table['columns'] = ("Student ID", "Name")
    table.column("#0", width=0, stretch='NO')
    table.column("Student ID", width=100)
    table.column("Name", width=150)
    table.heading("#0", text="", anchor='w')
    table.heading("Student ID", text="Student ID")
    table.heading("Name", text="Name")
    # Get Student Info
    data = getStudentInfo(path+str(course_id)+'.csv')
    
    for record in data[1:]:
        table.insert('', 'end', values=record)
    
    add_frame = tk.Frame(window)
    add_frame.pack(pady=20)   
    id_label = tk.Label(add_frame, text="Student ID")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(add_frame)
    id_entry.grid(row=1, column=0)
    name_label = tk.Label(add_frame, text="Full Name")
    name_label.grid(row=0, column=1)
    name_entry = tk.Entry(add_frame)
    name_entry.grid(row=1, column=1)
    
    def select_record():
	    # Clear entry boxes
        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        # Grab record number
        selected = table.focus()
        # Grab record values
        values = table.item(selected, 'values')
        # output to entry boxes
        id_entry.insert(0, values[0])
        name_entry.insert(0, values[1])

    # Submit Function
    def submit():
        # Grab record number
        selected = table.focus()
        # Save new data
        table.item(selected, text="", values=(id_entry.get()))
        studentID = id_entry.get()
        window.destroy()
        runFaceDataCollect(course_id, studentID)
    table.bind("<ButtonRelease-1>", lambda e: select_record())
    # Submit Button
    submit_button = tk.Button(window,background='black', foreground='green',
                            text="Submit",
                            font=("Leelawadee", 30, "bold"), 
                            command=submit)
    submit_button.pack(pady=10)
    window.mainloop()
    
def runFaceDataCollect(course_id, student_id):

    print("====== Face Data Collection Started ======")
    directory = os.path.dirname(__file__)
    
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        exit()
        
    weights = os.path.join(directory, "face_detection_yunet_2023mar.onnx")
    face_cascade_yunet = cv2.FaceDetectorYN_create(weights, "", (0, 0))
    count = 1
        
    while True:
        result,frame = video.read()
        if result is False:
            cv2.waitKey(0)
            break
        
        print(course_id, count)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
        height, width, _ = frame.shape
        face_cascade_yunet.setInputSize((width, height))
        _, faces_yn = face_cascade_yunet.detect(frame)
        faces_yn = faces_yn if faces_yn is not None else []
        
        for face in faces_yn:
            count += 1
            box = list(map(int, face[:4]))
            color = (0, 0, 255)
            thickness = 2
            cv2.rectangle(frame, box, color, thickness, cv2.LINE_AA)
                
            confidence = face[-1]
            confidence = "{:.2f}".format(confidence)
            position = (box[0], box[1] - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            scale = 0.5
            thickness = 2
            cv2.putText(frame, confidence, position, font, scale, color, thickness, cv2.LINE_AA)
            
            faces_folder_path = "version.0.3/datasets/images"
            if not os.path.exists(faces_folder_path):
                os.makedirs(faces_folder_path)
            cv2.imwrite(faces_folder_path+"/"+str(student_id)+".cam1."+str(count)+".jpg", gray[box[1]:box[1]+box[3], box[0]:box[0]+box[2]])
            
        cv2.imshow("Face Recognition Test",frame)

        if count > 100:
            break

        key_exit = cv2.waitKey(1)
        if key_exit == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    result = tk.messagebox.askquestion("Enough or not", "Do you want to add more?") 
    if result == True:
        chooseStudentIDpopUp(course_id)
    else:
        mp.MainPage(course_id)
        