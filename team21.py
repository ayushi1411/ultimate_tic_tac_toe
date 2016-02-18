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
		if len(blocks)==0:
			for i in range(9):
				if temp_block[i]!='-':
					blocks.append(i)


		cells=[]
		for i in blocks:
			cells.append(get_valid_cells(temp_board,i,flag))

		if len(cells)!=0:
			return (cells[0][0],cells[0][1])

		else:
			cells=[]
			for i in blocks:
				temp=get_empty_cells(temp_board,i);
				if temp[0]!=-1 and temp[1]!=-1:
					cells.append(temp)


	def get_empty_cells(self,temp_board,i):
		index_x=i/3
		index_y=i%3
		for j in range(index_x*3,index_x*3+3):
			for k in range(index_y*3,index_y*3+3):
				if temp_board[j][k]=='-':
					return (j,k)
		return (-1,-1)

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

	def get_valid_cells(self,temp_board,i,flag):
		index_x=i/3
		index_y=i%3
		cell_seq=[]
		#checking rows
		for j in range(index_x*3, index_x*3+3):
			for k in range (index_y*3,index_y*3+3):
				cell_seq.append(temp_board[j][k])

			ans=get_win_move(cell_seq,flag)
			if ans!=-1:
				return (j,index_y*3+ans)
			cell_seq=[]

		#checking columns
		for k in range (index_y*3,index_y*3+3):
			for j in range(index_x*3, index_x*3+3):
				cell_seq.append(temp_board[j][k])
			ans=get_win_move(cell_seq,flag)
			if ans!=-1:
				return (index_x*3+ans,k)
			cell_seq=[]	

		#checking major diagonal
		for j in range (3):
			cell_seq.append(temp_board[index_x+j][index_y+j])

		ans=get_win_move(cell_seq,flag)
		if ans!=-1:
			return (index_x+ans,index_y+ans)


		#checking minor diagonal
		cell_seq=[]
		for j in range(3):
			cell_seq.append(index_x*3+j,index_y*3-j)

		ans=get_win_move(cell_seq,flag)
		if ans!=-1:
			return (index_x+ans,index_y-ans)







	def get_win_move(self, tup,flag):
		if tup[0]==tup[1] and tup[0]==flag:
			return 2

		elif tup[0]==tup[2] and tup[0]==flag:
			return 1

		elif tup[1]==tup[2] and tup[1]==flag:
			return 0

		else :
			return -1

