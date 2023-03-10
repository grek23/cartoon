import cv2 as cv
import numpy as np


def main():
    print("Lets make a cartoon!")
    print(cv.__version__)

    img = cv.imread("selfie04.png")

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)

    edges = cv.adaptiveThreshold(
        gray, 255,
        cv.ADAPTIVE_THRESH_MEAN_C,
        cv.THRESH_BINARY, 9, 9)

    color = cv.bilateralFilter(img, 9, 250, 250)
    cartoon = cv.bitwise_and(color, color, mask=edges)

    cv.imshow("image", img)
    cv.imshow("edges", edges)
    cv.imshow("cartoon", cartoon)
    cv.waitKey(0)

    # cv.destroyWindow("image")
    # cv.destroyWindow("edges")


if __name__ == '__main__':
    main()
