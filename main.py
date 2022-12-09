from HexaGo import board
import sys
from sys import argv

def main():
	game_type = "cpu" # "cpu" or "vs". 1-player or 2-player.
	side = "white" # Paramater for cpu game. Dictate which side you are playing on
	simulation_no = 5000 # Dictate number of MCTS simulations executed for cpu
	c_param = 1000 # Dictate the exploit-exploration formula ratio. Higher value == more exploration (less exploit)
	verbose = False # Dictate if cpu should generate its UCB score for each move. Higher value == more favourable move

	if len(argv) >= 2:
		game_type, side, verbose = sanitise(game_type, side, verbose)

	game = board()
	game.play(game_type, side, simulation_no, c_param, verbose)

def sanitise(game_type, side, verbose):
	if "-h" in argv: # help flag
		print("""

	Usage: python main.py [game_type] [side]

	[game_type]: cpu or vs (1-player or 2-player).
	[side]: white or black (only when playing against cpu)
	-v: verbose tag. cpu will print UCB score for each move

	Default (with no arguments given): python main.py cpu white

			""")
		sys.exit()

	if "-v" in argv: # verbose flag
		argv.pop(argv.index("-v"))
		print(argv)
		verbose = True

	arg_n = len(argv)

	if arg_n >= 2:
		if argv[1] == "cpu" or argv[1] == "vs":
			game_type = argv[1]
		else:
			raise TypeError(f"Invalid game type! Your input: {argv[1]} [options: 'cpu' or 'vs']")

	if arg_n == 3:
		if argv[2] == "white" or argv[2] == "black":
			side = argv[2]
		else:
			raise TypeError(f"Invalid side! Your input: {argv[2]} [options: 'white' or 'black']")

	if arg_n > 3:
		raise TypeError(f"Too many arguments. 'python main.py -h' for help.")

	return game_type, side, verbose

if __name__ == "__main__":
	main()