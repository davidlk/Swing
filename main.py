import csv
import swing as sw

regShift = sw.ShiftType('Regular')
sw4Shift = sw.ShiftType('Swing 0400')
sw6Shift = sw.ShiftType('Swing 0600')
otherShift = sw.ShiftType('Other')

if __name__ == '__main__':
    # print regShift
    r = 0
    with open('dfFinal.csv', 'rU') as csvfile:
        shiftReader = csv.reader(csvfile)
        for row in shiftReader:
            timeBuckets = []
            buckIdx = 11
            for bucket in range(0,4):
                timeBuckets.append(sw.TimeBucket(row[buckIdx], row[buckIdx+1], row[buckIdx+2]))
                buckIdx = buckIdx + 4
            shift = sw.Shift(row[2], row[3], row[10], timeBuckets)
            print shift