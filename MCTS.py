# All credit to https://ai-boson.github.io/mcts/
# Code adapted to fit my use case.
# if you forget how to do MCST: https://www.youtube.com/watch?v=UXW2yZndl7U&ab_channel=JohnLevine

import numpy as np
from collections import defaultdict

class MonteCarloTreeSearchNode():

	def __init__(self, state, side, parent=None, parent_action=None):
		self.state = state
		self.side = side
		self.parent = parent
		self.parent_action = parent_action
		self.children = []
		self._number_of_visits = 0
		self._results = defaultdict(int)
		self._results[1] = 0
		self._results[-1] = 0
		self._untried_actions = self.untried_actions()
		return

	def untried_actions(self):
		self._untried_actions = self.state.get_legal_moves()
		return self._untried_actions

	def q(self):
		if self.side == "white":
			wins = self._results[1]
			loses = self._results[-1]
		else:
			wins = self._results[-1]
			loses = self._results[1]
		return wins - loses

	def n(self):
		return self._number_of_visits

	def expand(self):
		action = self._untried_actions.pop()
		next_state = self.state.copy_board_state()
		next_state.move(action)
		child_node = MonteCarloTreeSearchNode(
			next_state, self.side, parent=self, parent_action=action)

		self.children.append(child_node)
		return child_node

	def is_terminal_node(self):
		return self.state.is_game_over(self.state.get_legal_moves())

	def rollout(self):
		current_rollout_state = self.state.copy_board_state()
		while True:
			possible_moves = current_rollout_state.get_legal_moves()
			if current_rollout_state.is_game_over(possible_moves):
				return current_rollout_state.get_game_result()
			action = self.rollout_policy(possible_moves)
			current_rollout_state.move(action)

	def rollout_policy(self, possible_moves): # how rollout is carried out ie random
		return possible_moves[np.random.randint(len(possible_moves))]

	def backpropagate(self, result):
		self._number_of_visits += 1.
		self._results[result] += 1.
		if self.parent:
			self.parent.backpropagate(result)

	def is_fully_expanded(self):
		return len(self._untried_actions) == 0

	def best_child(self, c_param, verbose=False): # uses UCB formula
		choices_weights = [(c.q() / c.n()) + c_param * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
		if verbose==True:
			for i in range(len(self.children)):
				print(self.children[i].parent_action, choices_weights[i])
		return self.children[np.argmax(choices_weights)]

	def _tree_policy(self, c_param=1000): # main tree traversal logic (selects node to rollout)
		current_node = self
		while not current_node.is_terminal_node():
			if not current_node.is_fully_expanded():
				return current_node.expand()
			else:
				current_node = current_node.best_child(c_param)
		return current_node

	def best_action(self, simulation_no=5000, c_param=1000, verbose=False):
		for i in range(simulation_no):
			v = self._tree_policy(c_param)
			reward = v.rollout()
			v.backpropagate(reward)
		return self.best_child(c_param=0., verbose=verbose).parent_action
		# essentially return q / n because explore param == 0 (ie win percentage)




