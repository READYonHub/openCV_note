import cv2

faces = cv2.imread("faces.png")

gray = cv2.cvtColor(faces, cv2.COLOR_BGR2GRAY)

haar_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

detected_faces = haar_face.detectMultiScale(gray)

for (x,y,w,h) in detected_faces:
    cv2.rectangle(faces, (x, y), (w+x, h+y), (255,255,0), 2 )

cv2.imshow("Arcfelismerő", faces)

cv2.waitKey(0)
cv2.destroyAllWindows()
