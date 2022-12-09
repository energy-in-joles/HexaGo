# HexaGo (with MCTS AI)

### Description ###
Inspired by an old board game, HexaGo is a 6x6 board game, where both sides are given 3 rows of pawns (same characteristic as a Chess pawn). The goal is to get a pawn to the opponent's last row. This was a personal project of mine, where I used this as an opportunity to implement my first MCTS algorithm.

```
=== white's turn ===
  a b c d e f
6 X X X X X X
5 X X X X X X
4 X X X X X X
3 O O O O O O
2 O O O O O O
1 O O O O O O

Available moves: ['axb4', 'bxa4', 'bxc4', 'cxb4', 'cxd4', 'dxc4', 'dxe4', 'exd4', 'exf4', 'fxe4']
Choose a move: 
```

### How to Use ###
The code (main.py) can be executed both in the terminal and in an IDE. Ensure that all 3 files are store in the same folder.

#### Running in IDE ####
The parameters for running in IDE are as follows:
- game_type: "cpu" or "vs". 1-player or 2-player.
- side: "white" or "black". Dictate which side you are playing on (for CPU game ONLY)
- simulation_no: a positive integer to dictate the number of MCTS simulations executed for cpu (for CPU game ONLY)
- c_param: a positive integer to dictate the UCB exploit-exploration formula ratio. Higher value == more exploration and less exploit (for CPU game ONLY)
- verbose: Dictate if cpu should print its UCB score for each move. Higher value == more favourable move

#### Running in Terminal ####
Note that only **game_type** and **side** can be selected when executed in the terminal.

Usage: python main.py \[game_type] \[side]

Terminal Parameters:
	game_type: cpu or vs (1-player or 2-player).
	side: white or black (only when playing against cpu)
	-v: verbose tag. cpu will print UCB score for each move

### Credits ###
All credits to https://ai-boson.github.io/mcts/ for the MCTS code file. I merely adapted it for implementation.
