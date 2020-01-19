# Millad Dagdoni
# Dagdoni.com
import numpy as np

#Init stuff
alpha = 0.2  #how fast do you want to move the slope?
np.random.seed(1)
w = np.random.random((3,3)) - 1 #weights
x = np.array([[1,0,0],[0,1,0],[0,0,1]]) #input
y = np.array([1,1,0]).T #Output Wanted

#learn
for step in range(20):
    error = 0
    for i in range(len(x)):
        layer_0_x = x[i:i+1]
        layer_1_pred =(np.dot(layer_0_x, w))
        error += np.sum((layer_1_pred - y[i:i+1]) ** 2)
        derivant = alpha * (layer_0_x.T.dot(layer_1_pred - y[i:i+1]))
        w -= derivant
        print("ERROR: " +  str(error))

#Predict
lightsIseeArray = np.array([1,0,0])
shouldIdriveSumResult = np.sum(np.dot(lightsIseeArray, w))
shouldIdrive = shouldIdriveSumResult > 0
print("Should you drive now? " + str(shouldIdrive))
