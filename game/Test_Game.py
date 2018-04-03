from UserPlayer import UserPlayer
from ComputerPlayer import ComputerPlayer
from Game import Game
from unittest import TestCase
from unittest import mock
from io import StringIO
import sys

# Having a bit trouble implementing Test for reading print

class TestGame(TestCase):
    @mock.patch('sys.stdout', new_callable=StringIO)
    def UserPlayer_main_op(self, tst_str, mock_stdout):
        with mock.patch('builtins.input', side_effect=tst_str):
            UserPlayer().askInput()
        return mock_stdout.getvalue()

    def testValidUserInput(self):
        for s in ('s','p','r','S','P','R'):
            with mock.patch('builtins.input',return_value=s):
                r = UserPlayer().askInput()
                self.assertEqual(r,s.lower())

    # def testEmptyUserInput(self):
    #     capturedOutput = StringIO()          # Create StringIO object
    #     sys.stdout = capturedOutput                   #  and redirect stdout.
    #     with mock.patch('builtins.input',return_value=''):        
    #         sys.stdout = sys.__stdout__                   # Reset redirect.
    #         print ('Captured', capturedOutput.getvalue())   # Now works as before.
    #         self.assertEqual(capturedOutput.getvalue(), 'Invalid Input!')

    # def testSpaceUserInput(self):
    #     self.assertTrue(True)

    # def testLongUserInput(self):
    #     self.assertTrue(True)

    def testComputerInput100Round(self):
        for n in range(0,100):
            r = ComputerPlayer().generateInput()
            self.assertTrue(r =='s' or r == 'r' or r == 'p')

    # def testValidGameRematchInput(self):
    #     for s in ('y','Y'):
    #         with mock.patch('builtins.input',return_value=s):
    #             capturedOutput = StringIO()          # Create StringIO object
    #             sys.stdout = capturedOutput                   #  and redirect stdout.
    #             Game().checkRematch()
    #             sys.stdout = sys.__stdout__                   # Reset redirect.
    #             self.assertEqual(capturedOutput.getvalue(), 'Lets go!')

    # def testEmptyGameRematchInput(self):
    #     self.assertTrue(True)

    # def testSpaceGameRematchInput(self):
    #     self.assertTrue(True)
        
    # def testLongGameRematchInput(self):
    #     self.assertTrue(True)