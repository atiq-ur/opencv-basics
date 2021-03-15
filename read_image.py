# import library which is opencv-contrib-python that refers computer vision
import cv2 as cv
# lets read an image using cv
img = cv.imread('images/cat_dark.jpeg')

# details what exactly have done by imread()
# imread takes an argument in this case image which takes the pixels of the image
# and then store the pixels value in img variable
# now it's time to show the imgage that we have read using imread() function

cv.imshow('Output', img)
# imshow shows the pixels as an image which was read by imread() function
# it expects two arguments one is window name and another one is pixels value here is an img

cv.waitKey(0)
# here i'm writing cv.waitkey and it expects an integer value like 0,1,2,3...
# waitKey is used for how many time window will apear on screen it can be 20s
# after 20 sec the window will disapear
# i have written 0 that refers infinite time
