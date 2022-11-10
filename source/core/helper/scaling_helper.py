import cv2 as opencv

def rescaleImage(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return opencv.resize(frame, dimensions, interpolation=opencv.INTER_AREA)


# Change resolution method only work for live videos.
def changeResolution(width, heigth, capturedVideo):
    capturedVideo.set(3, width)
    capturedVideo.set(4, heigth)
    pass