# Millad Dagdoni
# Dagdoni.com
# 02.03.2018
import numpy as np

# Settings
learning_rate = 0.1
training_steps = 20

# Training data
# Each row is one traffic-light situation:
# [green, yellow, red]
x = np.array([
    [1, 0, 0],  # green
    [0, 1, 0],  # yellow
    [0, 0, 1],  # red
])

# Correct answers:
# 1 = drive
# 0 = do not drive
y = np.array([
    [1],
    [1],
    [0],
])

# Random starting weights
weights = np.random.randn(3, 1)

# Training loop
for step in range(training_steps):
    total_error = 0

    for i in range(len(x)):
        input_data = x[i:i+1]
        correct_answer = y[i:i+1]

        prediction = np.dot(input_data, weights)

        error = prediction - correct_answer
        total_error += np.sum(error ** 2)

        gradient = input_data.T.dot(error)
        weights -= learning_rate * gradient

    print("Step:", step, "Error:", total_error)

# Prediction
green_light = np.array([[1, 0, 0]])

result = np.dot(green_light, weights)
should_drive = result[0][0] > 0.5

print("Prediction score:", result[0][0])
print("Should you drive now?", should_drive)
