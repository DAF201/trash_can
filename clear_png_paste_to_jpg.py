#this is for human facedet use
import cv2
from PIL import Image
import numpy
import PyFaceDet
cap = cv2.VideoCapture(0)
covered = cv2.imread(r"Front_pic_path", cv2.IMREAD_UNCHANGED)
cv2.resize(covered,(600,600))
b, g, r, a = cv2.split(covered)
foreground = cv2.merge((b, g, r))
alpha = cv2.merge((a, a, a))
ret, alpha = cv2.threshold(alpha, 254, 1, cv2.THRESH_BINARY)
foreground = cv2.multiply(alpha, foreground)
ret,background=cap.read()
position=PyFaceDet.facedetectcnn.facedetect_cnn(background)
background=cv2.flip(background,1)
background_temp = background[position[0][0]:position[0][0]+foreground.shape[0], position[0][1]:position[0][1]+foreground.shape[1], :]
cv2.imshow('pic',background_temp)
background_temp = cv2.multiply(1-alpha, background_temp)
outImage = foreground + background_temp
image = Image.fromarray(cv2.cvtColor(outImage, cv2.COLOR_BGR2RGB))
# image.show()
background=Image.fromarray(cv2.cvtColor(background, cv2.COLOR_BGR2RGB))
if position!=[]:
    background.paste(image,(position[0][0],position[0][1]),None)
    background = cv2.cvtColor(numpy.asarray(background),cv2.COLOR_RGB2BGR)  
cv2.imshow("OpenCV",background)  
cv2.waitKey()
