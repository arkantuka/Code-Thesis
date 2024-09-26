import customtkinter as ctk
import pages.student_data_page as std_page
from tkinter import ttk

class ShowStudentDataPage:
    
    # Back Button Function
    def back(window, frame):
        frame.destroy()
        std_page.StudentDataPage(window)
        
    # Create Button
    def createButton(frame, text, command):
        button = ctk.CTkButton(master=frame, fg_color='gray',
                                width=200, height=50,
                                text=text,
                                font=("Leelawadee", 25),
                                command=command)
        return button
    
    # Create Entry
    def createEntry(frame, wid, hold_text):
        entry = ctk.CTkEntry(frame, width=wid,
                             font=('Leelawadee', 20), text_color='black',
                             placeholder_text=hold_text,
                             fg_color="#f0f0f0")
        return entry
    
    # Select record Function
    def select_record(table, id, name):
        # Clear entry boxs
        id.delete(0, 'end')
        name.delete(0, 'end')
        # Grab record
        selected = table.focus()
        values = table.item(selected, 'values')
        # Outpu to boxs
        id.insert(0, values[0])
        name.insert(0, values[1])
    
    # Insert Data Function
    def insertData():
        pass
    
    # Update Data Function
    def updateData():
        pass
    
    # Delete Data Function
    def deleteData():
        pass
        
    def __init__(self, window, list_of_data):
        
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        
        # Create Student Information Label
        student_information_label = ctk.CTkLabel(master=master_frame,
                                                text="Student Information",
                                                font=("Leelawadee", 35, "bold"),
                                                padx=20, pady=10)
        student_information_label.pack(pady=(20, 0))
        
        # Create Student Date Frame
        student_data_frame = ctk.CTkFrame(master=master_frame)
        student_data_frame.pack()

        # Create Table Frame
        table_frame = ctk.CTkFrame(master=student_data_frame)
        table_frame.grid(row=0, column=0, padx=20, pady=10)
        
        # Create Scrollbar and Table
        tree_scrollbar = ttk.Scrollbar(table_frame, orient="vertical")
        tree_scrollbar.pack(side="right", fill="y")
        table = ttk.Treeview(table_frame, height=15, show="headings",
                                     yscrollcommand=tree_scrollbar.set)
        table.pack(fill="both", expand=True)
        tree_scrollbar.config(command=table.yview)
        
        # Configure Table
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Leelawadee", 12, "bold"))
        style.configure("Treeview", font=("Leelawadee", 15), rowheight=20)

        # Insert Table
        table['columns'] = list_of_data[0]
        table.column('#0', width=0, stretch='YES')
        table.column('Student ID', anchor='center')
        table.column('Name')
        table.column('Face Status', anchor='center')
        for header in list_of_data[0]:
            table.heading(str(header), text=str(header))
        for value in list_of_data[1:]:
            table.insert("", "end", values=value)
            
        # Create Student Entry Frame
        entry_frame = ctk.CTkFrame(master=master_frame)
        entry_frame.pack()
        
        # Create Entry for show selection data
        style.configure("Entry", font=('Leelawadee', 20, 'bold'))
        id_label = ctk.CTkLabel(entry_frame, text='Student ID')
        id_label.grid(row=0, column=0)
        id_entry = ShowStudentDataPage.createEntry(entry_frame, 200, 'Student ID')
        id_entry.grid(row=1, column=0)
        name_label = ctk.CTkLabel(entry_frame, text='Full Name')
        name_label.grid(row=0, column=1)
        name_entry = ShowStudentDataPage.createEntry(entry_frame, 420, 'Full Name')
        name_entry.grid(row=1, column=1)
            
        # Create Button Frame
        button_frame = ctk.CTkFrame(master=master_frame)
        button_frame.pack(pady=(20,0))
        
        # Create Insert Data Button
        insert_data_button = ShowStudentDataPage.createButton(button_frame, 'Insert Data',
                                                              lambda: ShowStudentDataPage.insertData)
        insert_data_button.grid(row=0, column=0, padx=20, pady=10)
        
        # Create Update Data Button
        update_data_button = ShowStudentDataPage.createButton(button_frame, 'Update Data',
                                                              lambda: ShowStudentDataPage.updateData)
        update_data_button.grid(row=0, column=1, padx=20, pady=10)
        
        # Create Delete Data Button
        delete_data_button = ShowStudentDataPage.createButton(button_frame, 'Delete Data',
                                                              lambda: ShowStudentDataPage.deleteData)
        delete_data_button.grid(row=0, column=2, padx=20, pady=10)
        
        # bind
        table.bind('<Delete>', lambda e: ShowStudentDataPage.deleteData())
        table.bind('<ButtonRelease-1>', lambda e: ShowStudentDataPage.select_record(table, id_entry, name_entry))
        
        # Exit Button
        exit_button = ctk.CTkButton(master=master_frame, fg_color='red',
                                    width=200, height=50,
                                    text="Exit",
                                    font=("Leelawadee", 25),
                                    command=window.destroy)
        exit_button.pack(side="bottom", pady=30)
        
        # Back Button
        back_button = ctk.CTkButton(master=master_frame, fg_color='green',
                                    width=200, height=50,
                                    text="Back",
                                    font=("Leelawadee", 25),
                                    command=lambda: ShowStudentDataPage.back(window, master_frame))
        back_button.pack(side="bottom", pady=30)