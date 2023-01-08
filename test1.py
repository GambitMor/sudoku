import random


arr1 = ["-","-","-"]
arr = []

def fill_arr1():
		num_1 = (random.randint(1,9))
		arr1[0] = num_1
		num_2 = (random.randint(1,9))
		arr1[1] = num_2
		num_3 = (random.randint(1,9))
		arr1[2] = num_3
fill_arr1()
print(arr1)

for i in range(len(arr1) - 1):
	for j in range(i + 1, len(arr1)):
		if arr1[i] == arr1[j]:
			print("wrong value")


for num in arr1:
	if num != "-":
		arr.append(num)

print(arr)


# def bb():
# 	m = [[0 for x in range(3)] for y in range(3)]

# 	for i in m:
# 		print(i)

# bb()



# section_1 = ["-", "-", "-"]

# print(len(board))


# def fill():
# 	ax0 = 1
# 	ax1 = ax0

# 	section_1 = []

# 	for i in range(ax0):
# 	    section_1.append("-")
# 	    # for j in range(ax1):
# 	    # 	section_1[i].append("-")

# 	print (section_1)
# fill()
# for i in section_1:
	# section_1.append("-")
	# print(section_1)


# section_1 = ["-", "-", "-",
# 			 "-", "-", "-",
# 			 "-", "-", "-",]

# section_2 = section_1
# print(section_1)
# print(section_2)

# b = ["-", "-", "-", "-", "-", "-", "-", "-", "-",
#          "-", "-", "-", "-", "-", "-", "-", "-", "-",
#          "-", "-", "-", "-", "-", "-", "-", "-", "-",
#          "-", "-", "-", "-", "-", "-", "-", "-", "-",
#          "-", "-", "-", "-", "-", "-", "-", "-", "-",
#          "-", "-", "-", "-", "-", "-", "-", "-", "-",
#          "-", "-", "-", "-", "-", "-", "-", "-", "-",
#          "-", "-", "-", "-", "-", "-", "-", "-", "-",
#          "-", "-", "-", "-", "-", "-", "-", "-", "-",]


# def display_board():
# 	# for el in board:
# 	# 	el = 
# 	board = list(map(str, b))


# 	print("\n")
# 	print(board[0] + "  " + board[1] + "  " + board[2] + " | " + board[3] + "  " + board[4] + "  " + board[5] + " | " + board[6] + "  " + board[7] + "  " + board[8]),
# 	print(board[9] + "  " + board[10] + "  " + board[11] + " | " + board[12] + "  " + board[13] + "  " + board[14] + " | " + board[15] + "  " + board[16] + "  " + board[17]),
# 	print(board[18] + "  " + board[19] + "  " + board[20] + " | " + board[21] + "  " + board[22] + "  " + board[23] + " | " + board[24] + "  " + board[25] + "  " + board[26]),
# 	print("==========================="),
# 	print(board[27] + "  " + board[28] + "  " + board[29] + " | " + board[30] + "  " + board[31] + "  " + board[32] + " | " + board[33] + "  " + board[34] + "  " + board[35]),
# 	print(board[36] + "  " + board[37] + "  " + board[38] + " | " + board[39] + "  " + board[40] + "  " + board[41] + " | " + board[42] + "  " + board[43] + "  " + board[44]),
# 	print(board[45] + "  " + board[46] + "  " + board[47] + " | " + board[48] + "  " + board[49] + "  " + board[50] + " | " + board[51] + "  " + board[52] + "  " + board[53]),
# 	print("==========================="),
# 	print(board[54] + "  " + board[55] + "  " + board[56] + " | " + board[57] + "  " + board[58] + "  " + board[59] + " | " + board[60] + "  " + board[61] + "  " + board[62]),
# 	print(board[63] + "  " + board[64] + "  " + board[65] + " | " + board[66] + "  " + board[67] + "  " + board[68] + " | " + board[69] + "  " + board[70] + "  " + board[71]),
# 	print(board[72] + "  " + board[73] + "  " + board[74] + " | " + board[75] + "  " + board[76] + "  " + board[77] + " | " + board[78] + "  " + board[79] + "  " + board[80]),
# 	print("\n")
# # display_board()

# # arr = [0, 0, 0, 0, 0, 0, 0, 0]
	
# def fill():
# 	f = random.randint(1,9)
# 	b[1] = f
# 	c = random.randint(1,9)
# 	b[0] = c
# 	y = random.randint(1,9)
# 	b[2] = y


# fill()
# display_board()

# print(arr)

# while arr[0] != arr[1] and arr[1] != arr[2] and arr[0] != arr[2]:
# 	fill()
# 	print(arr)

# display_board()


# def display_section_1():
# section_1 = ((board[0], board[1], board[2]),
# 			(board[9], board[10], board[11]),
# 			(board[18], board[19], board[20]))
	
# 	for i in range(section_1 - 1):
# 		for j in range(i + 1, section_1):
# 			if section_1[i] == section_1[j]:
# 				print("wrong value")
# 	# for i in section_1:
# 	# 	print(i)


# display_section_1()


