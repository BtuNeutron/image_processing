import cv2 as opencv
# from core.helper import scaling_helper as scaleHelper


def readImage():
  # Read image from asset.
  catImage = opencv.imread('assets/photos/cat.jpg')
  
  # Show the image you read before.
  opencv.imshow('Cat', catImage)
  
  # Wait for pressing any key to close imaged window opened.
  opencv.waitKey(0)
  
  

def captureVideo():
  capture = opencv.VideoCapture('./assets/videos/dog.mp4')

  while True:
      isTrue, frame = capture.read()
      
      # if opencv.waitKey(20) & 0xFF==ord('d'):
      # This is the preferred way - if `isTrue` is false (the frame could 
      # not be read, or we're at the end of the video), we immediately
      # break from the loop. 
      if isTrue:    
          opencv.imshow('Video', frame)
          if opencv.waitKey(20) & 0xFF==ord('d'):
              break            
      else:
          break

  capture.release()
  opencv.destroyAllWindows()


captureVideo()