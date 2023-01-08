from board import Board
from rules import Rules
from player import Player
import random


class Game(object):
	"""docstring for Game"""
	def __init__(self):
		self.myBoard = Board()
		self.rules = Rules()
        # self.ally = Player("Ally")

		# self.player = [self.Ally]
		self.myBoard.fill_section_1()
		# self.myBoard.fill_section_2()
		# self.myBoard.fill_section_3()
		# self.myBoard.fill_section_4()
		# self.myBoard.fill_section_5()
		# self.myBoard.fill_section_6()
		# self.myBoard.fill_section_7()
		# self.myBoard.fill_section_8()
		# self.myBoard.fill_section_9()

		self.rules.check_matches_section_1()

		self.myBoard.display_board()

	




if __name__ == '__main__':
    g = Game()
    # g.play_game()
