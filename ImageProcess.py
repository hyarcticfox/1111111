import cv2
import numpy as np
from datetime import datetime
import random


txtFont = cv2.FONT_HERSHEY_DUPLEX   #normal size sans-serif font (more complex than FONT_HERSHEY_SIMPLEX)



class ImgProcess:

    def __init__(self):
        self.colorImg = []
        self.binaryImg = []
        self.posArray = []
        self.fx = self.fy = 1.8
        self.cretria = 15
        self.threshold = 200
        self.click = 0
        self.flag = False
        self.next = False
    def importImg(self, array):
        self.colorImg = cv2.imdecode(np.asarray(array), cv2.IMREAD_COLOR)  # 地址不能带中文
        self.colorImg = cv2.resize(self.colorImg, (int(self.colorImg.shape[1] * self.fy), int(self.colorImg.shape[0] *  self.fx)), cv2.INTER_NEAREST)

    def thresholdImg(self):
        grayImg = cv2.cvtColor(self.colorImg, cv2.COLOR_BGR2GRAY)  # 灰度化
        minVal = np.min(grayImg)
        ret, self.binaryImg = cv2.threshold(grayImg, self.threshold, 255, cv2.THRESH_BINARY_INV)
    def findPoints(self):
        contours, hierarchy = cv2.findContours(self.binaryImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for i in range(len(contours)):
            (x, y), radius = cv2.minEnclosingCircle(contours[i])
            center = (int(x), int(y))
            radius = int(radius)
            self.posArray.append([center, radius])
    def showImg(self,title,img):
        cv2.imshow(title, img)
    def __mouse_click(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # 左边鼠标点击
            self.click += 1
            if self.click < 4:
                cv2.circle(param[0], (x, y), param[1], (0, 0, 255), -1)
                if np.square(x-param[2][0]) + np.square(y-param[2][1]) < np.square(self.cretria):
                    #cv2.putText(param[0], "Right", org = (int(param[0].shape[0]/3), int(param[0].shape[1]/3)), fontFace= txtFont,
                    #          fontScale= 0.8, color = (0,0,255), thickness = 2)
                    self.flag = True
                    self.next = True
                else:
                   cv2.putText(param[0], "Wrong", org=(int(param[0].shape[0] / 3), int(param[0].shape[1] / 3)), fontFace=txtFont,
                           fontScale=0.8, color=(0, 0, 255), thickness=2)
            else:
                self.click = 0
                self.next = True

    def posJudge(self, title, img, center, radius):
        cv2.setMouseCallback(title, self.__mouse_click,
                             param=[img, radius, center])
def getTime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    img = ImgProcess()
    img.importImg("./star/QL1.jpg")

    img.thresholdImg()
    img.findPoints()
    randNum = random.randrange(len(img.posArray))
    circleImg = cv2.circle(img.colorImg, img.posArray[randNum][0], img.posArray[randNum][1] + 2, (255,255,255), -1)
    img.showImg("StarSeeker", circleImg)
    img.posJudge("StarSeeker", circleImg, img.posArray[randNum][0], img.posArray[randNum][1])
    while(1):
        img.showImg("StarSeeker", circleImg)
        if cv2.waitKey(20) & 0xFF == 27:
            break
#
#
    key = cv2.waitKey(0)
    if key == 27:
  #      writeLog()
 #       cv2.imwrite('SavePic.png', img)
  #      print('日志保存成功')
        cv2.destroyAllWindows()
 #   else:
  #      drawWords(img, chr(key))
  #
