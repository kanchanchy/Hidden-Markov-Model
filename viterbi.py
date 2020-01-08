import numpy as np

def viterbi(pi, transMat, obsMatrix, observations):
	seq_length = len(observations)
	no_state = pi.shape[0]
	alpha = np.zeros((seq_length, no_state))
	alpha[:,:] = float('-inf')
	backpointers = np.zeros((seq_length, no_state), 'int')
	alpha[0, :] = pi * obsMatrix[:,observations[0]]

	for t in range(1, seq_length):
		for j in range(no_state):
			for k in range(no_state):
				score = alpha[t-1, k] * transMat[k, j] * obsMatrix[j, observations[t]]
				if score > alpha[t, j]:
					alpha[t, j] = score
					backpointers[t, j] = k

	state_seq = []
	state_seq.append(np.argmax(alpha[seq_length-1,:]))
	for i in range(seq_length-1, 0, -1):
		state_seq.append(backpointers[i, state_seq[-1]])

	state_list = list(reversed(state_seq))
	return state_list[:len(state_list)-1]

if __name__ == "__main__":

	pi = np.array([0.0, 0.0, 0.0, 1.0])
	transMatrix = np.array([[1.0, 0.0, 0.0, 0.0], [0.1, 0.3, 0.5, 0.1], [0.1, 0.4, 0.3, 0.2], [0.1, 0.4, 0.2, 0.3]])
	obsMatrix = np.array([[1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.5, 0.0, 0.5], [0.0, 0.0, 0.5, 0.5, 0.0], [0.0, 0.5, 0.0, 0.0, 0.5]])
	states = S, A, B, C, D = 0, 1, 2, 3, 4

	print(viterbi(pi, transMatrix, obsMatrix, [A, D, C, B, D, C, C, S]))
	print(viterbi(pi, transMatrix, obsMatrix, [B, D, S]))
	print(viterbi(pi, transMatrix, obsMatrix, [B, C, C, B, D, D, C, A, C, S]))
	print(viterbi(pi, transMatrix, obsMatrix, [A, C, D, S]))
	print(viterbi(pi, transMatrix, obsMatrix, [A, D, A, C, S]))
	print(viterbi(pi, transMatrix, obsMatrix, [D, B, B, S]))
	print(viterbi(pi, transMatrix, obsMatrix, [A, B, S]))
	print(viterbi(pi, transMatrix, obsMatrix, [D, D, B, D, D, B, A, C, C, D, A, B, B, C, D, B, B, B, S]))
	print(viterbi(pi, transMatrix, obsMatrix, [D, B, D, S]))
	print(viterbi(pi, transMatrix, obsMatrix, [A, A, A, A, D, C, B, S]))

