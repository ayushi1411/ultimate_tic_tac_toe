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

		