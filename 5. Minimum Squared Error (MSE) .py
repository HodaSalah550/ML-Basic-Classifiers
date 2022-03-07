import numpy as np
import sympy as sm

#Feature Vectors for class1
class1 = [[1.58, 2.32, -5.80],
          [0.67, 1.58, -4.78],
          [1.04, 1.01, -3.63]]

#Feature Vectors for class2
class2 = [[0.21, 0.03, -2.21],
          [0.37, 0.28, -1.8],
          [0.18, 1.22, 0.16]]

#print("class 1:", class1, '\n')
#print("class 2:", class2, '\n')

#the unknown pattern
x = np.array([1.8 , -0.56 , 1.51])

c = 0.1
k = 1

w0 = sm.Symbol('w0')
w1 = sm.Symbol('w1')
w2 = sm.Symbol('w2')
w3 = sm.Symbol('w3')

E = (w0 + w1*class1[0][0] + w2*class1[0][1] + w3*class1[0][2] -1)**2 + (w0 + w1*class1[1][0] + w2*class1[1][1] + w3*class1[1][2] -1)**2 + (w0 + w1*class1[2][0] + w2*class1[2][1] + w3*class1[2][2] -1)**2 + (w0 + w1*class2[0][0] + w2*class2[0][1] + w3*class2[0][2] +1)**2 + (w0 + w1*class2[1][0] + w2*class2[1][1] + w3*class2[1][2] +1)**2 + (w0 + w1*class2[2][0] + w2*class2[2][1] + w3*class2[2][2] +1)**2

dEdw0 = sm.Function("dEdw0")
dEdw1 = sm.Function("dEdw1")
dEdw2 = sm.Function("dEdw2")
dEdw3 = sm.Function("dEdw3")

dEdw0 = sm.diff(E, w0)
dEdw1 = sm.diff(E, w1)
dEdw2 = sm.diff(E, w2)
dEdw3 = sm.diff(E, w3)

#print (dEdw0)
#print (dEdw1)
#print (dEdw2)
#print (dEdw3)

w_values = sm.solve((dEdw0, dEdw1, dEdw2, dEdw3), w0, w1, w2, w3)

print (w_values)        
