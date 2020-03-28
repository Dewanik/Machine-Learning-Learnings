from random import *
import numpy as np
import matplotlib.pyplot as plt
inputs = []
weights  = [0,0]
label = []
predicts = []

for i in range(100):
	inputs.append([randint(1,100),randint(1,100)])
	if inputs[i][1] > inputs[i][0]:
		label.append(1)
	else:
		label.append(-1)

for i in range(len(weights)):
	weights[i] = randint(-1,1)

def sign(n):
	if n >=0:
		return 1
	else:
		return -1

def perceptron(inputs):
	wsum = 0
	for i in range(len(weights)):
		wsum += inputs[i] * weights[i]
	output = sign(wsum)
	return output

def train(inputs,label,learn_rate):
	predict = perceptron(inputs)
	error = label - predict
	for i in range(len(weights)):
		weights[i] += error * inputs[i] * learn_rate
	predicts.append(perceptron(inputs))
	print('''#Error:{0}
        #Weights : {4}
        #Input:{1}
        #Predict:{2}
        #target:{3}'''.format((label-perceptron(inputs)),inputs,perceptron(inputs),label,weights))

for i in range(len(inputs)):
	print(i)
	train(np.array(inputs[i]),label[i],0.01)
ercount = 0;
for i in range(len(inputs)):
    plt.plot(range(0,100),range(0,100),linewidth=5)

    if inputs[i][1] > inputs[i][0]:
        if label[i] == predicts[i]:
            plt.scatter(inputs[i][0], inputs[i][1], color='blue',s=100)
        else:
    
            plt.scatter(inputs[i][0], inputs[i][1], color='red',s=100)
            ercount += 1
    else:
        if label[i] == predicts[i]:
           plt.scatter(inputs[i][0], inputs[i][1], color='green',s=100)
        else:
           ercount += 1
           plt.scatter(inputs[i][0], inputs[i][1], color='red',s=100)
print("Total NotClassifiedProperly:{0}".format(ercount))
plt.show()

	

	




