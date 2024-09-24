import csv
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import main_page as mp
import customtkinter as ctk
    
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
        with open('version.0.4/datasets/data/student_in_course_detail/'+ course_id +'.csv',encoding="utf8", mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Student ID', 'Name', 'Major'])
        with open('version.0.4/datasets/data/attendance/'+ course_id +'_attendence.csv',encoding="utf8", mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Student ID', 'Name', 'Major', 'Attendence Time'])
        return False
    
# Add New Student Info
def writeData(course_id, data):
        with open('version.0.4/datasets/data/student_in_course_detail/'+ course_id +'.csv', encoding="utf8", mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Student ID', 'Name', 'Major'])
            for i in range(len(data)):
                writer.writerow(data[i])
                
# Get Student Info           
def getStudentInfo(path):
    with open(path, encoding="utf8", mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        data = []
        for row in reader:
            data.append(row)
        return data    
        
# Main Function
def runCSVWrite(course_id):
    path = 'version.0.4/datasets/data/student_in_course_detail/'
    checkNewCourse(path, course_id)
    
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('dark-blue')
    ctk.deactivate_automatic_dpi_awareness()
    ctk.set_window_scaling(1.0)
    ctk.set_widget_scaling(1.0)
    window = ctk.CTk()
    window.after(0, lambda: window.wm_state('zoomed'))
    window.title('Student Infomations')
    
    # Create MainLabel
    choose_active_label = ctk.CTkLabel(master=window, 
                              text="Course : "+str(course_id), 
                              font=("Leelawadee", 30) ,
                              padx=100, pady=10)
    choose_active_label.pack()
    
    # Create Frame
    table_frame = ctk.CTkFrame(window, width=800, height=500)
    table_frame.pack(pady=20)

    # Create Scrollbar
    tree_scroll = ctk.CTkScrollbar(table_frame, orientation='vertical')
    tree_scroll.pack(side='right', fill='y')
    
    table = ttk.Treeview(table_frame, height=20, yscrollcommand=tree_scroll.set, selectmode="extended")
    table.pack()

    tree_scroll.configure(command=table.yview)
    
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Leelawadee', 15, 'bold'))
    style.configure("Treeview", font=('Leelawadee', 15), rowheight=20)
    
    table['columns'] = ("Student ID", "Name", "Major")
    
    table.column("#0", width=0, stretch='YES')
    table.column("Student ID", anchor='center')
    table.column("Name" , width=420)
    table.column("Major" , width=450)
    
    table.heading("#0", text="", anchor='w')
    table.heading("Student ID", text="Student ID", anchor='center')
    table.heading("Name", text="Name", anchor='center')
    table.heading("Major", text="Major", anchor='center')
    
    # Get Student Info
    data = getStudentInfo(path+str(course_id)+'.csv')
    
    for record in data[1:]:
        table.insert('', 'end', values=record)
    
    add_frame = ctk.CTkFrame(window)
    add_frame.pack(pady=20)
    style.configure("Entry", font=('Leelawadee', 20, 'bold'))
    id_label = ctk.CTkLabel(add_frame, text="Student ID")
    id_label.grid(row=0, column=0)
    id_entry = ctk.CTkEntry(add_frame, width=200, 
                            font=('Leelawadee', 20), text_color="black",
                            placeholder_text="Student ID",
                            fg_color="#f0f0f0")
    id_entry.grid(row=1, column=0)
    name_label = ctk.CTkLabel(add_frame, text="Full Name")
    name_label.grid(row=0, column=1)
    name_entry = ctk.CTkEntry(add_frame, width=420, 
                              font=('Leelawadee', 20), text_color="black",
                              placeholder_text="Full Name",
                              fg_color="#f0f0f0")
    name_entry.grid(row=1, column=1)
    major_label = ctk.CTkLabel(add_frame, text="Major")
    major_label.grid(row=0, column=2)
    major_entry = ctk.CTkEntry(add_frame, width=450, 
                               font=('Leelawadee', 20), text_color="black",
                               placeholder_text="Major",
                               fg_color="#f0f0f0")
    major_entry.grid(row=1, column=2)
    
    def select_record():
	    # Clear entry boxes
        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        major_entry.delete(0, 'end')

        # Grab record number
        selected = table.focus()
        # Grab record values
        values = table.item(selected, 'values')

        # output to entry boxes
        id_entry.insert(0, values[0])
        name_entry.insert(0, values[1])
        major_entry.insert(0, values[2])

    # Add Record
    def addInfo():
        table.insert(parent='', index='end', text="",
                     values=(id_entry.get(), name_entry.get(), major_entry.get()))
        
        # Clear the boxes
        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        major_entry.delete(0, 'end')
        
    def update_record():
        # Grab record number
        selected = table.focus()
        values = table.item(selected, 'values')
        # Save new data
        table.item(selected, text="", values=(id_entry.get(), name_entry.get(), major_entry.get()))

        # Clear entry boxes
        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        major_entry.delete(0, 'end')
        
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

    def callMain():
        window.destroy()
        mp.MainPage(course_id)
    
    # Edit Record Button Frame
    edit_button_frame = ctk.CTkFrame(window)
    edit_button_frame.pack(pady=10)
    # Create Buttons
    # Add Button
    add_info = ctk.CTkButton(master=edit_button_frame,
                                    fg_color="#f8f8f8",
                                text="Add This Infomation",
                                text_color="black",
                                height=60, width=300,
                                font=("Leelawadee", 20),
                                command=lambda: addInfo())
    add_info.grid(row=0, column=0, padx=20, pady=20)
    # Update Button
    update_button = ctk.CTkButton(master=edit_button_frame,
                                    fg_color="#f8f8f8",
                                text="Update This Infomation",
                                text_color="black",
                                height=60, width=300,
                                font=("Leelawadee", 20),
                                command=lambda: update_record())
    update_button.grid(row=0, column=1, padx=20, pady=20)
    # Delete Button
    delete_button = ctk.CTkButton(master=edit_button_frame,
                                    fg_color="#f8f8f8",
                                text="Delete Infomation",
                                text_color="black",
                                height=60, width=300,
                                font=("Leelawadee", 20),
                                command=lambda: deleteItems())
    delete_button.grid(row=0, column=2, padx=20, pady=20)
    
    table.bind('<Delete>', lambda e: deleteItems())
    table.bind("<ButtonRelease-1>", lambda e: select_record())
    
    back_button = ctk.CTkButton(master=window,
                                    fg_color="#f8f8f8",
                                text="Back without Saving",
                                text_color="black",
                                height=60, width=200,
                                font=("Leelawadee", 30, "bold"),
                                command=lambda: callMain())
    back_button.pack(side="bottom", pady=30)

    save_button = ctk.CTkButton(master=window,
                                    fg_color="#f8f8f8",
                                text="Save and Back to Main Page",
                                text_color="black",
                                height=60, width=200,
                                font=("Leelawadee", 30, "bold"),
                                command=lambda: write_to_csv())
    save_button.pack( side="bottom")

    window.mainloop()