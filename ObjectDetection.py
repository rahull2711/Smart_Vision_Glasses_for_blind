import cv2
import numpy as np
import os
import threading
from assistant import speak

class Avoid_obstacles:
    def __init__(self):
        print("Initializing the Obstacles Avoidance")
        self.testmode = 2
        self.key = ''
        self.stop_helpping = False

    def forward(self):
        print("No obstacles detected")
        speak("No obstacles detected")

    def backward(self):
        print("This is a closed way, go back please!")
        speak("This is a closed way, go back please!")

    def right(self):
        print("go slightly to the right please!")
        speak("go slightly to the right please!")

    def left(self):
        print("go slightly to the left please!")
        speak("go slightly to the left please!")

    def stop(self):
        print("Stop Helping you")
        speak("Stop Helping you")

    def calc_dist(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        dist = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(dist)
        return dist

    def getChunks(self, l, n):
        a = []
        for i in range(0, len(l), n):
            a.append(l[i:i + n])
        return a

    def Avoid(self, camp_port):
        cap = cv2.VideoCapture(camp_port)
        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print('Error: Creating directory of data')

        StepSize = 5
        currentFrame = 0

        if self.testmode == 1:
            self.F = open("./data/imagedetails.txt", 'a')
            self.F.write("\n\nNew Test \n")

        while not self.stop_helpping:
            print(self.stop_helpping)
            _, frame = cap.read()
            name = './data/frame' + str(currentFrame) + '.jpg'
            img = frame.copy()
            blur = cv2.bilateralFilter(img, 9, 40, 40)
            edges = cv2.Canny(blur, 50, 100)
            img_h = img.shape[0] - 1
            img_w = img.shape[1] - 1
            EdgeArray = []

            for j in range(0, img_w, StepSize):
                pixel = (j, 0)
                for i in range(img_h - 5, 0, -1):
                    if edges.item(i, j) == 255:
                        pixel = (j, i)
                        break
                EdgeArray.append(pixel)

            for x in range(len(EdgeArray) - 1):
                cv2.line(img, EdgeArray[x], EdgeArray[x + 1], (0, 255, 0), 1)

            for x in range(len(EdgeArray)):
                cv2.line(img, (x * StepSize, img_h), EdgeArray[x], (0, 255, 0), 1)

            chunks = self.getChunks(EdgeArray, int(len(EdgeArray) / 3))
            c = []

            for i in range(len(chunks) - 1):
                x_vals = []
                y_vals = []
                for (x, y) in chunks[i]:
                    x_vals.append(x)
                    y_vals.append(y)
                avg_x = int(np.average(x_vals))
                avg_y = int(np.average(y_vals))
                c.append([avg_y, avg_x])

            cv2.line(frame, (320, 480), (avg_x, avg_y), (255, 0, 0), 2)
            forwardEdge = c[1]
            print(forwardEdge)
            cv2.line(frame, (320, 480), (forwardEdge[1], forwardEdge[0]), (0, 255, 0), 3)
            cv2.imwrite(name, frame)
            y = min(c)
            print("y =", y)

            if forwardEdge[0] > 250:
                if y[1] < 310:
                    self.left()
                    direction = "left "
                else:
                    self.right()
                    direction = "right "
            else:
                self.forward()
                direction = "forward "

            if self.testmode == 1:
                self.F.write("frame" + str(currentFrame) + ".jpg" + " | " +
                             str(c[0]) + " | " + str(c[1]) + " | " + str(c[2]) + " | " + direction + "\n")
            currentFrame += 1

            if self.testmode == 2:
                cv2.imshow("frame", frame)
                k = cv2.waitKey(5) & 0xFF
                if k == 27:
                    self.stop_help()
                    break

        if self.stop_helpping:
            self.stop()
        cv2.destroyAllWindows()
        cap.release()

    def stop_help(self):
        self.stop_helpping = True

a = Avoid_obstacles()
a.Avoid(0)
