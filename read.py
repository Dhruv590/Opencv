import cv2 as cv

#reading images 

img = cv.imread('photos/cat 1.jpg')
cv.imshow('cat',img)
cv.waitKey(0)

#reading video 
capture = cv.VideoCapture('video/dog.mp4')  #(0or1) refrence camera

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()



