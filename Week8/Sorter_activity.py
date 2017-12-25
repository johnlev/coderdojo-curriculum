import random
from PyQt5.QtWidgets import *

'''
This week, we have been going over algorithms in programming, which is a set of operations that executes upon an input 
and outputs a result. For a sorting algorithm, this usually involves inputting a randomly ordered array and outputting
a sorted array. Suppose that we would like to order the following array of numbers [4, 2, 6, 3, 9] from least to
greatest. For us humans, this is a simple task as we compare the numbers next to each other to place them in the 
correct order of [2, 3, 4, 6, 9]. Similarly, computers do these comparisons but must manage storing the positions, 
the previous values, and new values to these positions when sorting, a task that is automatically done without thought
for us. Hence, when coding (sorting) algorithms, each step must be coded in a logical order. For this week's activity,
you will be coding some of the various sorting algorithms to sort a shuffled image back to its original state.
This will be done within the 'Sorter_activity.py' class.
'''

class Sorter:
    def __init__(self, appWidget, width, height, fragDimension):
        self.appWidget = appWidget
        self.width = width
        self.height = height
        self.fragDimension = fragDimension

        self.subpixmapKeys = []
        self.subpixmapDict = {}
        for y in range(fragDimension):
            for x in range(fragDimension):
                self.subpixmapKeys.append(x + y * fragDimension)
                self.subpixmapDict[x + y * fragDimension] = (x * width/fragDimension, y * height/fragDimension,
                                                             width/fragDimension, height/fragDimension)

        self.bubblesortUpdateThreshold = 5000
        self.mergesortUpdateThreshold = 50
        self.count = 0

    def bubblesort(self):
        self.appWidget.disableButtons()
        self.count = 0
        for end in range(len(self.subpixmapKeys) - 1, 0, -1):
            for i in range(end):
                self.count += 1
                if self.subpixmapKeys[i] > self.subpixmapKeys[i + 1]:
                    temp = self.subpixmapKeys[i]
                    self.subpixmapKeys[i] = self.subpixmapKeys[i + 1]
                    self.subpixmapKeys[i + 1] = temp

                if(self.count >= self.bubblesortUpdateThreshold):
                    self.count = 0
                    self.redraw()

        self.redraw()
        self.appWidget.enableButtons()

    def mergesort(self):
        self.appWidget.disableButtons()
        self.count = 0
        self.mergesortHelper(0, len(self.subpixmapKeys) - 1)
        self.redraw()
        self.appWidget.enableButtons()

    def mergesortHelper(self, start, end):
        if(start != end):
            mid = int((start + end) / 2)
            leftIndices = (start, mid)
            rightIndices = (mid + 1, end)

            self.mergesortHelper(leftIndices[0], leftIndices[1])
            self.mergesortHelper(rightIndices[0], rightIndices[1])

            i = start
            j = mid + 1
            tempArray = []
            while i < mid + 1 and j < end + 1:
                if self.subpixmapKeys[i] < self.subpixmapKeys[j]:
                    tempArray.append(self.subpixmapKeys[i])
                    i += 1
                else:
                    tempArray.append(self.subpixmapKeys[j])
                    j += 1

            while i < mid + 1:
                tempArray.append(self.subpixmapKeys[i])
                i += 1
            while j < end + 1:
                tempArray.append(self.subpixmapKeys[j])
                j += 1

            for k in range(len(tempArray)):
                self.subpixmapKeys[k + start] = tempArray[k]
                self.count += 1
                if(self.count >= self.mergesortUpdateThreshold):
                    self.count = 0
                    self.redraw()

    def getSubpixmapTuple(self, index):
        if(index < len(self.subpixmapKeys)):
            return self.subpixmapDict[self.subpixmapKeys[index]]
        else:
            print('Error: Index value \'{}\' is too high'.format(index))
            exit(1)

    def shuffleImage(self):
        self.appWidget.disableButtons()
        random.shuffle(self.subpixmapKeys)
        self.appWidget.update()
        self.appWidget.enableButtons()

    def redraw(self):
        self.appWidget.update()
        QApplication.processEvents()


    # def saveImage(self):
    #     for i in range(self.width):  # for every col:
    #         for j in range(self.height):  # For every row
    #             self.imgPixels[i,j] = self.hsv2rgb(self.pixelHues[j + i * self.height] / 360.0, 1, 1)
    #
    #     self.img.save('{}{}{}'.format(self.tempDir, self.numOfImages, '.png'))
    #     self.numOfImages += 1
    #
    # def saveVideo(self, fileName):
    #     infoImg = cv2.imread('{}{}'.format(self.tempDir, '0.png'))
    #     height, width, layers = infoImg.shape
    #     video = cv2.VideoWriter('vid/{}{}'.format(fileName, '.avi'), cv2.VideoWriter_fourcc(*'DIVX'), 60, (width, height))
    #
    #     for i in range(0, self.numOfImages, int(self.numOfImages / 600)):
    #         img = cv2.imread('{}{}{}'.format(self.tempDir, i, '.png'))
    #         video.write(img)
    #
    #     img = cv2.imread('{}{}{}'.format(self.tempDir, int(self.numOfImages - 1), '.png'))
    #     video.write(img)
    #
    #     cv2.destroyAllWindows()
    #     video.release()
    #
    # def hsv2rgb(self, h, s, v):
    #     return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
