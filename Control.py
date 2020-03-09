import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFile, QByteArray
from MainWindow import *

from ImageProcess import *
from Choice import *
from CompleteImage import *
from Practice import *

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
    

class CompleteImageWindow(QDialog,Ui_CompleteImage):
    def __init__(self):
        super(CompleteImageWindow, self).__init__()
        self.setupUi(self)
        self.pushButtonQL.clicked.connect(self.PressQL)
        self.pushButtonBH.clicked.connect(self.PressBH)
        self.pushButtonZQ.clicked.connect(self.PressZQ)
        self.pushButtonXW.clicked.connect(self.PressXW)
    def PressQL(self):
        self.graphicsView1.setStyleSheet("border-image: url(:/star/QL1.jpg);")
        self.graphicsView2.setStyleSheet("border-image: url(:/star/QL2.jpg);")
        self.graphicsView3.setStyleSheet("border-image: url(:/star/QL3.jpg);")

    def PressBH(self):
        self.graphicsView1.setStyleSheet("border-image: url(:/star/BH1.jpg);")
        self.graphicsView2.setStyleSheet("border-image: url(:/star/BH2.jpg);")
        self.graphicsView3.setStyleSheet("border-image: url(:/star/BH3.jpg);")

    def PressZQ(self):
        self.graphicsView1.setStyleSheet("border-image: url(:/star/ZQ1.jpg);")
        self.graphicsView2.setStyleSheet("border-image: url(:/star/ZQ2.jpg);")
        self.graphicsView3.setStyleSheet("border-image: url(:/star/ZQ3.jpg);")

    def PressXW(self):
        self.graphicsView1.setStyleSheet("border-image: url(:/star/XW1.jpg);")
        self.graphicsView2.setStyleSheet("border-image: url(:/star/XW2.jpg);")
        self.graphicsView3.setStyleSheet("border-image: url(:/star/XW3.jpg);")


