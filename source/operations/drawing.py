import cv2 as opencv
import numpy

blank = numpy.zeros((500,500,3), dtype='uint8')
  
def drawCircle():
  circleImage = opencv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40,(40,100,255), thickness=-1)
  opencv.imshow('Circle image', circleImage)
  opencv.waitKey(0)
  
  
def typeOnImage():
  textImage =  opencv.putText(blank, 'Hello, world!',(225,225),opencv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0))
  opencv.imshow('Text Image', textImage)
  opencv.waitKey(0)
  
  
def drawRectangle():
  rectangleImage = opencv.rectangle(blank, (0,0), (255,500), (0, 0, 255 ), thickness=opencv.FILLED)
  opencv.imshow('Rectange Drawed Imaged', rectangleImage)
  opencv.waitKey(0)
  
  
def drawLine():
  lineImage =  opencv.line(blank,(100,0), (blank.shape[1]//2, blank.shape[0]//2),(40,50,255), thickness=3)
  opencv.imshow('Line Image', lineImage)
  opencv.waitKey(0)
  
  
    




