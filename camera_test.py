# import packages
import cv2

CAMERA_NUMBERS = [1, 2, 4 ,6, 8, 77, 100, 0]
yes_open = []


# 1. open the camera

for i in CAMERA_NUMBERS:
    camera = cv2.VideoCapture(i)
    if  camera.isOpened():
        print(f"camera open:[{i}]")
        yes_open.append(i)
    else:
        print(f"no response[{i}]")
        



# 2. loop 
#        take a frame from the camera 
#        display the frame in a window
#        check if the user want to exit the loop  
# 3. close the camera and window