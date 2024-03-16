import cv2
import numpy as np

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,QSlider
from PyQt6.QtCore import QSize, Qt
import sys


class WindowDriver(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../ui/mainwindow.ui",self)

        self.setWindowTitle('Slider Color Application')

        self.lower_h_sld.valueChanged.connect(self.get_sliders_change_lower_h)
        self.lower_s_sld.valueChanged.connect(self.get_sliders_change_lower_s)
        self.lower_v_sld.valueChanged.connect(self.get_sliders_change_lower_v)

        self.up_h_sld.valueChanged.connect(self.get_sliders_change_up_h)
        self.up_s_sld.valueChanged.connect(self.get_sliders_change_up_s)
        self.up_v_sld.valueChanged.connect(self.get_sliders_change_up_v)



    def get_sliders_change_lower_h(self):
        self.lower_h_num.display(self.lower_h_sld.value())

    def get_sliders_change_lower_s(self):
        self.lower_s_num.display(self.lower_s_sld.value())

    def get_sliders_change_lower_v(self):
        self.lower_v_num.display(self.lower_v_sld.value())
    
    def get_sliders_change_up_h(self):
        self.up_h_num.display(self.up_h_sld.value())

    def get_sliders_change_up_s(self):
        self.up_s_num.display(self.up_s_sld.value())

    def get_sliders_change_up_v(self):
        self.up_v_num.display(self.up_v_sld.value())

app = QApplication(sys.argv)

window = WindowDriver()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

#app.exec()



# recuperer une image
# img = cv2.imread("../Doc/niryo.jpg")

# # Afficher une image 
# cv2.imshow("Image de niryo", img)

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


# best values found : (92,127,91) , (122,252,171) 
cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    Lower_H = window.lower_h_sld.value()
    Lower_S = window.lower_s_sld.value()
    Lower_V = window.lower_v_sld.value()

    Up_H = window.up_h_sld.value()
    Up_S = window.up_s_sld.value()
    Up_V = window.up_v_sld.value()

    lower_color = np.array([Lower_H,Lower_S,Lower_V])
    upper_color = np.array([Up_H,Up_S,Up_V])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF # Button ESC
    if k == 27:
        break

cv2.destroyAllWindows()
    