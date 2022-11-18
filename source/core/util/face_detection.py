import cv2 as opencv

image = opencv.imread("../../assets/Faces/scientists/physics.jpeg")

def main():
    recognizeFace()


def recognizeFace():
    opencv.imshow("Face detection", image)

    haarCascade = opencv.CascadeClassifier('haar_face.xml')
    facesRect = haarCascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors=1)
    print(len(facesRect))

    for (x,y,w,h) in facesRect:
        opencv.rectangle(image, (x,y),(x+w,y+h),(0,255,0),thickness=1)

    opencv.imshow("Detected Face", image)
    opencv.waitKey(0)


    

main(),