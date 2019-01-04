#!/usr/bin/python3
import cv2

cap = cv2.VideoCapture("testfiles/test.mp4")
i = 0
length = 180
avg_color = [0 ,0 ,0]
while(i < length):
	acc_color = [0, 0, 0]
	ret, frame = cap.read()
	#print("Frame " + str(i))	
	i += 1
	#cv2.imwrite("testfiles/frameout/frame"+ str(i) + ".jpg", frame)
	for x in range(frame.shape[0]):
		for y in range(frame.shape[1]):
			acc_color[0] += frame[x][y][0]
			acc_color[1] += frame[x][y][1]
			acc_color[2] += frame[x][y][2]
#	print(acc_color)
	j = frame.shape[0] * frame.shape[1]
	avg_color[0] += acc_color[0] / (length * j)
	avg_color[1] += acc_color[1] / (length * j)
	avg_color[2] += acc_color[2] / (length * j)
#	print(avg_color)

print(avg_color)
cap.release()
cv2.destroyAllWindows()
