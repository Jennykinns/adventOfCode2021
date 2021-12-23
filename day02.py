## Get data
import utils
data = utils.readDayInputData(2)

class submarineDriveSystem(object):
    def __init__(self):
        self.depthPosition_legacy = 0

        self.horizontalPosition = 0
        self.depthPosition = 0
        self.aimDirection = 0

    def parseInstruction(self, instructionString):
        instruction, value = instructionString.split(' ')
        value = int(value)

        if instruction == 'forward':
            self.horizontalMove(value)
        elif instruction == 'down':
            self.verticalMove(value)
        elif instruction == 'up':
            self.verticalMove(value * -1)

        else:
            raise('Invalid instruction given: {}'.format(instructionString))

    def horizontalMove(self, number):
        self.horizontalPosition += number

        ## Part 2
        self.depthPosition += self.aimDirection * number

    def verticalMove(self, number):
        ## Part 1
        self.depthPosition_legacy += number

        ## Part 2
        self.aimDirection += number

    def calculateSolution_legacy(self):
        return self.horizontalPosition * self.depthPosition_legacy

    def calculateSolution(self):
        return self.horizontalPosition * self.depthPosition


sub = submarineDriveSystem()
for each in data:
    sub.parseInstruction(each)

print('Part 1:\n',
      sub.calculateSolution_legacy())
print('Part 2:\n',
      sub.calculateSolution())
