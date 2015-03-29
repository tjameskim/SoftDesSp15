import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
kernel = np.ones((21,21),'uint8')

while(True):
	
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for (x,y,w,h) in faces:
		#frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
		#draw the mouth
		#cv2.circle(frame,(int(x+.5*w),int(y+.75*h)),int(1./8*w),(0,0,255),-1)
		#cv2.ellipse(frame,(int(x+.5*w),int(y+.85*h)),(x,y,x+w,y+h),(0,0,0),8)
		#draw the eyes
		#cv2.line(frame,(int(x+1./8*w),int(y+1./4*h)), (int(x+3./8*w),int(y+1./4*h)),(0,0,0),5,8,0)
		#cv2.line(frame,(int(x+5./8*w),int(y+1./4*h)), (int(x+7./8*w),int(y+1./4*h)),(0,0,0),5,8,0)
	 # Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()