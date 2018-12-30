def Opencv():
    import cv2
    import numpy as np
    import msvcrt
    import os

    # img = cv2.imread("abhishek.jpg")
    # #img=img.resize(1080,720,3)
    # # print(img)
    # # # print(img.shape)
    # # cv2.circle((img,center = [5,4] , radius = 150 , color = 'Red'))
    # cv2.imshow("Abhishek",img)
    # k = cv2.waitKey(0)
    # if k == 'a':
    #     cv2.destroyAllWindows()
    # elif k == ord('s'): # wait for 's' key to save and exit
    #     cv2.imwrite('messigray.png',img)
    #     cv2.destroyAllWindows()
    # # img1=np.ones((120,120,3))
    # # cv2.imshow("Img",img1)
    # # cv2.waitKey(0)


    ##FACE RECOGNITION
    # face_cascade = cv2.CascadeClassifier('C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
    face_cascade_1 = cv2.CascadeClassifier('C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')
    # img = cv2.imread('index1.jpg')
    # img1 = cv2.resize(img, (720,500))
    video = cv2.VideoCapture(0)

    path = os.path.abspath(os.path.curdir)
    for root,subdir,file in os.walk(path):
        print(subdir)

    i=1
    while i<150:
        name = str(i)
        ret, frame = video.read()
        print (ret,type(frame))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade_1.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            simg = frame[y:y + h, x:x + w]
            simg1 = cv2.cvtColor(simg, cv2.COLOR_BGR2GRAY)
            cv2.imwrite('F:\FACE_DATA\\face_recog\\abhishek\\abhishek_'+name+'.jpg', simg1)
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(154,124,10),2)


        cv2.imshow('video',frame)
        cv2.waitKey(1)
        i+=1




    cv2.destroyAllWindows()

Opencv()