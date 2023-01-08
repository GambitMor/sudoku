from board import Board
from player import Player
import numpy as np

class Rules(object):
	def __init__(self):
		self.myBoard = Board()
		self.player = Player("Ally")


	def check_matches_sections(self):
		self.section_2 = ((self.board[3], self.board[4], self.board[5]),
						  (self.board[12], self.board[13], self.board[14]),
						  (self.board[21], self.board[22], self.board[23]))
		self.section_3 = ((self.board[6], self.board[7], self.board[8]),
						  (self.board[15], self.board[16], self.board[17]),
						  (self.board[24], self.board[25], self.board[26]))
		self.section_4 = ((self.board[27], self.board[28], self.board[29]),
						  (self.board[36], self.board[37], self.board[38]),
						  (self.board[45], self.board[46], self.board[47]))
		self.section_5 = ((self.board[30], self.board[31], self.board[32]),
						  (self.board[39], self.board[40], self.board[41]),
						  (self.board[48], self.board[49], self.board[50]))
		self.section_6 = ((self.board[33], self.board[34], self.board[35]),
						  (self.board[42], self.board[43], self.board[44]),
						  (self.board[51], self.board[52], self.board[53]))
		self.section_7 = ((self.board[54], self.board[55], self.board[56]),
						  (self.board[63], self.board[64], self.board[65]),
						  (self.board[72], self.board[73], self.board[74]))
		self.section_8 = ((self.board[57], self.board[58], self.board[59]),
						  (self.board[66], self.board[67], self.board[68]),
						  (self.board[75], self.board[76], self.board[77]))
		self.section_9 = ((self.board[60], self.board[61], self.board[62]),
						  (self.board[69], self.board[70], self.board[71]),
						  (self.board[78], self.board[79], self.board[80]))

		
	def check_matches_section_1(self):
		self.board = list(map(str, self.myBoard.b))
		print(self.board)
		self.section_1 = [[self.board[0], self.board[1], self.board[2]], 
							[self.board[9], self.myBoard.b[10], self.board[11]],
							[self.board[18], self.board[19], self.board[20]]]
		print(self.section_1)
		for i in range(len(self.section_1) - 1):
			for j in range(i + 1, len(self.section_1)):
				if self.section_1[i] == self.section_1[j]:
					print("wrong value")

	def check_matches_section_2(self):
		for i in range(section_2 - 1):
			for j in range(i + 1, section_2):
				if section_2[i] == section_2[j]:
					print("wrong value")

	def check_matches_section_3(self):
		for i in range(section_3 - 1):
			for j in range(i + 1, section_3):
				if section_3[i] == section_3[j]:
					print("wrong value")

	def check_matches_section_4(self):
		for i in range(section_4 - 1):
			for j in range(i + 1, section_4):
				if section_4[i] == section_4[j]:
					print("wrong value")

	def check_matches_section_5(self):
		for i in range(section_5 - 1):
			for j in range(i + 1, section_5):
				if section_5[i] == section_5[j]:
					print("wrong value")

	def check_matches_section_6(self):
		for i in range(section_6 - 1):
			for j in range(i + 1, section_6):
				if section_6[i] == section_6[j]:
					print("wrong value")

	def check_matches_section_7(self):
		for i in range(section_7 - 1):
			for j in range(i + 1, section_7):
				if section_7[i] == section_7[j]:
					print("wrong value")

	def check_matches_section_8(self):
		for i in range(section_8 - 1):
			for j in range(i + 1, section_8):
				if section_8[i] == section_8[j]:
					print("wrong value")

	def check_matches_section_9(self):
		for i in range(section_9 - 1):
			for j in range(i + 1, section_9):
				if section_9[i] == section_9[j]:
					print("wrong value")

	

	def check_matches_rows(self):
		# for i in self.myBoard:


		pass

	def check_matches_columns(self):
		pass


