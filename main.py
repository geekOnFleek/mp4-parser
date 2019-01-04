#!/usr/bin/python3
import cv2

cap = cv2.VideoCapture("testfiles/test.mp4")
i = 0
while(i < 180):
	ret, frame = cap.read()
	#cv2.imshow('frame', gray)
	print("Frame " + str(i))	
	i += 1
	cv2.imwrite("testfiles/frameout/frame"+ str(i) + ".jpg", frame)
	if not cv2.waitKey(10):
		break

cap.release()
cv2.destroyAllWindows()