class ChoiceWindow(QDialog,Ui_ChoiceWindow):
    def __init__(self):
        super(ChoiceWindow, self).__init__()
        self.setupUi(self)
        self.pushButtonQL.clicked.connect(self.PracitceQL)
        self.pushButtonBH.clicked.connect(self.PracitceBH)
        self.pushButtonZQ.clicked.connect(self.PracitceZQ)
        self.pushButtonXW.clicked.connect(self.PracitceXW)

    def PracitceQL(self):
        score = 0
        wrong = 0
        right = 0
        self.lineEditScore.setText(str(0))
        self.lineEditRight.setText(str(0))
        self.lineEditWrong.setText(str(0))
        for num in range(5):
            img = ImgProcess()
            randNum = random.randint(1, 3)
            file = QFile(":/star/QL" + str(randNum) + ".jpg")
            if not file.open(QFile.ReadOnly):
                QMessageBox.warning(self, self.tr("Application"),
                                    self.tr("Cannot read file %1:n%2.").arg(fileName).arg(file.errorString()))
                return
            else:
                imgArray = file.readAll()

            img.importImg(imgArray)
            img.thresholdImg()
            img.findPoints()
            randPoint = random.randrange(len(img.posArray))
            circleImg = cv2.circle(img.colorImg, img.posArray[randPoint][0], img.posArray[randPoint][1] + 3, (255,255,255), -1)
            img.showImg("StarSeeker", circleImg)
            img.posJudge("StarSeeker", circleImg, img.posArray[randPoint][0], img.posArray[randPoint][1])
            while (1):
                img.showImg("StarSeeker", circleImg)
                if img.next:
                    if img.flag:
                        right += 1
                        if img.click == 1:
                            score += 20
                        elif img.click == 2:
                            score += 10
                        elif img.click == 3:
                            score += 5
                        self.lineEditScore.setText(str(score))
                        self.lineEditRight.setText(str(right))
                    else:
                        wrong += 1
                        self.lineEditWrong.setText(str(wrong))

                    break
                if cv2.waitKey(20) & 0xFF == 27:
                    esc = 1
                    break

    def PracitceBH(self):
        score = 0
        wrong = 0
        right = 0
        self.lineEditScore.setText(str(0))
        self.lineEditRight.setText(str(0))
        self.lineEditWrong.setText(str(0))
        for num in range(5):
            img = ImgProcess()
            randNum = random.randint(1, 3)
            file = QFile(":/star/BH" + str(randNum) + ".jpg")
            if not file.open(QFile.ReadOnly):
                QMessageBox.warning(self, self.tr("Application"),
                                    self.tr("Cannot read file %1:n%2.").arg(fileName).arg(file.errorString()))
                return
            else:
                imgArray = file.readAll()

            img.importImg(imgArray)
            img.thresholdImg()
            img.findPoints()
            randPoint = random.randrange(len(img.posArray))
            circleImg = cv2.circle(img.colorImg, img.posArray[randPoint][0], img.posArray[randPoint][1] + 2,
                                   (255, 255, 255), -1)
            img.showImg("StarSeeker", circleImg)
            img.posJudge("StarSeeker", circleImg, img.posArray[randPoint][0], img.posArray[randPoint][1])
            while (1):
                img.showImg("StarSeeker", circleImg)
                if img.next:
                    if img.flag:
                        right += 1
                        if img.click == 1:
                            score += 20
                        elif img.click == 2:
                            score += 10
                        elif img.click == 3:
                            score += 5
                        self.lineEditScore.setText(str(score))
                        self.lineEditRight.setText(str(right))
                    else:
                        wrong += 1
                        self.lineEditWrong.setText(str(wrong))

                    break
                if cv2.waitKey(20) & 0xFF == 27:
                    esc = 1
                    break
    def PracitceZQ(self):
        score = 0
        wrong = 0
        right = 0
        self.lineEditScore.setText(str(0))
        self.lineEditRight.setText(str(0))
        self.lineEditWrong.setText(str(0))
        for num in range(5):
            esc = 0
            img = ImgProcess()
            randNum = random.randint(1, 3)
            file = QFile(":/star/ZQ" + str(randNum) + ".jpg")
            if not file.open(QFile.ReadOnly):
                QMessageBox.warning(self, self.tr("Application"),
                                    self.tr("Cannot read file %1:n%2.").arg(fileName).arg(file.errorString()))
                return
            else:
                imgArray = file.readAll()

            img.importImg(imgArray)
            img.thresholdImg()
            img.findPoints()
            randPoint = random.randrange(len(img.posArray))
            circleImg = cv2.circle(img.colorImg, img.posArray[randPoint][0], img.posArray[randPoint][1] + 2,
                                   (255, 255, 255), -1)
            img.showImg("StarSeeker", circleImg)
            img.posJudge("StarSeeker", circleImg, img.posArray[randPoint][0], img.posArray[randPoint][1])
 #           if (~cvGetWindowHandle("StarSeeker")):
  #              cv2.destroyAllWindows()
 #               break
            while (1):
                img.showImg("StarSeeker", circleImg)
                if img.next:
                    if img.flag:
                        right += 1
                        if img.click == 1:
                            score += 20
                        elif img.click == 2:
                            score += 10
                        elif img.click == 3:
                            score += 5
                        self.lineEditScore.setText(str(score))
                        self.lineEditRight.setText(str(right))
                    else:
                        wrong += 1
                        self.lineEditWrong.setText(str(wrong))

                    break
                if cv2.waitKey(20) & 0xFF == 27:

                    esc = 1
                    break
 #               if (~cvGetWindowHandle("StarSeeker")):
 #                   cv2.destroyAllWindows()
 #                   break


    def PracitceXW(self):
        score = 0
        wrong = 0
        right = 0
        self.lineEditScore.setText(str(0))
        self.lineEditRight.setText(str(0))
        self.lineEditWrong.setText(str(0))
        for num in range(5):
            img = ImgProcess()
            randNum = random.randint(1, 3)
            file = QFile(":/star/XW" + str(randNum) + ".jpg")
            if not file.open(QFile.ReadOnly):
                QMessageBox.warning(self, self.tr("Application"),
                                    self.tr("Cannot read file %1:n%2.").arg(fileName).arg(file.errorString()))
                return
            else:
                imgArray = file.readAll()

            img.importImg(imgArray)
            img.thresholdImg()
            img.findPoints()
            randPoint = random.randrange(len(img.posArray))
            circleImg = cv2.circle(img.colorImg, img.posArray[randPoint][0], img.posArray[randPoint][1] + 2,
                                   (255, 255, 255), -1)
            img.showImg("StarSeeker", circleImg)
            img.posJudge("StarSeeker", circleImg, img.posArray[randPoint][0], img.posArray[randPoint][1])
            while (1):
                img.showImg("StarSeeker", circleImg)
                if img.next:
                    if img.flag:
                        right += 1
                        if img.click == 1:
                            score += 20
                        elif img.click == 2:
                            score += 10
                        elif img.click == 3:
                            score += 5
                        self.lineEditScore.setText(str(score))
                        self.lineEditRight.setText(str(right))
                    else:
                        wrong += 1
                        self.lineEditWrong.setText(str(wrong))

                    break
                if cv2.waitKey(20) & 0xFF == 27:
                    esc = 1
                    break
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    CompleteImageWin = CompleteImageWindow()
    ChoiceWin = ChoiceWindow()
    mainWin.pushButtonPractice.clicked.connect(ChoiceWin.show)
    mainWin.pushButtonCImage.clicked.connect(CompleteImageWin.show)
    mainWin.show()

    sys.exit(app.exec_())