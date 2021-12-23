## Get data
import utils
data = utils.readDayInputData(1, convertOutput='int')


## Part 1
increasedIndices = [i for i in range(1, len(data)) if data[i] > data[i-1]]

## ---
print('Part 1:\n',
      len(increasedIndices))



## Part 2
slidingWindowData = [sum([data[i-1], data[i], data[i+1]])
                          for i in range(1, len(data)-1)]
increasedIndices = [i for i in range(1, len(slidingWindowData))
                    if slidingWindowData[i] > slidingWindowData[i-1]]

## ---
print('Part 2:\n',
      len(increasedIndices))

