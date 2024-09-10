import datetime
import cv2
import csv
import os
import main_page as mp

def getStudentNameAndID(course_id):
    name_list = []
    id_list = []
    with open('version.0.3/datasets/data/student_in_course_detail/'+ course_id +'.csv', mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            name_list.append(row[1])
            id_list.append(row[0])
    return name_list, id_list

def writeAttendance(course_id, student_id, name):
    with open('version.0.3/datasets/data/attendance/'+ course_id +'_attendence.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([student_id, name, datetime.datetime.now().strftime("%d/%m/%Y : %H:%M:%S")])

# Main Function
def runFaceRecognition(course_id):
    all_name, all_id = getStudentNameAndID(course_id)
    print(all_name, all_id)
    already_Taken = []

    video = cv2.VideoCapture(0)
    
    directory = os.path.dirname(__file__)
    weights = os.path.join(directory, "face_detection_yunet_2023mar.onnx")
    face_cascade_yunet = cv2.FaceDetectorYN_create(weights, "", (0, 0))
    
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    model_path = 'version.0.3/training_faces.yml'
    face_recognizer.read(model_path)

    while True:
        result,frame = video.read()
        if result is False:
            cv2.waitKey(0)
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        height, width, _ = frame.shape
        face_cascade_yunet.setInputSize((width, height))
        _, faces_yn = face_cascade_yunet.detect(frame)
        
        for face in faces_yn:
            
            box = list(map(int, face[:4]))
            color = (0, 0, 255)
            thickness = 2
            cv2.rectangle(frame, box, color, thickness, cv2.LINE_AA)
            
            serial, conf = face_recognizer.predict(gray[box[1]:box[1]+box[3], box[0]:box[0]+box[2]])
            
            print(conf, serial)
            
            position = (box[0], box[1] - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            scale = 0.5
            thickness = 2
            color_red = (0, 0, 255)
            color_green = (0, 255, 0)
            
            if(conf > 60):
                # print(all_id.index(serial))
                index = all_id.index(str(serial))
                cv2.putText(frame, all_name[index]+" "+"{:.2f}".format(conf), 
                            position, font, scale, color_green, thickness)
                cv2.rectangle(frame, box, color_green, thickness, cv2.LINE_AA)
                if all_name[index] not in already_Taken:
                    writeAttendance(course_id, all_id[index], all_name[index])
                    already_Taken.append(all_name[index])
            else:
                cv2.putText(frame, "Unknown", position, font, scale, color_red, thickness)
                cv2.rectangle(frame, box, color_red, thickness, cv2.LINE_AA)
            
        cv2.imshow("Face Recognition Test",frame)

        key_exit = cv2.waitKey(1)
        if key_exit == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    mp.MainPage(course_id)
