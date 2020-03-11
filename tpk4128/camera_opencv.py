import numpy as np
import cv2 as cv


class Camera(object):

    def __init__(self):

        # Implement this constructor that opens a webcam and stores it in self._camera
        self._camera = cv.VideoCapture(0)
        if not self._camera.isOpened():
            print("Not able to open camera")
            exit()


    def capture(self):

        # Implement this function that grabs an image from the webcam and returns a numpy array
        ret, img = self._camera.read()
        if not ret:
            print("Error reading from camera")
            
        return img

    def __del__(self):

        # Implement this destructor. Remember to free the camera.
        self._camera.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    cam = Camera()
    while True:
        img = cam.capture()
        print(len(img.tostring()), img.dtype, img.shape)
        cv.imshow("image", img)
        cv.waitKey(1)

