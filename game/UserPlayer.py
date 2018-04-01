class UserPlayer():
    playerInput = ''

    def askInput(self):
        self.playerInput = input('You go first (r)/Rock (p)/Paper (s)/Scissors: ')
        while not(self.validateInput(self.playerInput)):
            print('Invalid Input!')
            self.playerInput = input('You go again (r)/Rock (p)/Paper (s)/Scissors: ')
        return self.playerInput

    def validateInput(self, userInput):
        check = str(userInput).lower()
        if (check == 'r') or  (check == 's') or (check == 'p'):
            return True
        else:
            return False
