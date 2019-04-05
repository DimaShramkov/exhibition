import sys
from PyQt5 import QtCore, QtGui, QtWidgets


from vievs.viev import View
#from Model.modulVideo import modulVideo
from PyQt5.QtGui import QPixmap

class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)

        #self._model = modulVideo()
        self._view = View()
        self.init()

    def init(self):
        self._view.onMonitor1Signal.connect(self.pushButtonM1Yes)
        self._view.onMonitor2Signal.connect(self.pushButtonM2Yes)
        self._view.onMonitor3Signal.connect(self.pushButtonM3Yes)
        #self._view.onClick.connect(self.onClickButton)
        self._view.offMonitor1Signal.connect(self.pushButtonM1No)
        self._view.offMonitor2Signal.connect(self.pushButtonM2No)
        self._view.offMonitor3Signal.connect(self.pushButtonM3No)
        self._view.onProjectorSignal.connect(self.pushButtonOn)
        self._view.offProjectorSignal.connect(self.pushButtonOff)
        self._view.onAllMonitorSignal.connect(self.pushButtonAllMOn)
        self._view.offAllMonitorSignal.connect(self.pushButtonAllMOff)

       #self._view.stopButtonSignal.connect(self.buttonStop)

        #self._model.frameSignal.connect(self.test, QtCore.Qt.QueuedConnection)

    def pushButtonOn(self):
        self.run_projector(self)
        print("Проектор включён")

    def pushButtonOff(self):
        self.stop_projector(self)
        print("Проектор выключен")

    def pushButtonM1Yes(self):
        self.run_monitor1(self)
        print("Монитор №1 включён")

    def pushButtonM1No(self):
        self.stop_monitor1(self)
        print("Монитор №1 выключен")

    def pushButtonM2Yes(self):
        self.run_monitor2(self)
        print("Монитор №2 включён")
        #print(self._view.text

    def pushButtonM2No(self):
        self.stop_monitor2(self)
        print("Монитор №2 выключен")

    def pushButtonM3Yes(self):
        self.run_monitor3(self)
        print("Монитор №3 включён")

    def pushButtonM3No(self):
        self.stop_monitor3(self)
        print("Монитор №3 выключен")

    def pushButtonAllMOn(self):
        self.run_video(self)
        print("Все мониторы включены")

    def pushButtonAllMOff(self):
        self.stop_video(self)
        print("Все мониторы выключены")

    def run(self):
        self._view.show()
        return self._app.exec_()

        #self._view.pushButtonM1Yes.connect(self.onClickButton)
    #def offProjector(self):
