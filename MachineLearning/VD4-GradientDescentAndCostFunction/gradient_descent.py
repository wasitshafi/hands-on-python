import numpy as np

# basics of gradient_descent, it includes some mathematical formulas
def gradient_descent(x, y):
  # we can vary these two parameters to get the best results
  iteration = 10000
  learning_rate = .0001
  
  m_curr = b_curr = 0
  n = len(x)
  
  for i in range(iteration):
    y_predicted = m_curr * x + b_curr # y = mx + c
    cost = 1/n * sum((val** 2 for val in (y - y_predicted)))
    md = -(2/n) * sum(x * (y - y_predicted)) # derevative of m based on formula
    bd = -(2/n) * sum(y - y_predicted)
    m_curr = m_curr - learning_rate * md # new values
    b_curr = b_curr - learning_rate * bd
    print("m {},   b{},   iteration{},   cost {}".format(m_curr, b_curr, i, cost)) # our cost should be decreasing 
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)