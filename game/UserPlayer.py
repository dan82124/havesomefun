class UserPlayer:
    playerInput = ''

    def askInput(self):
        self.playerInput = str(input('You go first (r)/Rock (p)/Paper (s)/Scissors: ')).lower()
        while not(self.validateInput(self.playerInput)):
            print('Invalid Input!')
            self.playerInput = input('You go again (r)/Rock (p)/Paper (s)/Scissors: ')
        return self.playerInput

    def validateInput(self, userInput):
        if (userInput == 'r') or  (userInput == 's') or (userInput == 'p'):
            return True
        else:
            return False
