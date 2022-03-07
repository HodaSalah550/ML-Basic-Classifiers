import numpy as np
import random

#Feature Vectors for class1
class1 = [[1.58, 2.32, -5.80],
          [0.67, 1.58, -4.78],
          [1.04, 1.01, -3.63],
          [-1.49, 2.18, -3.39], 
          [-0.41, 1.21, -4.73],
          [1.39, 3.16, 2.87],
          [1.20, 1.40, -1.89],
          [-0.92, 1.44, -3.22],
          [0.45, 1.33, -4.38],
          [-0.76, 0.84,-1.96]]


#Feature Vectors for class2
class2 = [[0.21, 0.03, -2.21],
          [0.37, 0.28, -1.8],
          [0.18, 1.22, 0.16],
          [-0.24, 0.93, -1.01],
          [-1.18, 0.39, -0.39],
          [0.74, 0.96, -1.16],
          [-0.38, 1.94, -0.48],
          [0.02, 0.72, -0.17],
          [0.44, 1.31, -0.14],
          [0.46, 1.49, 0.68]]

#print("class 1:", class1, '\n')
#print("class 2:", class2, '\n')

#the unknown pattern
x = np.array([1.8 , -0.56 , 1.51])

c = 0.1
k = 1
w0 = random.uniform(0,1)
w1 = random.uniform(0,1)
w2 = random.uniform(0,1)
w3 = random.uniform(0,1)

#print ("w0 before iterations",w0)
#print ("w1 before iterations",w1)
#print ("w2 before iterations",w2)
#print ("w3 before iterations",w3)

EndOfIterations=0
while (EndOfIterations <=100):
    EndOfIterations = EndOfIterations + 1

for i in range (10):
    D = w0+(w1*class1[i][0])+(w2*class1[i][1])+(w3*class1[i][2])

if (D>0):
    print ("We don't need more iterations for w's values")

else:
    w0=w0+(c*k)
    w1=w1+(c*class1[i][0])
    w2=w2+(c*class1[i][1])
    w3=w3+(c*class1[i][2])
    
for j in range (10):
    D = w0+(w1*class2[j][0])+(w2*class2[j][1])+(w3*class2[j][2])

if (D<0):
    print ("We don't need more iterations for w's values")
    
else:
    w0=w0-(c*k)
    w1=w1-(c*class2[j][0])
    w2=w2-(c*class2[j][1])
    w3=w3-(c*class2[j][2])
    
#print ("w0 after iterations",w0)
#print ("w1 after iterations",w1)
#print ("w2 after iterations",w2)
#print ("w3 after iterations",w3)

Classification = w0+(w1*x[0])+(w2*x[1])+(w3*x[2])

if (Classification>0):
    print ("The unkown pattern x is belongs to class1")

else:
    print ("The unkown pattern x is belongs to class2")
