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
    path = 'version.0.2\datasets/data/student_in_course_detail/'
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
    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    count = 1
    while True:
        ret,frame = video.read()
        frame = cv2.resize(frame, (800, 600))
        print(course_id, count)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.03, 5)
        for (x, y, w, h) in faces:
            count += 1
            faces_folder_path = "version.0.2/datasets/images/"+str(course_id)
            if not os.path.exists(faces_folder_path):
                os.makedirs(faces_folder_path)
            cv2.imwrite(faces_folder_path+"/"+str(student_id)+"."+str(count)+".jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
            
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
        