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
#assume x belongs to class1

c = 0.1
k = 1

w01 = random.uniform(0,1)
w11 = random.uniform(0,1)
w21 = random.uniform(0,1)
w31 = random.uniform(0,1)

w02 = random.uniform(0,1)
w12 = random.uniform(0,1)
w22 = random.uniform(0,1)
w32 = random.uniform(0,1)

#print ("w01 before iterations",w01)
#print ("w11 before iterations",w11)
#print ("w21 before iterations",w21)
#print ("w31 before iterations",w31)

#print ("w02 before iterations",w02)
#print ("w12 before iterations",w12)
#print ("w22 before iterations",w22)
#print ("w32 before iterations",w32)

for i in range (10):
        D1 = w01 + (w11*class1[i][0]) + (w21*class1[i][1]) + (w31*class1[i][2]) 
        D2 = w02 + (w12*class1[i][0]) + (w22*class1[i][1]) + (w32*class1[i][2]) 

if (D1 > D2):
        print ("Before iterations, \n The unkown pattern x belongs to class1")

else:
    w01=w01+(c*(D1-1))
    w11=w11+(c*(D1-1)*class2[i][0])
    w21=w21+(c*(D1-1)*class2[i][1])
    w31=w31+(c*(D1-1)*class2[i][2])

    w02=w02-(c*(D2-0))
    w12=w12-(c*(D2-0)*class2[i][0])
    w22=w22-(c*(D2-0)*class2[i][1])
    w32=w32-(c*(D2-0)*class2[i][2])

for i in range (10):
        D1 = w01 + (w11*class1[i][0]) + (w21*class1[i][1]) + (w31*class1[i][2]) 
        D2 = w02 + (w12*class1[i][0]) + (w22*class1[i][1]) + (w32*class1[i][2]) 

if (D1 > D2):
        print ("After iterations, \n The unkown pattern x belongs to class1")

else: 
        print ("After iterations, \n The unkown pattern x belongs to class2")
