class Board(object):
	def __init__(self):
		self.board = ["-", "-", "-", "-", "-", "-", "-", "-", "-",
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


	def fill(self, num=1):
		random.fill(self.filled_digits)


	def display_board(self):
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

	def change_move(self):
		pass

	

    
