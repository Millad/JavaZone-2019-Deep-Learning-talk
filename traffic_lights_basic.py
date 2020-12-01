# Millad Dagdoni
# Dagdoni.com
import numpy as np

#Init stuff
alpha = 0.8  #how fast do you want to move the slope?
w = np.random.random((3,1)) - 1 #weights
x = np.array([[1,0,0],[0,1,0],[0,0,1]]) #input
y = np.array([1,1,0]).T #Output Wanted
error = 0

#learn
if __name__ == "__main__":
    for step in range(2):
        for i in range(len(x)):
            layer_0_x = x[i:i+1]
            layer_1_pred =(np.dot(layer_0_x, w))
            error = np.sum((layer_1_pred - y[i]) ** 2)
            derivant = alpha * (layer_0_x.T.dot(layer_1_pred - y[i]))
            w -= derivant
            print("ERROR: " +  str(error))

    #Predict
    greenLightsIseeArray = np.array([1,0,0])
    shouldIdriveSumResult = np.sum(np.dot(greenLightsIseeArray, w))
    shouldIdrive = shouldIdriveSumResult > 0
    print("Should you drive now? " + str(shouldIdrive))