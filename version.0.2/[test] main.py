from algrorithm import face_data_collect as fdatcol
from algrorithm import face_train as ftrain
from algrorithm import face_recognition as frec
# from algrorithm import csv_write as csvw
import csv


course_id = input("Enter Course Code: ")
mode = input("1: csv write\n2: face collect\n3: face train\n4: face recognition\n5: clean up attendence\nEnter Mode : ")
if mode == '1':
    # csvw.runCSVWrite(course_id)
    print("Old Version")
elif mode == '2':
    fdatcol.runFaceDataCollect(course_id)
elif mode == '3':
    ftrain.runFaceTrain(course_id)
elif mode == '4':
    frec.runFaceRecognition(course_id)
elif mode == '5':
    #for clean up attendence file
    with open('datasets/data/attendance/'+ course_id +'_attendence.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Student ID', 'Name', 'Attendence Time'])
else:
    print("Mode Not Found")