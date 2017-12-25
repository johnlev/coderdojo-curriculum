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
This will be done within 'Sorter_activity.py'.

We will be implementing bubblesort and mergesort in the 'bubblesort' and 'mergesortHelper' methods, respectively.
Quicksort and Radixsort have already been implemented and are available for you to play with and get an idea what the 
sorting algorithms you are implementing will do.
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

        self.shuffleUpdateThreshold = int(len(self.subpixmapKeys) / 100)
        self.bubblesortUpdateThreshold = 5000
        self.mergesortUpdateThreshold = 40
        self.quicksortUpdateThreshold = 10
        self.radixsortUpdateThreshold = 25
        self.count = 0

    def bubblesort(self):
        self.appWidget.disableAllButtons()
        self.count = 0

        # ANSWER STARTS HERE
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
        # ANSWER ENDS HERE

        self.redraw()
        self.appWidget.enableShuffleButton()

    def mergesort(self):
        self.appWidget.disableAllButtons()
        self.count = 0
        self.mergesortHelper(0, len(self.subpixmapKeys) - 1)
        self.redraw()
        self.appWidget.enableShuffleButton()

    def mergesortHelper(self, start, end):
        # ANSWER STARTS HERE
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
        # ANSWER ENDS HERE

    def quicksort(self):
        self.appWidget.disableAllButtons()
        self.count = 0
        self.quicksortHelper(0, len(self.subpixmapKeys) - 1)
        self.redraw()
        self.appWidget.enableShuffleButton()

    def quicksortHelper(self, start, end):
        if start < end:
            split = self.partition(start, end)

            self.quicksortHelper(start, split - 1)
            self.quicksortHelper(split + 1, end)

    def partition(self, start, end):
        pivot = self.subpixmapKeys[start]
        leftIndex = start + 1
        rightIndex = end

        done = False
        while not done:

            while leftIndex <= rightIndex and self.subpixmapKeys[leftIndex] <= pivot:
                leftIndex += 1

            while self.subpixmapKeys[rightIndex] >= pivot and rightIndex >= leftIndex:
                rightIndex -= 1

            if rightIndex < leftIndex:
                done = True
            else:
                self.count += 1
                temp = self.subpixmapKeys[leftIndex]
                self.subpixmapKeys[leftIndex] = self.subpixmapKeys[rightIndex]
                self.subpixmapKeys[rightIndex] = temp
                if (self.count > self.quicksortUpdateThreshold):
                    self.count = 0
                    self.redraw()

        self.count += 1
        temp = self.subpixmapKeys[start]
        self.subpixmapKeys[start] = self.subpixmapKeys[rightIndex]
        self.subpixmapKeys[rightIndex] = temp
        if (self.count > self.quicksortUpdateThreshold):
            self.count = 0
            self.redraw()

        return rightIndex

    # Method to do Radix Sort
    # Source: https://www.geeksforgeeks.org/radix-sort/
    def radixsort(self):
        self.appWidget.disableAllButtons()
        self.count = 0

        # Find the maximum number to know number of digits
        max1 = max(self.subpixmapKeys)

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp > 1:
            self.countingsort(exp)
            exp *= 10

        self.redraw()
        self.appWidget.enableShuffleButton()

    # Source: https://www.geeksforgeeks.org/radix-sort/
    def countingsort(self, exp1):

        n = len(self.subpixmapKeys)

        # The output array elements that will have sorted arr
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = int(self.subpixmapKeys[i] / exp1)
            count[(index) % 10] += 1

        # Change count[i] so that count[i] now contains actual
        #  position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = int(self.subpixmapKeys[i] / exp1)
            output[count[(index) % 10] - 1] = self.subpixmapKeys[i]
            count[(index) % 10] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(self.subpixmapKeys)):
            self.subpixmapKeys[i] = output[i]
            self.count += 1
            if (self.count >= self.radixsortUpdateThreshold):
                self.count = 0
                self.redraw()

    def getSubpixmapTuple(self, index):
        if(index < len(self.subpixmapKeys)):
            return self.subpixmapDict[self.subpixmapKeys[index]]
        else:
            print('Error: Index value \'{}\' is too high'.format(index))
            exit(1)

    def shuffleImage(self):
        self.appWidget.disableAllButtons()
        self.count = 0

        for i in range(len(self.subpixmapKeys)):
            j = i + int(random.random() * (len(self.subpixmapKeys) - i))
            tmp = self.subpixmapKeys[i]
            self.subpixmapKeys[i] = self.subpixmapKeys[j]
            self.subpixmapKeys[j] = tmp

            self.count += 1
            if(self.count > self.shuffleUpdateThreshold):
                self.count = 0
                self.redraw()

        # random.shuffle(self.subpixmapKeys)
        self.appWidget.update()
        self.appWidget.enableShuffleButton()
        self.appWidget.enableSortingButtons()

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
