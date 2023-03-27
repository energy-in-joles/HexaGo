from MCTS import MonteCarloTreeSearchNode
from copy import deepcopy

class board():
	BOARD_SIZE = 6
	ASCII_a_INT = 97 # int to convert to ASCII "a"
	# board indexes from perspective of white (translated from board matrix)
	BOARD_COL_INDEXES = [chr(i) for i in range(ASCII_a_INT,BOARD_SIZE+ASCII_a_INT)]
	BOARD_ROW_INDEXES = [j+1 for j in reversed(range(BOARD_SIZE))]

	def __init__(self, board=None, turn="white"):
		if board == None:
			self.board_matrix = self.reset_board()
		else:
			self.board_matrix = board
		self.turn = turn
		return

	def reset_board(self):
		# creates 2D array for each block of black and white pawns
		black_rows = [["X" for i in range(self.BOARD_SIZE)] for j in range(int(self.BOARD_SIZE / 2))]
		white_rows = [["O" for i in range(self.BOARD_SIZE)] for j in range(int(self.BOARD_SIZE / 2))]
		return black_rows + white_rows

	def copy_board_state(self):
		copied_board = deepcopy(self.board_matrix) # board needs to be deepcopied because it is a 2d array
		return board(copied_board, self.turn)

	def print_board(self):
		if self.turn == "white":
			print("  "+" ".join(self.BOARD_COL_INDEXES)) ## offset by two chars for row indexes
			for i in range(self.BOARD_SIZE):
				print(str(self.BOARD_ROW_INDEXES[i])+" "+" ".join(self.board_matrix[i]))
		else:
			print("  "+" ".join(reversed(self.BOARD_COL_INDEXES)))
			for i in reversed(range(self.BOARD_SIZE)):
				print(str(self.BOARD_ROW_INDEXES[i])+" "+" ".join(reversed(self.board_matrix[i])))
		print("")
		return

	def get_legal_moves(self, turn=None): # get all legal moves for current turn
		legal_moves = []
		if turn == None:
			turn = self.turn
		for y in range(self.BOARD_SIZE):
			for x in range(self.BOARD_SIZE):
				if (self.board_matrix[y][x] == "O" and turn == "white" or 
				self.board_matrix[y][x] == "X" and turn == "black"):
					legal_moves += self.get_indiv_legal_moves(y, x, turn)
		if len(legal_moves) == 0: # if no moves left, append the option to "skip"
			legal_moves.append("skip")
		return legal_moves

	def get_indiv_legal_moves(self, y, x, turn): # get legal moves of indiv piece for current turn
		indiv_legal_moves = []
		if turn == "white":
			y_direction = -1
			target = "X"
			row_to_win = 0 # which row number leads to win condition
		else:
			y_direction = 1
			target = "O"
			row_to_win = self.BOARD_SIZE-1

		if row_to_win == y+y_direction: # add hash symbol if move is a win condition
			win_str = "#"
		else:
			win_str = ""

		if y+y_direction < 0 or y+y_direction >= self.BOARD_SIZE: # no moves if forward dir is out of board
			return indiv_legal_moves

		curr_board_col = self.BOARD_COL_INDEXES[x] # convert matrix index to board index for string
		target_board_row = self.BOARD_ROW_INDEXES[y+y_direction]

		if self.board_matrix[y+y_direction][x] == ".": # see if piece can advance straight
			indiv_legal_moves.append(f"{curr_board_col}{target_board_row}{win_str}")
		# try used to pass out of range cases
		try: # see if piece can "eat" to the left. "O" in e3 eating "X" in d3 == exd3
			if self.board_matrix[y+y_direction][x-1] == target and x-1 >= 0: # x-1 > 0 to prevent -1 index
				target_board_col = self.BOARD_COL_INDEXES[x-1]
				indiv_legal_moves.append(f"{curr_board_col}x{target_board_col}{target_board_row}{win_str}")
		except:
			pass

		try: # see if piece can "eat" to the right
			if self.board_matrix[y+y_direction][x+1] == target and x+1 >= 0:
				target_board_col = self.BOARD_COL_INDEXES[x+1]
				indiv_legal_moves.append(f"{curr_board_col}x{target_board_col}{target_board_row}{win_str}")
		except:
			pass
		return indiv_legal_moves

	def is_game_over(self, legal_moves):
		if "O" in self.board_matrix[0] or "X" in self.board_matrix[-1]: # if either sees a win
			return True
		if "skip" in legal_moves: # if both sides have no legal moves (ie only has 'skip'), draw
			if "skip" in self.get_legal_moves(self.get_other_side(self.turn)): # if other side also has no legal moves
				return True
		return False

	def get_game_result(self):
		if "O" in self.board_matrix[0]: # if white wins
			return 1
		if "X" in self.board_matrix[-1]: # if black wins
			return -1
		else: # if draw
			return 0

	def print_game_result(self, result):
		if result == 1:
			print("White wins!")
		elif result == -1:
			print("Black wins!")
		else:
			print("No moves left. It's a draw!")

	def move(self, choice): # update board matrix based on choice from legal moves
		if choice == "skip": # skip turn if no moves
			self.next_turn()
			return

		if self.turn == "white":
			y_direction = -1
			curr_piece = "O"
		else:
			y_direction = 1
			curr_piece = "X"

		if choice[-1] == "#": # trying to get target board row index. if last char is #, then it's second last char
			target_board_row = int(choice[-2])
		else:
			target_board_row = int(choice[-1])

		target_matrix_row = self.BOARD_ROW_INDEXES.index(target_board_row) # convert board index back to matrix index
		curr_matrix_row = target_matrix_row-y_direction # move backwards to current row index in matrix
		curr_matrix_col = self.BOARD_COL_INDEXES.index(choice[0])
		self.board_matrix[curr_matrix_row][curr_matrix_col] = "."

		if "x" in choice: # set target matrix col index
			target_matrix_col = self.BOARD_COL_INDEXES.index(choice[2])
		else: # if no "eating", no change to matrix col index
			target_matrix_col = curr_matrix_col
		self.board_matrix[target_matrix_row][target_matrix_col] = curr_piece

		self.next_turn() # move to the next player
		return

	def get_player_choice(self, legal_moves):
		print(f"Available moves: {legal_moves}")
		while True: # loop so that if player inputs wrong choice, open input field again
			p_choice = input("Choose a move: ")

			if p_choice not in legal_moves:
				print("Invalid move! Please try again.")
			else:
				print("")
				return p_choice

	def get_cpu_choice(self, side, legal_moves, simulation_no, c_param, verbose):
		cpu = MonteCarloTreeSearchNode(state = self, side = self.get_other_side(side))
		c_choice = cpu.best_action(simulation_no, c_param, verbose)
		print(f"Computer chose {c_choice}")
		print("")
		return c_choice

	def get_other_side(self, side): # a helper function to change sides (not gate for black and white)
		if side == "white":
			return "black"
		else:
			return "white"

	def next_turn(self):
		self.turn = self.get_other_side(self.turn)
		return

	def play(self, game_type="cpu", side="white", simulation_no=5000, c_param=1000, verbose=False): # main function to play
		while True:
			legal_moves = self.get_legal_moves()

			if self.is_game_over(legal_moves):
				self.print_board()
				self.print_game_result(self.get_game_result())
				break

			print(f"=== {self.turn}'s turn ===")
			self.print_board()

			if game_type == "cpu" and side != self.turn: # if it is cpu's turn
				choice = self.get_cpu_choice(side, legal_moves, simulation_no, c_param, verbose)
			else: # execute this for "vs" game mode or on player's turn in cpu game
				choice = self.get_player_choice(legal_moves)

			self.move(choice)
		return
