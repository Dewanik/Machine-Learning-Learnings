import numpy as np

class Neural_Network:
	def __init__(self,i_n,h_n,o_n):
		self.weights_input = 2 * np.random.random((i_n,h_n)) - 1
		self.weights_out = 2 * np.random.random((h_n,o_n)) - 1
		self.h_layers  = np.random.random((h_n,h_n))
		self.o_layers = np.random.random((o_n,o_n))

	#Forward Progations
	
	def predict(self,inputs):
		self.h_layers = 1/(1+np.exp(-np.dot(np.array([inputs]),self.weights_input)))
		self.o_layers = 1/(1+np.exp(-np.dot(self.h_layers,self.weights_out)))
		if self.o_layers[0][0] > self.o_layers[0][1]:
			return (0,0,0)
		else:
			return (255,255,255)


	def train(self,inputs,target):
		y = np.array(target)
		l2_delta =  (y - self.o_layers)*(self.o_layers*(1-self.o_layers))
		l1_delta = l2_delta.dot(self.weights_out.T) * (self.h_layers * (1-self.h_layers))
		self.weights_out += self.h_layers.T.dot(l2_delta)
		self.weights_input += np.array([inputs]).T.dot(l1_delta)
		print(target)
