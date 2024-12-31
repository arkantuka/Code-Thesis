import threading
import customtkinter as ctk
import openpyxl
import cv2
import os
import pages.manage_student_data_menu_page as mng_std_menu
from PIL import Image
from tkinter import messagebox, ttk
from CTkMessagebox import CTkMessagebox

font = "THSarabunNew"
button_font_size = 30
header_font_size = 50
entry_font_size = 20
table_font_size = 15

# Create Camera Thread
class CameraThread(threading.Thread):
    def __init__(self, camera_id, camera_frame):
        threading.Thread.__init__(self)
        self.camera_id = camera_id
        self.camera_frame = camera_frame
        
    def run(self):
        CollectFacePage.capture_video(self.camera_id, self.camera_frame)

class CollectFacePage:
    
    student_id = ''
    student_name = ''
    faces_path = ''
    capture_status = False
    cam1_count = 0
    cam2_count = 0
    table = None
    
    def close_camera():
        cam1 = cv2.VideoCapture(0+cv2.CAP_DSHOW)
        cam2 = cv2.VideoCapture(1+cv2.CAP_DSHOW)
        cam1.release()
        cam2.release()
        cv2.destroyAllWindows()
    
    # Back Button Function
    def back(window, frame, workbook):
        CollectFacePage.close_camera()
        workbook.close()
        frame.destroy()
        mng_std_menu.StudentMenu(window)
        
    # Create Button
    def createButton(frame, text, command):
        button = ctk.CTkButton(master=frame, fg_color='gray',
                                width=200, height=50,
                                text=text,
                                font=(font, button_font_size, "bold"),
                                command=command)
        return button
    
    # Create Entry
    def createEntry(frame, wid, hold_text):
        entry = ctk.CTkEntry(frame, width=wid,
                             font=(font, entry_font_size), text_color='black',
                             placeholder_text=hold_text,
                             fg_color="#f0f0f0")
        return entry
    
    # Select record Function
    def select_record(table, id_entry, name_entry):
        try:
            # Clear entry boxs
            id_entry.delete(0, 'end')
            name_entry.delete(0, 'end')
            # Grab record
            selected = table.focus()
            values = table.item(selected, 'values')
            # Output to boxs
            id_entry.insert(0, values[0])
            name_entry.insert(0, values[1])
            # Set ID and Name
            CollectFacePage.set_id_name(id_entry, name_entry)
        except:
            pass         
    
    def set_table(table):
        CollectFacePage.table = table
    
    # Update Face Status Function
    def update_face_status_facedetect(table, id, name):
        # Grab record number
        selected = table.focus()
        face_status = "Collected"
        # Save new data
        table.item(selected, text="", values=(id, name, face_status))
        
    # Set ID and Name
    def set_id_name(id_entry, name_entry):
        if id_entry.get() and name_entry.get() != '':
            CollectFacePage.student_id = id_entry.get()
            CollectFacePage.student_name = name_entry.get()
        else:
            pass
    
    def find_ids_index_duplicate(ids_database, ids_opened):
        idx = []
        for id in ids_database:
            if id in ids_opened:
                idx.append(ids_opened.index(id)+3)
        return idx
    
    def update_face_status(ids, year_path):
        collection_ids = []
        faceID_path = os.listdir(f"version.final/images/{year_path}")
        for id in faceID_path:
            collection_ids.append(id)
        return CollectFacePage.find_ids_index_duplicate(collection_ids, ids)
    
    def sort_column(table, col, reverse):
        data = [(table.set(item, col),item) for item in table.get_children('')]
        data.sort(reverse=reverse)
        for index, (val, item) in enumerate(data):
            table.move(item, '', index)
        table.heading(col, command=lambda: CollectFacePage.sort_column(table, col, not reverse))
            
    # Create Frame 1 Function
    def createFrame1(window, master_frame, file_path):
        # Load Excel File    
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        loadToList = list(sheet.values)
        list_of_data = []
        for row in loadToList:
            if row[0][:] == 'None':
                continue
            list_of_data.append(list(row))
        all_ids = [i[0] for i in list_of_data[3:]]
        year_path = os.path.basename(file_path)
        year_path = os.path.splitext(year_path)[0]
        duplicate_ids = CollectFacePage.update_face_status(all_ids, year_path)
        for idx in duplicate_ids:
            list_of_data[idx][2] = "Collected"        

        # Create Sub master Frame 1
        sub_master_frame_1 = ctk.CTkFrame(master=master_frame)
        sub_master_frame_1.grid(row=0, column=0, padx=(10,0), pady=10 )
        
        # Create Student Information Label
        student_information_label = ctk.CTkLabel(master=sub_master_frame_1,
                                                text="Student Information",
                                                font=(font, header_font_size, "bold"),
                                                padx=20, pady=10)
        student_information_label.pack(pady=(15, 0))
        
        # Create Student Date Frame
        student_data_frame = ctk.CTkFrame(master=sub_master_frame_1)
        student_data_frame.pack()

        # Create Table Frame
        table_frame = ctk.CTkFrame(master=student_data_frame)
        table_frame.grid(row=0, column=0, padx=10, pady=5)
        
        # Create Scrollbar and Table
        tree_scrollbar = ttk.Scrollbar(table_frame, orient="vertical")
        tree_scrollbar.pack(side="right", fill="y")
        table = ttk.Treeview(table_frame, height=25, show="headings",
                                     yscrollcommand=tree_scrollbar.set)
        table.pack(fill="both", expand=True)
        tree_scrollbar.config(command=table.yview)
        
        # Configure Table
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(font, table_font_size,"bold"))
        style.configure("Treeview", font=(font, table_font_size), rowheight=20)

        # Insert Table
        table['columns'] = list_of_data[0]
        table.column('#0', width=0, stretch='YES')
        table.column('Student ID', anchor='center', width=130)
        table.column('Name', width=260)
        table.column('Face Status', anchor='center', width=100)
        for header in list_of_data[0]:
            table.heading(str(header), text=str(header), command=lambda c=header: CollectFacePage.sort_column(table, c, False))
        for value in list_of_data[1:]:
            table.insert("", "end", values=value)
            
        # Create Student Entry Frame
        entry_frame = ctk.CTkFrame(master=sub_master_frame_1)
        entry_frame.pack()
        
        # Create Entry for show selection data
        style.configure("Entry", font=(font, entry_font_size, 'bold'))
        id_label = ctk.CTkLabel(entry_frame, text='Student ID')
        id_label.grid(row=0, column=0)
        id_entry = CollectFacePage.createEntry(entry_frame, 150, 'Student ID')
        id_entry.grid(row=1, column=0)
        name_label = ctk.CTkLabel(entry_frame, text='Full Name')
        name_label.grid(row=0, column=1)
        name_entry = CollectFacePage.createEntry(entry_frame, 350, 'Full Name')
        name_entry.grid(row=1, column=1)
        
        CollectFacePage.set_table(table)
        
        # bind
        table.bind('<ButtonRelease-1>', lambda e: CollectFacePage.select_record(table, id_entry, name_entry))
        
        # Exit Button
        exit_button = ctk.CTkButton(master=sub_master_frame_1, fg_color='red',
                                    width=220, height=50,
                                    text="Exit",
                                    font=(font, button_font_size, "bold"),
                                    command=window.destroy)
        exit_button.pack(side="bottom", pady=(30,25))
        
        # Back Button
        back_button = ctk.CTkButton(master=sub_master_frame_1, fg_color='green',
                                    width=220, height=50,
                                    text="Back",
                                    font=(font, button_font_size, "bold"),
                                    command=lambda: CollectFacePage.back(window, master_frame, workbook))
        back_button.pack(side="bottom", pady=(20,0))
        
    # Create Camera Lebel and Show
    def capture_video(camid, cam_frame):
        # Create Face Detection YUNet
        directory = os.path.dirname(__file__)
        weights = os.path.join(directory, "face_detection_yunet_2023mar.onnx")
        face_cascade_yunet = cv2.FaceDetectorYN_create(weights, "", (0, 0))
        # Create Camera Label and set Camera
        width = 480
        height = 480
        cam = cv2.VideoCapture(camid+cv2.CAP_DSHOW)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        lmain = ctk.CTkLabel(cam_frame, text="")
        lmain.pack()
        # Show Frame Function
        def show_frame():
            _, frame = cam.read()
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Detect Faces
            h, w, _ = frame.shape
            faces = face_cascade_yunet.setInputSize((w, h))
            _, faces = face_cascade_yunet.detect(frame)
            faces = faces if faces is not None else []
            # Draw Bounding Box
            for face in faces:
                # Face Line
                box = list(map(int, face[:4]))
                if CollectFacePage.capture_status is False:
                    color = (255, 0, 0, 255)
                    confidence = face[-1]
                    confidence = "{:.2f}".format(confidence)
                else:
                    color = (255, 215, 0, 255)
                    confidence = "Processing..."
                thickness = 2
                cv2.rectangle(cv2image, box, color, thickness, lineType=cv2.LINE_AA)
                # Face Confidence
                position = (box[0], box[1] - 10)
                font = cv2.FONT_HERSHEY_SIMPLEX
                scale = 0.5
                thickness = 2
                cv2.putText(cv2image, confidence, position, font, scale, color, thickness, lineType=cv2.LINE_AA)
                # Capture Faces
                if CollectFacePage.cam1_count == 50 and CollectFacePage.cam2_count == 50:
                    CollectFacePage.cam1_count, CollectFacePage.cam2_count = 0, 0
                    CollectFacePage.capture_status = False
                    CollectFacePage.update_face_status_facedetect(CollectFacePage.table, CollectFacePage.student_id, CollectFacePage.student_name)
                    messagebox.showinfo(title="Success", message="Face Capture has been completed.")
                elif CollectFacePage.capture_status:
                    if CollectFacePage.cam1_count < 50 and camid == 0:
                        CollectFacePage.cam1_count += 1
                        cv2.imwrite(CollectFacePage.faces_path+"/"+str(CollectFacePage.student_id)+"-"
                                    +str(camid)+"-"+str(CollectFacePage.cam1_count)+".jpg", 
                                    gray_img[box[1]:box[1]+box[3], box[0]:box[0]+box[2]])
                    if CollectFacePage.cam2_count < 50 and camid == 1:
                        CollectFacePage.cam2_count += 1
                        cv2.imwrite(CollectFacePage.faces_path+"/"+str(CollectFacePage.student_id)+"-"
                                    +str(camid)+"-"+str(CollectFacePage.cam2_count)+".jpg",
                                    gray_img[box[1]:box[1]+box[3], box[0]:box[0]+box[2]])
            # Show Image
            img = Image.fromarray(cv2image)
            imgctk = ctk.CTkImage(light_image=img, dark_image=img, size=img.size)
            lmain.configure(image=imgctk)
            lmain.after(100, show_frame)
        show_frame()
        
    # Create Collect Face Function
    def collect_face(year_folder):
        result = messagebox.askyesno(title="Confirm", message="Are you sure you want to collect face?")
        if result:
            parent_dir = "version.final/images"
            year_folder = os.path.join(parent_dir, year_folder)
            if CollectFacePage.student_id != '':
                faces_folder = os.path.join(year_folder, CollectFacePage.student_id)
                if not os.path.exists(faces_folder):os.mkdir(faces_folder)
                CollectFacePage.faces_path = faces_folder
                CollectFacePage.capture_status = True
                CollectFacePage.capture_cam1_status = True
                CollectFacePage.capture_cam2_status = True
        else:
            pass

    # Create Frame 2 Function
    def createFrame2(window, master_frame, year):
        # Create Sub Master Frame 2
        sub_master_frame_2 = ctk.CTkFrame(master=master_frame)
        sub_master_frame_2.grid(row=0, column=1, padx=5, pady=5)
        

        camera_main_frame = ctk.CTkFrame(master=sub_master_frame_2)
        camera_main_frame.pack(fill="both", expand=True)

        camera_frame = ctk.CTkFrame(master=camera_main_frame)
        camera_frame.pack(fill="both", expand=True)
        
        # Create Camera 1 Frame
        camera_1_frame = ctk.CTkFrame(master=camera_frame)
        camera_1_frame.grid(row=0, column=0, padx=5, pady=5)
        
        # Create Camera 2 Frame
        camera_2_frame = ctk.CTkFrame(master=camera_frame)
        camera_2_frame.grid(row=0, column=1, padx=5, pady=5)
        
        # Start Thread
        thread1 = CameraThread(0, camera_1_frame)
        thread2 = CameraThread(1, camera_2_frame)
        thread1.start()
        thread2.start()
        
                # Create Facecollection Frame
        collect_button_frame = ctk.CTkFrame(master=camera_main_frame)
        collect_button_frame.pack(pady=10)
        
        # Create Facecollection Button
        collect_button = CollectFacePage.createButton(collect_button_frame, 'Capture Face',
                                                            lambda: CollectFacePage.collect_face(year))
        collect_button.pack(pady=10)
                
    
    def __init__(self, window, file_path):
        
        # Create Master Frame
        master_frame = ctk.CTkFrame(master=window)
        master_frame.pack(fill="both", expand=True)
        master_frame.grid_rowconfigure(0, weight=1)
        master_frame.grid_columnconfigure(0, weight=1)
        master_frame.grid_columnconfigure(1, weight=1)
        
        year_path = os.path.basename(file_path)
        year_path = os.path.splitext(year_path)[0]
        
        CollectFacePage.createFrame1(window, master_frame, file_path)
        CollectFacePage.createFrame2(window, master_frame, year_path)