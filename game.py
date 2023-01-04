from board import Board
from rules import Rules


class Game(object):
	"""docstring for Game"""
	def __init__(self):
		self.myBoard = Board()
		
		# self.player = [self.Ally]

	def play_game(self):
		self.myBoard.display_board()

	def display_section_1(self)




if __name__ == '__main__':
    g = Game()
    g.play_game()
