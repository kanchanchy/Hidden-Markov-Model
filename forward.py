import numpy as np
import math

def forward(pi, transMat, obsMat, observations):
	seq_length = len(observations)
	no_state = pi.shape[0]

	alpha = np.zeros((seq_length, no_state))
	alpha[0, :] = pi * obsMat[:,observations[0]]

	for i in range(1, seq_length):
		for j in range(no_state):
			for k in range(no_state):
				alpha[i, j] += alpha[i-1, k] * transMat[k, j] * obsMat[j, observations[i]]
	return np.sum(alpha[seq_length-1,:])

if __name__ == "__main__":

	#forward algorithm for lamda 1
	pi = np.array([0.0, 1.0, 0.0, 0.0])
	transMatrix = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.4, 0.3, 0.3], [0.3, 0.2, 0.2, 0.3]])
	obsMatrix = np.array([[1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0, 0.0], [0.0, 0.2, 0.2, 0.3, 0.3], [0.0, 0.0, 0.0, 0.5, 0.5]])
	states = S, A, B, C, D = 0, 1, 2, 3, 4

	print("Printing probabilities of each observations for lambda 1:")
	print(math.log(forward(pi, transMatrix, obsMatrix, [A, D, C, B, D, C, C, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [B, D, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [B, C, C, B, D, D, C, A, C, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [A, C, D, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [A, D, A, C, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [D, B, B, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [A, B, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [D, D, B, D, D, B, A, C, C, D, A, B, B, C, D, B, B, B, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [D, B, D, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [A, A, A, A, D, C, B, S])))

	#forward algorithm for lamda 2
	pi = np.array([0.0, 0.0, 0.0, 1.0])
	transMatrix = np.array([[1.0, 0.0, 0.0, 0.0], [0.1, 0.3, 0.5, 0.1], [0.1, 0.4, 0.3, 0.2], [0.1, 0.4, 0.2, 0.3]])
	obsMatrix = np.array([[1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.5, 0.0, 0.5], [0.0, 0.0, 0.5, 0.5, 0.0], [0.0, 0.5, 0.0, 0.0, 0.5]])
	states = S, A, B, C, D = 0, 1, 2, 3, 4

	print("Printing probabilities of each observations for lambda 2:")
	print(math.log(forward(pi, transMatrix, obsMatrix, [A, D, C, B, D, C, C, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [B, D, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [B, C, C, B, D, D, C, A, C, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [A, C, D, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [A, D, A, C, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [D, B, B, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [A, B, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [D, D, B, D, D, B, A, C, C, D, A, B, B, C, D, B, B, B, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [D, B, D, S])))
	print(math.log(forward(pi, transMatrix, obsMatrix, [A, A, A, A, D, C, B, S])))

