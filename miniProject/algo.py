import cv2

def fd(image):
    face_cascade = cv2.CascadeClassifier(r'C:\Users\vky_h\Desktop\mini\miniProject\miniApp\templates\miniApp\haarcascade_frontalface_default.xml')
    img = cv2.imread(image)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    print(type(face_cascade))

    for (x, y , w ,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

    #cv2.imshow('img',img)
    if len(faces)==0:
        # return False
        print(faces)
        #False is a signature by default
    else:
        # return True
        print(faces)
        #True is a photo    
    #cv2.waitKey()

# fd('C:/Users/vky_h/Desktop/mini/miniProject/public/static/blank.png')
# fd("C:/Users/vky_h/Pictures/todo.png")
fd(r"C:\Users\vky_h\Pictures\todo.png")