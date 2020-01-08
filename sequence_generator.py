import numpy as np
import random

def sample_randomly_highest_probability(probabilities):
	max_prob = np.amax(probabilities)
	index_list = (np.where(probabilities == max_prob))[0]
	if len(index_list) == 1:
		return index_list[0]
	else:
		return random.choice(index_list)

def sequence_generator(pi, transMatrix, obsMatrix, states):
	sequences = []
	while len(sequences) < 10:
		curr_sequence = []
		curr_state = 0
		current_obs = 1
		while current_obs != 0:
			if len(curr_sequence) == 0:
				next_state = sample_randomly_highest_probability(pi)
			else:
				next_state = sample_randomly_highest_probability(transMatrix[curr_state])
			curr_state = next_state

			current_obs = sample_randomly_highest_probability(obsMatrix[next_state])
			curr_sequence.append(states[current_obs])
		if curr_sequence not in sequences:
			sequences.append(curr_sequence)

	for sequence in sequences:
		for i in range(len(sequence)):
			if i == len(sequence) - 1:
				print(sequence[i], end =" ")
			else:
				print(sequence[i] + ",", end =" ")
		print("\n")

if __name__ == "__main__":

	pi = np.array([0.0, 1.0, 0.0, 0.0])
	transMatrix = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.4, 0.3, 0.3], [0.3, 0.2, 0.2, 0.3]])
	obsMatrix = np.array([[1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0, 0.0], [0.0, 0.2, 0.2, 0.3, 0.3], [0.0, 0.0, 0.0, 0.5, 0.5]])
	states = ['S', 'A', 'B', 'C', 'D']

	sequence_generator(pi, transMatrix, obsMatrix, states)



