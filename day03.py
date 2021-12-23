## Get input data
import utils
data = utils.readDayInputData(3)

def binaryStringToInt(input):
    return int(input, 2)

lengthOfDataBinary = len(data[0])

## Part 1
def getGammaAndEpsilon(dataSet):
    binaryArray = [0] * lengthOfDataBinary
    for i in range(len(dataSet)):
        for j in range(lengthOfDataBinary):
            binaryArray[j] += int(dataSet[i][j])

    gammaRate = ''.join(['0' if x < len(dataSet)/2 else '1'
                         for x in binaryArray])
    epsilonRate = ''.join(['0' if x >= len(dataSet)/2 else '1'
                           for x in binaryArray])
    # epsilonRate = ''.join(['1' if x <= len(dataSet)/2 else '0'
    #                        for x in binaryArray])
    return gammaRate, epsilonRate

gRate, eRate = getGammaAndEpsilon(data)
print('Part 1:\n',
      binaryStringToInt(gRate) * binaryStringToInt(eRate))

## Part 2
O2Rates = list(data)
Co2Rates = list(data)

for i in range(lengthOfDataBinary):
    ## Oxygen
    if len(O2Rates) > 1:
        g, e = getGammaAndEpsilon(O2Rates)
        newO2Rates = []
        for rate in O2Rates:
            if rate[i] == g[i]:
                newO2Rates.append(rate)
        O2Rates = newO2Rates

    ## CO2 Scrubber
    if len(Co2Rates) > 1:
        g, e = getGammaAndEpsilon(Co2Rates)
        newCo2Rates = []
        for rate in Co2Rates:
            if rate[i] == e[i]:
                newCo2Rates.append(rate)
            Co2Rates = newCo2Rates

print('Part 2:\n',
      binaryStringToInt(O2Rates[0]) * binaryStringToInt(Co2Rates[0]))

