import cv2 as opencv
import numpy

def draw():
  blank = numpy.zeros((500,500,3), dtype='uint8')
  image = opencv.imread('../assets/photos/cat.jpg')
  
  # opencv.imshow('Cat', image)
  # opencv.imshow('Blank Image', blank)
  rectangleImage = opencv.rectangle(blank, (0,0), (255,500), (0, 0, 255 ), thickness=opencv.FILLED)
  opencv.imshow('Rectange Drawed Imaged', rectangleImage)
  circleImage = opencv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40,(40,100,255),thickness=-1)
  opencv.imshow('Circle image', circleImage)
  
  lineImage =  opencv.line(blank,(100,0), (blank.shape[1]//2, blank.shape[0]//2),(40,50,255),thickness=3)
  opencv.imshow('Line Image', lineImage)
  
  textImage =  opencv.putText(blank, 'Hello, world!',(225,225),opencv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0))
  opencv.imshow('Text Image', textImage)
  
  
  
  
  opencv.waitKey(0)


draw()
