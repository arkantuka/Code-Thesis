import csv
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import main_page as mp

# Center Window
def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")
    
# Check New Course for Create CSV
def checkNewCourse(path, course_id):
    course_paths = [os.path.join(path,f) for f in os.listdir(path)]
    course_ids = []
    for course_path in course_paths:
        courseID = os.path.split(course_path)[1].split('.')[0]
        course_ids.append(courseID)
    if course_id in course_ids:
        return True
    else:
        with open('version.0.3/datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Student ID', 'Name'])
        with open('version.0.3/datasets/data/attendance/'+ course_id +'_attendence.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Student ID', 'Name', 'Attendence Time'])
        return False
    
# Add New Student Info
def writeData(course_id, data):
        with open('version.0.3/datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Student ID', 'Name'])
            for i in range(len(data)):
                writer.writerow(data[i])
                
# Get Student Info           
def getStudentInfo(path):
    with open(path, mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        data = []
        for row in reader:
            data.append(row)
        return data
        
# Main Function
def runCSVWrite(course_id):
    path = 'version.0.3/datasets/data/student_in_course_detail/'
    checkNewCourse(path, course_id)
    
    window = tk.Tk()
    window.title('Student Info')
    window.eval('tk::PlaceWindow . center')
    
    # Create MainLabel
    choose_active_label = tk.Label(window, 
                              text="Course : "+str(course_id), 
                              font=("Leelawadee", 30) ,
                              padx=100, pady=10)
    choose_active_label.pack()
    
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

    # Add Record
    def addInfo():
        table.insert(parent='', index='end', text="", values=(id_entry.get(), name_entry.get()))

        # Clear the boxes
        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        
    def update_record():
        # Grab record number
        selected = table.focus()
        # Save new data
        table.item(selected, text="", values=(id_entry.get(), name_entry.get()))

        # Clear entry boxes
        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        
    # Delete Items in Table
    def deleteItems():
        for item in table.selection():
            table.delete(item)
    
    # Write Data to CSV and Close Window    
    def write_to_csv():
        updated_data = []
        for i in range(table.get_children().__len__()):
            updated_data.append(table.item(table.get_children()[i])['values'])
        writeData(course_id, updated_data)
        window.destroy()
        mp.MainPage(course_id)
    
    # Create Buttons
    # Add Button
    add_info = tk.Button(window, 
                      height=2,
                      width=20,
                      text="Add This Infomation", 
                      command=addInfo)
    add_info.pack(pady=10)
    # Update Button
    update_button = tk.Button(window,
                           height=2,
                           width=20,
                           text="Update This Infomation", 
                           command=update_record)
    update_button.pack(pady=10)
    # Delete Button
    delete_data = tk.Button(window, 
                         height=2,
                         width=20,
                         text="Delete This Infomation", 
                         command=deleteItems)
    delete_data.pack(pady=10)
    
    table.bind('<Delete>', lambda e: deleteItems())
    table.bind("<ButtonRelease-1>", lambda e: select_record())
    
    write_to_csv = tk.Button(window, foreground="green",background='black',
                         height=2,
                         width=35,
                         font=("Leelawadee", 15, 'bold'),
                         text="Write To CSV File and Back to Main Page", 
                         command=write_to_csv)
    write_to_csv.pack(pady=10)
    
    window.mainloop()
