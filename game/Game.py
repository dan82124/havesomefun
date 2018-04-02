from UserPlayer import UserPlayer
from ComputerPlayer import ComputerPlayer

class Game:
    player = ''
    aI = ''
    winDict = {'rs' : True, 'pr' : True, 'sp' : True, 'sr' : False, 'rp' : False, 'ps' : False}

    def __init__(self):
        print("Lets Play Rock, Paper, Scissors!")
        self.initGame()

    def initGame(self):
        self.player = UserPlayer().askInput()
        self.aI = ComputerPlayer().generateInput()
        print('Your Input is: %s' %self.player)
        print("Computer's input is: %s" %self.aI)
        self.checkWinner()

    def checkWinner(self):
        if self.player == self.aI:
            print("You've Tied. Please try again!")
            self.initGame()
        else:
            if self.winDict[(self.player+self.aI)]:
                print("You've won!")
            else:
                print("You've lost!")
            self.checkRematch()

    def checkRematch(self):
        rematch = str(input('Wanna Rematch? (y/n) ')).lower()
        while not(self.validateInput(rematch)):
            print('Invalid Input!')
            rematch = str(input('Wanna Rematch? (y/n) ')).lower()

        if rematch == 'y' :
            print('Lets go!')
            self.initGame()
        else:
            print('GoodBye!')

    def validateInput(self, userInput):
        if (userInput == 'y') or (userInput == 'n'):
            return True
        else:
            return False

def main():
    Game()

if __name__ == '__main__':
    main()