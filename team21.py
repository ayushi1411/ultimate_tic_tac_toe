'''
Team 21
Ayushi Goyal 201401060
Shreya Jain 201402230
Class Player21 implemented using alpha beta pruning and other heuristics
'''
import copy
class Player21:
	def __init__(self):
		self.WINNING_SEQUENCE=[(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8)]
		self.DEPTH=4
		self.maximum=9223372036854775807

	MAXX = 9223372036854775807
	
	def move(self,temp_board,temp_block,old_move,flag):
		if old_move[0]==-1 and old_move[1]==-1:
			return (4,4)

		cells=self.get_valid_moves(temp_board,temp_block,old_move,flag)
		print cells
		if len(cells)==1:
			return (cells[0][0],cells[0][1])

		action_values=[]
		for action in cells:
			successor_state = self.generate_successor(temp_board, action, flag)
			action_values.append((action, self.__min_val_ab(successor_state, self.DEPTH, temp_block, flag, old_move)))

		_, best_action_val = max(action_values, key=lambda x: x[1])
		print "out"
		final_choice=[]
		for best_action,value in action_values:
			if value==best_action_val:
				final_choice.append(best_action)

		return random.choice(final_choice)
		#return (cells[0],cells[1])

	def get_valid_moves(self,temp_board,temp_block,old_move,flag):
		blocks=self.get_valid_blocks(temp_block,old_move)
		if len(blocks)==0:
			for i in range(9):
				if temp_block[i]=='-':
					blocks.append(i)

		cells=[]
		for i in blocks:
			temp=[]
			temp=self.get_valid_cells(temp_board,i,flag)

			for i in temp:
				cells.append(i)

		valid_cells=[]
		#print cells
		for i in cells:
			if i[0]!=-1 and i[1]!=-1:
				valid_cells.append(i)

		if len(valid_cells)!=0:
			#print valid_cells
			return valid_cells

		else:
			cells=[]
			temp=[]
			#valid_cells=[]
			for i in blocks:
				temp=[]
				temp=self.get_empty_cells(temp_board,i);
				for i in temp:
					cells.append(i)

			return cells




	def get_empty_cells(self,temp_board,i):
		index_x=i/3
		index_y=i%3
		empty_cells=[]
		for j in range(index_x*3,index_x*3+3):
			for k in range(index_y*3,index_y*3+3):
				if temp_board[j][k]=='-':
					empty_cells.append((j,k))
		return empty_cells

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

	def get_valid_cells1(self,temp_board,i,flag):
		index_x=i/3
		index_y=i%3
		#cells_seq=[]
		cells=[]
		for j in range (index_x*3,index_x*3+3):
			for k in range (index_y*3,index_y*3+3):
				if temp_board[j][k]=='-':
					cells.append((j,k))

	def get_valid_cells(self,temp_board,i,flag):
		index_x=i/3
		index_y=i%3
		cell_seq=[]
		cells=[]
		#checking rows
		for j in range(index_x*3, index_x*3+3):
			for k in range (index_y*3,index_y*3+3):
				cell_seq.append(temp_board[j][k])

			ans=self.get_win_move(cell_seq,flag)
			if ans!=-1:
				if (j,index_y*3+ans) not in cells:
					cells.append((j,index_y*3+ans))
			cell_seq=[]

		#checking columns
		for k in range (index_y*3,index_y*3+3):
			for j in range(index_x*3, index_x*3+3):
				cell_seq.append(temp_board[j][k])
			ans=self.get_win_move(cell_seq,flag)
			if ans!=-1:
				if (index_x*3+ans,k) not in cells:
					cells.append((index_x*3+ans,k))
				#return (index_x*3+ans,k)
			cell_seq=[]	

		#checking major diagonal
		for j in range (3):
			cell_seq.append(temp_board[index_x*3+j][index_y*3+j])

		ans=self.get_win_move(cell_seq,flag)
		if ans!=-1:
			if (index_x*3+ans,index_y*3+ans) not in cells:
				cells.append((index_x*3+ans,index_y*3+ans))
		#	return (index_x*3+ans,index_y*3+ans)


		#checking minor diagonal
		cell_seq=[]
		for j in range(3):
			cell_seq.append(temp_board[index_x*3+j][index_y*3+2-j])

		ans=self.get_win_move(cell_seq,flag)
		if ans!=-1:
			if (index_x*3+ans,index_y*3+2-ans) not in cells:
				cells.append((index_x*3+ans,index_y*3+2-ans))
			#return (index_x*3+ans,index_y*3+2-ans)

		if len(cells)!=0:
			return cells

		return [(-1,-1)]

	def get_win_move(self, tup,flag):
		if tup[0]==tup[1] and tup[2]=='-' and tup[0]==flag:
			return 2

		elif tup[0]==tup[2] and tup[1]=='-' and tup[0]==flag:
			return 1

		elif tup[1]==tup[2] and tup[0]=='-' and tup[1]==flag:
			return 0

		else :
			return -1

	def __min_val_ab(self,temp_board, depth, temp_block, flag, old_move, alpha=-(MAXX), beta=(MAXX)):	
		score=[0]*9
		if self.terminal_test(temp_board, depth, temp_block):
			for i in range(9):
				block_state=[]
				for j in range((i/3)*3,(i/3)*3+3):
					for k in range((i%3)*3,(i%3)*3+3):
						block_state.append(temp_board[j][k])
				score[i]=self.evaluation_func(block_state, flag)

		val = (self.maximum)
		for act in self.get_valid_moves(temp_board,temp_block,old_move,flag):
			successor_state = self.generate_successor(temp_board, act, flag)
			val = min(val, self.__max_val_ab(successor_state,  depth - 1, temp_block, flag, old_move, alpha, beta))
			if val <= alpha:
				return val
			beta = min(beta, val)
		return val

	def __max_val_ab(self,temp_board, depth, temp_block,flag, old_move, alpha=-(MAXX), beta=(MAXX)):
		score=[0]*9
		if self.terminal_test(temp_board, depth, temp_block):
			for i in range(9):
				block_state=[]
				for j in range((i/3)*3,(i/3)*3+3):
					for k in range((i%3)*3,(i%3)*3+3):
						block_state.append(temp_board[j][k])
				score[i]=self.evaluation_func(block_state, flag)

		val = -(self.maximum)
		for act in self.get_valid_moves(temp_board,temp_block,old_move,flag):
			successor_state = self.generate_successor(temp_board, act, flag)
			val = max(val, self.__min_val_ab(successor_state, depth, temp_block, flag, old_move, alpha, beta))
			if val >= beta:
				return val
			alpha = max(alpha, val)
		return val


	def terminal_test(self,temp_board, depth, temp_block):
		if depth==0:
			return True
		a,msg =  self.terminal_state_reached(temp_board, temp_block)
		return a

	def generate_successor(self, temp_board, action, flag):
		board = copy.deepcopy(temp_board)
		board[action[0]][action[1]] = flag
		return board

	def terminal_state_reached(self,game_board, status_block):
		
		boardstat = status_block
		if (boardstat[0] == boardstat[1] and boardstat[1] == boardstat[2] and boardstat[1]!='-' and boardstat[1]!='d') or (boardstat[3]!='d' and boardstat[3]!='-' and boardstat[3] == boardstat[4] and boardstat[4] == boardstat[5]) or (boardstat[6]!='d' and boardstat[6]!='-' and boardstat[6] == boardstat[7] and boardstat[7] == boardstat[8]):
			#print block_stat
			return True,'W'

		elif (boardstat[0]!='d' and boardstat[0] == boardstat[3] and boardstat[3] == boardstat[6] and boardstat[0]!='-') or (boardstat[1]!='d'and boardstat[1] == boardstat[4] and boardstat[4] == boardstat[7] and boardstat[4]!='-') or (boardstat[2]!='d' and boardstat[2] == boardstat[5] and boardstat[5] == boardstat[8] and boardstat[5]!='-'):
			#print block_stat
			return True,'W'

		elif (boardstat[0] == boardstat[4] and boardstat[4] == boardstat[8] and boardstat[0]!='-' and boardstat[0]!='d') or (boardstat[2] == boardstat[4] and boardstat[4] == boardstat[6] and boardstat[2]!='-' and boardstat[2]!='d'):
			#print block_stat
			return True,'W'

		else:
			smfl = 0
			for i in range(9):
				for j in range(9):
					if game_board[i][j] == '-' and status_block[(i/3)*3+(j/3)] == '-':
						smfl = 1
						break
			if smfl == 1:
				return False,'continue'
			
			else:
				pointplayer1 = 0
				pointplayer2 = 0
				for i in status_block:
					if i == 'x':
						pointplayer1+=1
					elif i=='o':
						pointplayer2+=1
				if pointplayer1>pointplayer2:
					return True,'P1'
				elif pointplayer2>pointplayer1:
					return True,'P2'
				else:
					pointplayer1 = 0
					pointplayer2 = 0
					for i in range(len(game_board)):
						for j in range(len(game_board[i])):
							if game_board[i][j] == 'x':
								pointplayer1+=1
							elif game_board[i][j]=='o':
								pointplayer2+=1
					if pointplayer1>pointplayer2:
						return True,'P1'
					elif pointplayer2>pointplayer1:
						return True,'P2'
					else:
						return True,'D'

	def opponent(self,flag):
		if flag=='x':
			return 'o'
		else :
			return 'x'

	def get_score(self,cells_seq,flag):
		score=0
		if (cells_seq[0]==cells_seq[1] and cells_seq[1]==cells_seq[2]):
			if cells_seq[1]==flag:
				score=score+100
			elif cells_seq[1]==self.opponent(flag):
				score=score-100

		if (cells_seq[0]==cells_seq[1] and cells_seq[2]=='-'):
			if cells_seq[1]==flag:
				score=score+10
			elif cells_seq[1]==self.opponent(flag):
				score=score-10

		if (cells_seq[2]==cells_seq[1] and cells_seq[0]=='-'):
			if cells_seq[1]==flag:
				score=score+10
			elif cells_seq[1]==self.opponent(flag):
				score=score-10

		if (cells_seq[0]==cells_seq[2] and cells_seq[1]=='-'):
			if cells_seq[0]==flag:
				score=score+10
			elif cells_seq[0]==self.opponent(flag):
				score=score-10

		if(cells_seq[1]=='-' and cells_seq[2]=='-'):
			if cells_seq[0]==flag:
				score=score+1
			elif cells_seq[0]==self.opponent(flag):
				score=score-1

		if(cells_seq[0]=='-' and cells_seq[2]=='-'):
			if cells_seq[1]==flag:
				score=score+1
			elif cells_seq[1]==self.opponent(flag):
				score=score-1

		if(cells_seq[1]=='-' and cells_seq[0]=='-'):
			if cells_seq[2]==flag:
				score=score+1
			elif cells_seq[2]==self.opponent(flag):
				score=score-1
		return score

	def evaluation_func(self,block_state,flag):
		score=0
		cells_seq=[block_state[0],block_state[1],block_state[2]]
		score=score+self.get_score(cells_seq,flag)

		cells_seq=[block_state[3],block_state[4],block_state[5]]
		score=score+self.get_score(cells_seq,flag)

		cells_seq=[block_state[6],block_state[7],block_state[8]]
		score=score+self.get_score(cells_seq,flag)

		cells_seq=[block_state[0],block_state[3],block_state[6]]
		score=score+self.get_score(cells_seq,flag)

		cells_seq=[block_state[1],block_state[4],block_state[7]]
		score=score+self.get_score(cells_seq,flag)

		cells_seq=[block_state[2],block_state[5],block_state[8]]
		score=score+self.get_score(cells_seq,flag)

		cells_seq=[block_state[0],block_state[4],block_state[8]]
		score=score+self.get_score(cells_seq,flag)

		cells_seq=[block_state[2],block_state[4],block_state[6]]
		score=score+self.get_score(cells_seq,flag)

		return score