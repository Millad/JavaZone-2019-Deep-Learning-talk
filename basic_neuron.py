# Millad Dagdoni
# Dagdoni.com

alpha = 0.1
w = 0.5
x = 4
y = 8

for step in range(10):
    pred = x * w
    error = (pred  - y) ** 2
    derivative = alpha * x * (pred - y)
    w = w - derivative
    print("ERROR: " +  str(error) + " PRED: " + str(pred))
