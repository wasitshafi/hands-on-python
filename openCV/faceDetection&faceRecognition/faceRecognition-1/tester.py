import cv2
import spreadSheet as sp
def generate_dataset(img, id, img_id):
    cv2.imwrite("dataset/user." + str(id) + "." + str(img_id) + ".jpg", img)

def draw_boundary(img, classifier, scaleFactor, minNeighbours, color,text, clf):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbours)
    coords = []

    for(x, y, w, h) in features:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        id, _= clf.predict(gray_img[y:y+h, x:x+w])
        
        id, confi= clf.predict(gray_img[y:y+h, x:x+w])

        print("userid = ", id, " confidence = " ,confi, end ="\n\n")
        font = cv2.FONT_HERSHEY_SIMPLEX
        """     if(confi <=45):
            if( id == 1):
                cv2.putText(img, "wasit", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)
            elif( id == 2):
                cv2.putText(img, "shivam", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)
        else:
            cv2.putText(img, "Face not detected....!", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)
        """
        if( id == 1):
           cv2.putText(img, "shahid", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)
           sp.markAttendence(id)
        elif( id == 2):
           cv2.putText(img, "salman", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)
           sp.markAttendence(id)
        elif( id == 3):
           cv2.putText(img, "amir", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)
           sp.markAttendence(id)
        elif( id == 5):
           cv2.putText(img, "shivam", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)
           sp.markAttendence(id)
        elif( id == 6):
           cv2.putText(img, "Israr sir", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)
           sp.markAttendence(id)
        elif( id == 48):
           cv2.putText(img, "haimd", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)
           sp.markAttendence(id)
        elif( id == 54):
           cv2.putText(img, "wasit", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)
           sp.markAttendence(id)
        else:
           cv2.putText(img, "Face not recognized....!", (x,y-4), font, 0.8, color, 1, cv2.LINE_AA)

        coords = [x, y, w, h]
    return coords
def recognize(img, clf, faceCascade):
    color = {"blue":(255,0,0),"red": (0,0,255)}

    coords = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "face", clf)
    return img

def detect(img, faceCascade, img_id):
    color = {"blue":(255, 0, 0), "red":(255, 255, 0)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, color['red'], "face")
    if len(coords) == 4:
        roi_img = img[coords[1] : coords[1]+coords[3],coords[0] : coords[0]+coords[2]]
        user_id = 3 # change the user for each different users
        generate_dataset(roi_img, user_id, img_id)

    return img

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.yml")
video_capture = cv2.VideoCapture(0)
img_id  = 0
while True:
    _, img = video_capture.read()
     
    #img = detect(img, faceCascade, img_id)
    img = recognize(img, clf, faceCascade)
    cv2.imshow("face Detection", img)
    img_id = img_id + 1
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
  
