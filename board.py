import random


class Board(object):
	def __init__(self):
		self.b = ["-", "-", "-", "-", "-", "-", "-", "-", "-",
		         "-", "-", "-", "-", "-", "-", "-", "-", "-",
		         "-", "-", "-", "-", "-", "-", "-", "-", "-",
		         "-", "-", "-", "-", "-", "-", "-", "-", "-",
		         "-", "-", "-", "-", "-", "-", "-", "-", "-",
		         "-", "-", "-", "-", "-", "-", "-", "-", "-",
		         "-", "-", "-", "-", "-", "-", "-", "-", "-",
		         "-", "-", "-", "-", "-", "-", "-", "-", "-",
		         "-", "-", "-", "-", "-", "-", "-", "-", "-",]
		self.filled_digits = []
		# self.fill_in()


	def fill_section_1(self):
		num_1 = (random.randint(1,9))
		self.b[0] = num_1
		num_2 = (random.randint(1,9))
		self.b[2] = num_2
		num_3 = (random.randint(1,9))
		self.b[9] = num_3

		while self.b[0] == self.b[2] or self.b[2] == self.b[9] or self.b[0] == self.b[9]:
			self.fill_section_1()

	def fill_section_2(self):
		num_4 = (random.randint(1,10))
		self.b[12] = num_4
		num_5 = (random.randint(1,10))
		self.b[13] = num_5
		num_6 = (random.randint(1,10))
		self.b[14] = num_6

		while( self.b[12] != self.b[13] and self.b[13] != self.b[14] and self.b[12] != self.b[14] and 
			self.b[12] != self.b[0]):
			self.fill_section_2()
	def fill_section_3(self):
		num_7 = (random.randint(1,10))
		self.b[15] = num_7
		num_8 = (random.randint(1,10))
		self.b[25] = num_8
		num_9 = (random.randint(1,10))
		self.b[26] = num_9

		while (self.b[15] != self.b[25] and self.b[25] != self.b[26] and
		self.b[15] != self.b[26] and self.b[15] != self.b[12]):
			self.fill_section_3()

	def fill_section_4(self):
		num_10 = (random.randint(1,10))
		self.b[29] = num_10
		num_11 = (random.randint(1,10))
		self.b[37] = num_11
		num_12 = (random.randint(1,10))
		self.b[47] = num_12

		while (self.b[29] != self.b[37] and self.b[37] != self.b[47] and
		self.b[29] != self.b[47] and self.b[29] != self.b[2]):
			self.fill_section_4()
		
	def fill_section_5(self):
		num_13 = (random.randint(1,10))
		self.b[30] = num_13
		num_14 = (random.randint(1,10))
		self.b[32] = num_14
		num_15 = (random.randint(1,10))
		self.b[49] = num_15

		while (self.b[30] != self.b[32] and self.b[32] != self.b[49] and
		self.b[30] != self.b[49] and self.b[30] != self.b[29] and
		self.b[32] != self.b[29] and self.b[32] != self.b[14]):
			self.fill_section_5()
		
	def fill_section_6(self):
		num_16 = (random.randint(1,10))
		self.b[42] = num_16
		num_17 = (random.randint(1,10))
		self.b[43] = num_17
		num_18 = (random.randint(1,10))
		self.b[44] = num_18

		while (self.b[42] != self.b[43] and self.b[43] != self.b[44] and
		self.b[42] != self.b[44] and self.b[42] != self.b[37] and
		self.b[42] != self.b[15] and self.b[43] != self.b[37] and
		self.b[43] != self.b[25] and self.b[44] != self.b[37] and
		self.b[44] != self.b[26]):
			self.fill_section_6()

	def fill_section_7(self):
		num_19 = (random.randint(1,10))
		self.b[54] = num_19
		num_20 = (random.randint(1,10))
		self.b[64] = num_20
		num_21 = (random.randint(1,10))
		self.b[73] = num_21

		while (self.b[54] != self.b[64] and self.b[64] != self.b[73] and
		self.b[54] != self.b[73] and self.b[54] != self.b[0] and
		self.b[54] != self.b[9] and self.b[64] != self.b[37] and
		self.b[73] != self.b[37]):
			self.fill_section_7()

	def fill_section_8(self):
		num_22 = (random.randint(1,10))
		self.b[57] = num_22
		num_23 = (random.randint(1,10))
		self.b[66] = num_23
		num_24 = (random.randint(1,10))
		self.b[75] = num_24

		while (self.b[56] != self.b[66] and self.b[66] != self.b[75] and
		self.b[57] != self.b[75] and self.b[57] != self.b[54] and
		self.b[57] != self.b[30] and self.b[57] != self.b[12] and
		self.b[66] != self.b[64] and self.b[66] != self.b[30] and
		self.b[66] != self.b[12] and self.b[75] != self.b[73] and
		self.b[75] != self.b[30] and self.b[75] != self.b[12]):
			self.fill_section_8()

	def fill_section_9(self):
		num_25 = (random.randint(1,10))
		self.b[60] = num_25
		num_26 = (random.randint(1,10))
		self.b[71] = num_26
		num_27 = (random.randint(1,10))
		self.b[79] = num_27

		while (self.b[60] != self.b[71] and self.b[71] != self.b[79] and
		self.b[60] != self.b[79] and self.b[57] != self.b[60] and
		self.b[60] != self.b[54] and self.b[60] != self.b[42] and
		self.b[60] != self.b[15] and self.b[79] != self.b[73] and
		self.b[79] != self.b[75] and self.b[79] != self.b[43] and
		self.b[79] != self.b[25] and self.b[71] != self.b[64] and
		self.b[71] != self.b[66] and self.b[71] != self.b[44] and
		self.b[71] != self.b[26]):
			self.fill_section_9()


	def display_board(self):
		self.board = list(map(str, self.b))

		print("\n")
		print(self.board[0] + "  " + self.board[1] + "  " + self.board[2] + " | " + self.board[3] + "  " + self.board[4] + "  " + self.board[5] + " | " + self.board[6] + "  " + self.board[7] + "  " + self.board[8]),
		print(self.board[9] + "  " + self.board[10] + "  " + self.board[11] + " | " + self.board[12] + "  " + self.board[13] + "  " + self.board[14] + " | " + self.board[15] + "  " + self.board[16] + "  " + self.board[17]),
		print(self.board[18] + "  " + self.board[19] + "  " + self.board[20] + " | " + self.board[21] + "  " + self.board[22] + "  " + self.board[23] + " | " + self.board[24] + "  " + self.board[25] + "  " + self.board[26]),
		print("==========================="),
		print(self.board[27] + "  " + self.board[28] + "  " + self.board[29] + " | " + self.board[30] + "  " + self.board[31] + "  " + self.board[32] + " | " + self.board[33] + "  " + self.board[34] + "  " + self.board[35]),
		print(self.board[36] + "  " + self.board[37] + "  " + self.board[38] + " | " + self.board[39] + "  " + self.board[40] + "  " + self.board[41] + " | " + self.board[42] + "  " + self.board[43] + "  " + self.board[44]),
		print(self.board[45] + "  " + self.board[46] + "  " + self.board[47] + " | " + self.board[48] + "  " + self.board[49] + "  " + self.board[50] + " | " + self.board[51] + "  " + self.board[52] + "  " + self.board[53]),
		print("==========================="),
		print(self.board[54] + "  " + self.board[55] + "  " + self.board[56] + " | " + self.board[57] + "  " + self.board[58] + "  " + self.board[59] + " | " + self.board[60] + "  " + self.board[61] + "  " + self.board[62]),
		print(self.board[63] + "  " + self.board[64] + "  " + self.board[65] + " | " + self.board[66] + "  " + self.board[67] + "  " + self.board[68] + " | " + self.board[69] + "  " + self.board[70] + "  " + self.board[71]),
		print(self.board[72] + "  " + self.board[73] + "  " + self.board[74] + " | " + self.board[75] + "  " + self.board[76] + "  " + self.board[77] + " | " + self.board[78] + "  " + self.board[79] + "  " + self.board[80]),
		print("\n")




	def check_for_end(self):
		game_still_going = True
		for i in self.board:
			for j in self.board:
				if j != "-"	and j >= 1 and j <= 9:	         # I'll bump into a bag if the last 
					game_still_going = False					 				# number >9 or <1 game will end anyway
				
		self.board.display_board()

	def make_limits(self):
		for i in board:
			for j in board:
				if j > 9 or j < 1:
					return False
				print("wrong value")
		

	def change_move(self):
		position = input("Choose a position from 1-81: ")
		position = int(position) - 1 					#TODO
		pass

	

    
