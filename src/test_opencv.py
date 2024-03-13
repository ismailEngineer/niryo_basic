import cv2
import numpy as np

# recuperer une image
img = cv2.imread("../Doc/niryo.jpg")

# Afficher une image 
cv2.imshow("Image de niryo", img)

# k = cv2.waitKey(0)


# cap = cv2.VideoCapture(0)

 
# # Read the entire file until it is completed 
# while(cap.isOpened()): 
#   # Capture each frame 
#     ret, frame = cap.read() 
#     if ret == True: 
#         # Display the resulting frame
#         cv2.imshow("Image de niryo", frame)

#     if cv2.waitKey(25) & 0xFF == ord('q'): 
#             print(frame)
#             break



cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
    