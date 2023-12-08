import cv2

classifier = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while 1:
	ret, img = cap.read()

	mata = classifier.detectMultiScale(img)

	for(x,y,w,h) in mata:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 3)

	cv2.imshow('Eye detection', img)

	k = cv2.waitKey(30)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()