# HexaGo (with MCTS AI)

### Description ###
Inspired by an old board game, HexaGo is a 6x6 board game, where both sides are given 3 rows of pawns (same characteristic as a Chess pawn). The goal is to get a pawn to the opponent's last row. This was a personal project of mine, where I used this as an opportunity to implement my first MCTS algorithm.

Start:
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

White ("O") wins:
```
Choose a move: bxa6#

  f e d c b a
1 O O O O O O
2 O O O O O O
3 X X O O . .
4 X . . X X .
5 X X X . . X
6 X X X X X O

White wins!
```

### How to Use ###
The code (`main.py`) can be executed both in the terminal and in an IDE. Parameters are available in `main.py` to adjust the AI algorithm. Ensure that all 3 scripts are stored in the same source folder.

#### Terminal Paramaters ####
Note that only **game_type** and **side** can be set as terminal parameters.

Usage: `python main.py [game_type] [side] [-v]`
- \[game_type]: `cpu` or `vs` (1-player or 2-player).
- \[side]: `white` or `black` (only when playing against cpu)
- `-v`: verbose flag. cpu will print UCB score for each move

#### main.py Paramaters ####
`main.py` provides additional paramters for adjusting the AI algorithm:
- game_type: "cpu" or "vs". 1-player or 2-player.
- side: "white" or "black". Dictate which side you are playing on (for CPU game ONLY)
- simulation_no: a positive integer to dictate the number of MCTS simulations executed for cpu (for CPU game ONLY)
- c_param: UCB confidence value. A positive integer to dictate the exploit-exploration formula ratio. Higher value == more exploration and less exploit (for CPU game ONLY)
- verbose: Dictate if cpu should print its UCB score for each move. Higher value == more favourable move (for CPU game ONLY)

### Credits ###
All credits to https://ai-boson.github.io/mcts/ for the MCTS code file. I merely adapted it for implementation.
