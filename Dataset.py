class Dataset (object):

    # Loads a dataset from a file, first line is the topic of the test, second line is the test date, rest are the test
    # scores
    def __init__ (self, file_name):

        text_file = open(file_name, "r")
        self.testTopic = text_file.readline().strip()
        self.testDate = text_file.readline().strip()

        self.__numList = []
        self.__numList.sort()

        for line in text_file:
            line = int(line)
            self.__numList.append(line)

    # Returns the mean of the dataset.
    def getMean (self):
        total = 0

        for n in self.__numList:
            total += n

        return total / len(self.__numList)

    # Returns the range of the dataset.
    def getRange (self):
        return max(self.__numList) - min(self.__numList)

    # Returns the median of the dataset.
    def getMedian (self):

        self.__numList.sort()

        if len(self.__numList) % 2 == 0:
            pos = len(self.__numList) // 2
            return (self.__numList[pos] + self.__numList[pos - 1]) / 2
        else:
            pos = len(self.__numList) // 2
            return self.__numList[pos]

    # Returns the standard deviation of the dataset.
    def getStdDev (self):

        import math

        total = 0

        for x in range(len(self.__numList)):
            total += (self.getMean() - self.__numList[x]) ** 2

        return math.sqrt(total / len(self.__numList))

