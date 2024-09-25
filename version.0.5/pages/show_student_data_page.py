import customtkinter as ctk
from tkinter import ttk

class ShowStudentDataPage:
    
    # # Back Button Function
    # def back(window, frame):
    #     frame.destroy()
    #     mp.MainPage(window)
        
    def __init__(self, window, list_of_data):
        
        list_values = list_of_data
        
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        
        # Create Student Date Frame
        student_data_frame = ctk.CTkFrame(master=master_frame)
        student_data_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

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
        style.configure("Treeview.Heading", font=("Leelawadee", 10, "bold"))
        style.configure("Treeview", font=("Leelawadee", 10), rowheight=20)

        # Insert Table
        table['columns'] = list_values[0]
        table.column('#0', width=0, stretch='YES')
        table.column('Student ID', anchor='center')
        table.column('Name')
        table.column('Face Status', anchor='center')
        for header in list_values[0]:
            table.heading(str(header), text=str(header))
        for value in list_values[1:]:
            table.insert("", "end", values=value)
        
        # Exit Button
        exit_button = ctk.CTkButton(master=master_frame, fg_color='red',
                                    width=200, height=50,
                                    text="Exit",
                                    font=("Leelawadee", 25),
                                    command=window.destroy)
        exit_button.pack(side="bottom", pady=30)
        
        # # Back Button
        # back_button = ctk.CTkButton(master=master_frame, fg_color='green',
        #                             width=200, height=50,
        #                             text="Back",
        #                             font=("Leelawadee", 25),
        #                             command=lambda: StudentDataPage.back(window, master_frame))
        # back_button.pack(side="bottom", pady=30)