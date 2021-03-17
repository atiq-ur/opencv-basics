#In this part i wanna show how read a video using path or camera
#at first we need to import opencv
import cv2 as cv

#cap = cv.VideoCapture('videos/dog.mp4')
#VideoCapture is a method that's responsible for capturing video
#either from location or any camera
#for web cam or any camera attached with pc, then
cap = cv.VideoCapture(0)
# 0 refers your default web cam, it can be 1, 2, 3, or more with respect to
#first camera, sec camera, and so

#keep in mind opencv read video frame by frame that's why
#for reading video need a lop, for this case we should use while loop

while True:
    _, frame = cap.read() #isSuccess means the frame is successfully read or not

    #then show the frame as like as an image, that we have covered in last part

    cv.imshow('Video Window', frame) #window name and what should display

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


    # as we know waitKey() refers how long window will be displayed 1 means continue
    # 0xFF == ord('q') refers if q press from the keyboard then break from the while loop

#after that we should need to release the capture and destroy all the window what cv took

cap.release()
cv.destroyAllWindows()
