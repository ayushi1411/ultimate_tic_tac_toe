'''
Team 21
Ayushi Goyal 201401060
Shreya Jain 201402230
Class Player21 implemented using alpha beta pruning and other heuristics
'''

class Player21:
	def __init__(self):
		self.WINNING_SEQUENCE=[(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8)]


	def move(self,temp_board,temp_block,old_move,flag):
		if old_move[0]==-1 and old_move[1]==-1:
			return (4,4)

		cells=get_valid_moves(temp_board,temp_block,old_move,flag)

	def get_valid_moves(self,temp_board,temp_block,old_move,flag):
		blocks=get_valid_blocks(temp_block,old_move)

	def get_valid_blocks(self,temp_block,old_move):
		valid_blocks = []
		if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
			valid_blocks = [1,3]
		elif old_move[0] % 3 == 0 and old_move[1] % 3 == 2:
			valid_blocks = [1,5]
		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 0:
			valid_blocks = [3,7]
		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 2:
			valid_blocks = [5,7]
		elif old_move[0] % 3 == 0 and old_move[1] % 3 == 1:
			valid_blocks = [0,2]
		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 0:
			valid_blocks = [0,6]
		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 1:
			valid_blocks = [6,8]
		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 2:
			valid_blocks = [2,8]
		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 1:
			valid_blocks = [4]

		final_valid_blocks = []
		for i in valid_blocks:
			if temp_block[i] == '-':
				final_valid_blocks.append(i)
		return final_valid_blocks