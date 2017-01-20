class ShiftType:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Shift type ' + self.name


class Shift:
    def __init__(self, startDateTime, endDateTime, patientCount, timeBuckets):
        self.startDateTime = startDateTime
        self.endDateTime = endDateTime
        self.patientCount = patientCount
        self.timeBuckets = timeBuckets

    def shiftLength(self):
        return self.endDateTime - self.startDateTime

    @property
    def isSwing(self):
        return self.startDateTime.hour() == 22

    @property
    def isTriggered(self):
        return self.endDateTime.hour() == 4

    def __str__(self):
        tbString = ','.join([tb.__str__() for tb in self.timeBuckets])
        return 'Shift(' + self.startDateTime + ',' + self.endDateTime + ',' + self.patientCount + ',('+ tbString +'))'


class TimeBucket:
    def __init__(self, bucketNumber, totalArrivals, waitingCount):
        self.bucketNumber = bucketNumber
        self.totalArrivals = totalArrivals
        self.waitingCount = waitingCount

    def __str__(self):
        return 'TBuck(' + self.bucketNumber + ',' + self.totalArrivals + ',' + self.waitingCount +')'

