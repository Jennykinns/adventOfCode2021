import os

def readDayInputData(dayIndex, convertOutput='str'):
    dataFile = '/home/jenks/adventOfCode2021/data/{:02d}'.format(dayIndex)
    data = []
    with open(dataFile) as f:
        for l in f.readlines():
            if convertOutput == 'str':
                data.append(l.replace('\n', ''))
            elif convertOutput == 'int':
                data.append(int(l.replace('\n', '')))
    return data
