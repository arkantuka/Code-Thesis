import csv
import tkinter as tk
from tkinter import ttk
import main_page as mp

                
# Get Student Info           
def getAttendenceInfo(path):
    with open(path, mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        data = []
        for row in reader:
            data.append(row)
        return data
        
# Main Function
def showAttendence(course_id):
    path = 'version.0.2/datasets/data/attendance/'

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
    
    table = ttk.Treeview(table_frame, height=25, yscrollcommand=tree_scroll.set, selectmode="extended")
    table.pack()

    table['columns'] = ("Student ID", "Name", "Attendence Time")
    
    table.column("#0", width=0, stretch='NO')
    table.column("Student ID", width=100)
    table.column("Name", width=150)
    table.column("Attendence Time", width=150)
    
    table.heading("#0", text="", anchor='w')
    table.heading("Student ID", text="Student ID")
    table.heading("Name", text="Name")
    table.heading("Attendence Time", text="Attendence Time")
    
    # Get Student Info
    data = getAttendenceInfo(path+str(course_id)+'_attendence.csv')
    
    for record in data[1:]:
        table.insert('', 'end', values=record)
    
    back_to_main = tk.Button(window, foreground="green",background='grey',
                         height=2,
                         width=35,
                         font=("Leelawadee", 15, 'bold'),
                         text="Back To Main Page", 
                         command=lambda: [window.destroy(), mp.MainPage(course_id)])
    back_to_main.pack(pady=10)
    
    window.mainloop()
