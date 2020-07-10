import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('1.jpg')
frame = cv2.imread('1.jpg')

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_blue = np.array([60, 40, 40])
upper_blue = np.array([150, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
edges = cv2.Canny(mask, 200, 400)


def detect_edges(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    show_image("hsv", hsv)
    lower_blue = np.array([60, 40, 40])
    upper_blue = np.array([150, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    show_image("blue mask", mask)
    edges = cv2.Canny(mask, 200, 400)
    return edges


def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)
    # only focus bottom half of the screen
    polygon = np.array([[
        (400,470),
        (870,470),
        (1127,720),
        (195,720),
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)
    return cropped_edges


cropped_edges = region_of_interest(edges)


def detect_line_segments(cropped_edges, frame ):

    # tuning min_threshold, minLineLength, maxLineGap is a trial and error process by hand
    rho = 1 # distance precision in pixel, i.e. 1 pixel
    angle = np.pi / 180 # angular precision in radian, i.e. 1 degree
    min_threshold = 10 # minimal of votes
    line_segments = cv2.HoughLinesP(cropped_edges, rho, angle, min_threshold,np.array([]), minLineLength=1, maxLineGap=20)

    for line in line_segments:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0,255,0), 3)
    #img8 = (line_segments/256).astype('uint8')
    return line_segments


line_segments = detect_line_segments(cropped_edges, frame )


print(frame.dtype)
print(frame.shape)
print(cropped_edges.dtype)
print(line_segments.dtype)

cv2.imshow("img", image)
cv2.waitKey()
cv2.imshow("img", hsv)
cv2.waitKey()
cv2.imshow("img", mask)
cv2.waitKey()
cv2.imshow("img", edges)
cv2.waitKey()
cv2.imshow("img", cropped_edges)
cv2.waitKey()
cv2.imshow("img", frame)
cv2.waitKey()

plt.figure(figsize=(50, 50))
plt.subplot(161)
plt.imshow(frame);
plt.title("Frame")
plt.subplot(162)
plt.imshow(hsv);
plt.title("Frame")
plt.subplot(163)
plt.imshow(mask);
plt.title("Frame")
plt.subplot(164)
plt.imshow(edges);
plt.title("Frame")
plt.subplot(165)
plt.imshow(cropped_edges);
plt.title("Frame")
plt.subplot(166)
plt.imshow(line_segments);
plt.title("Frame")
plt.show()