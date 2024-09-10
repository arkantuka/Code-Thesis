# import cv2

# cam1 = cv2.VideoCapture(0)
# cam2 = cv2.VideoCapture(1)
# cam3 = cv2.VideoCapture(2)

# while True:
#     ret1, frame1 = cam1.read()
#     ret2, frame2 = cam2.read()
#     ret3, frame3 = cam3.read()
    
#     frame1 = cv2.resize(frame1, (200, 200))
#     frame2 = cv2.resize(frame2, (200, 200))
#     frame3 = cv2.resize(frame3, (200, 200))

#     all_cam = cv2.hconcat([frame1, frame2, frame3])
#     cv2.imshow("test", all_cam)
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

import datetime
import cv2
import csv

def getStudentNameAndID(course_id):
    name_list = []
    id_list = []
    with open('datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            name_list.append(row[2])
            id_list.append(row[1])
    return name_list, id_list

def writeAttendance(course_id, student_id, name):
    with open('datasets/data/attendance/'+ course_id +'_attendence.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([student_id, name, datetime.datetime.now().strftime("%H:%M:%S")])

def runFaceRecognition(course_id):
    all_name, all_id = getStudentNameAndID(course_id)
    already_Taken = []
    #use 3 camera
    cam1 = cv2.VideoCapture(0)
    cam2 = cv2.VideoCapture(1)
    cam3 = cv2.VideoCapture(2)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read(course_id+"_trainingData.yml")

    while True:
        ret1, frame1 = cam1.read()
        ret2, frame2 = cam2.read()
        ret3, frame3 = cam3.read()
        
        frame1 = cv2.resize(frame1, (480, 360))
        frame2 = cv2.resize(frame2, (480, 360))
        frame3 = cv2.resize(frame3, (480, 360))

        all_cam = cv2.hconcat([frame1, frame2, frame3])

        gray = cv2.cvtColor(all_cam, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.05, 100, minSize=(40, 40))
        for (x, y, w, h) in faces:
            serial, conf = face_recognizer.predict(gray[y:y+h, x:x+w])
            if(conf > 70):
                print(serial)
                cv2.putText(all_cam, all_name[serial]+" "+str(conf), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.rectangle(all_cam, (x, y), (x+w, y+h), (0, 255, 0), 5)
                if all_name[serial] not in already_Taken:
                    writeAttendance(course_id, all_id[serial], all_name[serial])
                    already_Taken.append(all_name[serial])
            else:
                cv2.putText(all_cam, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                cv2.rectangle(all_cam, (x, y), (x+w, y+h), (0, 0, 255), 5)
            
        cv2.imshow("Face Recognition Test",all_cam)

        key_exit = cv2.waitKey(1)
        if key_exit == ord('q'):
            break

    cam1.release(), cam2.release(), cam3.release()
    cv2.destroyAllWindows()
    print("====== Face Recognition Samples Complete ======")

runFaceRecognition('517111')