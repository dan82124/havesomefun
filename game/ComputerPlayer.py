from random import randint

class ComputerPlayer:
    outputDict = {0 : 'r', 1 : 'p', 2 : 's'}

    def generateInput(self):
        selected = randint(0,2)
        print('Computer has decided!')
        return ComputerPlayer.outputDict[selected]
