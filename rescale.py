import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #work for video , img
    width = int(frame.shape[1] * scale)
    hieght = int(frame.shape[0] * scale)

    dimensions = (width,hieght)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#reading img / rescaling
img = cv.imread('Photos/cat.jpg')

resized_image = rescaleFrame(img)

cv.imshow('Cat',img)
cv.imshow('Image', resized_image)

cv.waitKey(0)

#work only for live video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

#reading video / Rescaleing video
capture = cv.VideoCapture('Videos/dog.mp4')  #(0or1) refrence camera

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()