# Millad Dagdoni
# Dagdoni.com
# 02.03.2018

alpha = 0.1
w = 0.5
x = 4
y = 8

for step in range(10):
    pred = x * w
    error = (pred  - y) ** 2
    derivative_of_error = alpha * x * (pred - y)
    w -= derivative_of_error
    print("ERROR: " +  str(error) + " PRED: " + str(pred))
