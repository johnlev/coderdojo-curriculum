import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Week8.Sorter_activity import Sorter

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Sorting Visualizer'
        self.width = 550
        self.height = 750
        self.fragDimension = 50

        self.pixmap = QPixmap("res/catimage.jpg")
        self.sorter = Sorter(self, self.pixmap.width(), self.pixmap.height(), self.fragDimension)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.centerFrame()

        self.shuffleButton = QPushButton('Shuffle', self)
        self.shuffleButton.setToolTip('Shuffle the pixels of the Image')
        self.shuffleButton.move(25, 550)
        self.shuffleButton.clicked.connect(self.sorter.shuffleImage)

        self.bubbleSortButton = QPushButton('BubbleSort', self)
        self.bubbleSortButton.setToolTip('Start a bubble sort of the image')
        self.bubbleSortButton.move(25, 580)
        self.bubbleSortButton.clicked.connect(self.sorter.bubblesort)

        self.mergeSortButton = QPushButton('MergeSort', self)
        self.mergeSortButton.setToolTip('Start a merge sort of the image')
        self.mergeSortButton.move(25, 610)
        self.mergeSortButton.clicked.connect(self.sorter.mergesort)

    def centerFrame(self):
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

    def enableButtons(self):
        self.shuffleButton.setEnabled(True)
        self.bubbleSortButton.setEnabled(True)
        self.mergeSortButton.setEnabled(True)

    def disableButtons(self):
        self.shuffleButton.setEnabled(False)
        self.bubbleSortButton.setEnabled(False)
        self.mergeSortButton.setEnabled(False)

    # An event-based paint method that is called each time an App.update() in called.
    # This redraws the shuffled image on the window based on the current state of self.sorter.
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        fragWidth = self.pixmap.width() / self.fragDimension
        fragHeight = self.pixmap.height() / self.fragDimension
        for y in range(self.fragDimension):
            for x in range(self.fragDimension):
                srcTuple = self.sorter.getSubpixmapTuple(x + y * self.fragDimension)
                painter.drawPixmap(25 + (x * fragWidth), 25 + (y * fragHeight), fragWidth, fragHeight, self.pixmap,
                                   srcTuple[0], srcTuple[1], srcTuple[2], srcTuple[3])
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
