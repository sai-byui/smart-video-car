import cv2
import matplotlib.pyplot as plt
import numpy as np

frame = cv2.imread('1.jpg')



hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_blue = np.array([60, 40, 40])
upper_blue = np.array([150, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
edges = cv2.Canny(mask, 200, 400)

def detect_edges(frame):
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    show_image("hsv", hsv)
    lower_blue=np.array([60, 40, 40])
    upper_blue=np.array([150, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    show_image("blue mask", mask)
    edges = cv2.Canny(mask, 200, 400)
    return edges

def region_of_interest(edges):
    height, width=edges.shape
    mask = np.zeros_like(edges)
    # only focus bottom half of the screen
    polygon = np.array([[
        (0, height * 1/2),
        (width, height * 1 / 2),
        (width, height),
        (0, height),
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)
    return cropped_edges



print(frame.dtype)
print(frame.shape)
cv2.imshow("img", frame)
cv2.imshow("img", hsv)
cv2.imshow("img", mask)
cv2.imshow("img", edges)
#cv2.imshow("img", cropped_edges)
cv2.waitKey()
