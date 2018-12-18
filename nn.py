import numpy as np

#Sigmoid Function/ Activation of Neuron
def nonlin(x, deriv=False):
    if (deriv == True):
        return (x * (1 - x))
    return 1 / (1 + np.exp(-x))

print "@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print "@Executing Neural Network!@"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print ""

#Import Dataset using numpy
dataset = np.genfromtxt ('data.csv', delimiter=",", dtype=float)

#Input Data (TEST)
X = dataset[:,:-1]
#Turn input into array
X = np.asarray(X)

#Output Data
y = []
for d in dataset[:,-1]:
    if d == 1:
        y.append(1)
    else:
        y.append(0)
#Turn output into array
y = np.asarray(y)
#Turn Data to coloumn for Input
y = y[np.newaxis].T
#Initalize weights of neural Network
np.random.seed(1)

#2 Layers of Weights
#30 input nodes not including results attribute
#4 Nodes hidden Layer
#1 Output Node
syn0 = 2 * np.random.random((30, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

"""
    Loop trains the neural Network
    Passes every Data
    Evaluates the Error
    Updates the Weights
"""

for i in xrange(80):
    l0 = X
    #Tried to apply Loop here for X to try solve the output issue
    #Loop seems to either break the program or breaks the decreasing error rate
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l2_error = y - l2

    if (i % 1) == 0:
        print "Error: " + str(np.mean(np.abs(l2_error)))

    l2_delta = l2_error * nonlin(l2, deriv=True)

    l1_error = l2_delta.dot(syn1.T)

    l1_delta = l1_error * nonlin(l1, deriv=True)

    #Values stored for every link in syn0 and syn1
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print "Error OUTPUT"

#Because we use 1 output node we loop for results
#If predicted result is above 0.5 then 1 else 0
counter = 0
for p in range(len(l2)):
    if (l2[p] > 0.5) and (y[p] == 1):
        counter = counter+1
    elif (l2[p] <= 0.5) and (y[p] == 0):
        counter = counter+1

print counter/len(l2)
print l2
