import datetime
import cv2
import csv
import main_page as mp

def getStudentNameAndID(course_id):
    name_list = []
    id_list = []
    with open('version.0.2/datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            name_list.append(row[1])
            id_list.append(row[0])
    return name_list, id_list

def writeAttendance(course_id, student_id, name):
    with open('version.0.2/datasets/data/attendance/'+ course_id +'_attendence.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([student_id, name, datetime.datetime.now().strftime("%d/%m/%Y : %H:%M:%S")])

# Main Function
def runFaceRecognition(course_id):
    all_name, all_id = getStudentNameAndID(course_id)
    print(all_name, all_id)
    already_Taken = []

    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('version.0.2/algrorithm/haarcascade_frontalface_default.xml')
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('version.0.2/datasets/data/train_data/'+course_id+"_trainingData.yml")

    while True:
        ret,frame = video.read()
        frame = cv2.resize(frame, (800, 600))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.05, 5)
        for (x, y, w, h) in faces:
            serial, conf = face_recognizer.predict(gray[y:y+h, x:x+w])
            print(conf, serial)
            if(conf > 60):
                # print(all_id.index(serial))
                index = all_id.index(str(serial))
                cv2.putText(frame, all_name[index]+" "+"{:.2f}".format(conf), 
                            (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
                if all_name[index] not in already_Taken:
                    writeAttendance(course_id, all_id[index], all_name[index])
                    already_Taken.append(all_name[index])
            else:
                cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
            
        cv2.imshow("Face Recognition Test",frame)

        key_exit = cv2.waitKey(1)
        if key_exit == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    mp.MainPage(course_id)
