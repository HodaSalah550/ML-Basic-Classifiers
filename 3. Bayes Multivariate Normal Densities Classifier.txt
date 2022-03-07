import numpy as np
from numpy.linalg import inv
import pandas as pd

#Feature Vectors for class1
class1 = {
    'x1': [1.58, 0.67, 1.04, -1.49, -0.41, 1.39, 1.20, -0.92, 0.45, -0.76],
    'x2': [2.32, 1.58, 1.01, 2.18, 1.21, 3.16, 1.40, 1.44, 1.33, 0.84],
    'x3': [-5.80, -4.78, -3.63, -3.39, -4.73, 2.87, -1.89, -3.22, -4.38, -1.96]
}

#Feature Vectors for class2
class2 = {
    'x1': [0.21,0.37,0.18,-0.24,-1.18,0.74,-0.38,0.02,0.44,0.46],
    'x2': [0.03,0.28,1.22,0.93, 0.39,0.96,1.94,0.72,1.31,1.49],
    'x3': [-2.21,-1.8,0.16,-1.01,-0.39,-1.16,-0.48,-0.17,-0.14,0.68]
}

#Feature Vectors for class3
class3 = {
    'x1':[-1.54,5.41,1.55,1.86,1.68,3.51,1.40,0.44,0.25,-0.66],
    'x2':[1.17,3.45,0.99,3.19,1.79,-0.22,-0.44,0.83,0.68,-0.45],
    'x3':[0.64,-1.33,2.69,1.51,-0.87,-1.39,0.92,1.97,-0.99,0.08]
}

#print("class 1:", class1, '\n')
#print("class 2:", class2, '\n')
#print("class 3:", class3, '\n')

#the unknown pattern
x = np.array([1.8 , -0.56 , 1.51])

#mean vector for class1
df1 = pd.DataFrame(class1)
m11 = df1['x1'].mean()
m12 = df1['x2'].mean()
m13 = df1['x3'].mean()
mean1 = np.array([m11,m12,m13])

#mean vector for class2
df2 = pd.DataFrame(class2)
m21 = df2['x1'].mean()
m22 = df2['x2'].mean()
m23 = df2['x3'].mean()
mean2 = np.array([m21,m22,m23])

#mean vector for class3
df3 = pd.DataFrame(class3)
m31 = df3['x1'].mean()
m32 = df3['x2'].mean()
m33 = df3['x3'].mean()
mean3 = np.array([m31,m32,m33])

#print ("mean for class 1:", mean1, '\n')
#print ("mean for class 2:", mean2, '\n')
#print ("mean for class 3:", mean3, '\n')

#Covariance Matrix for class1
class1_Data = np.array([class1['x1'],class1['x2'],class1['x3']])
covMatrix1 = np.cov(class1_Data,bias=True)

#Covariance Matrix for class2
class2_Data = np.array([class2['x1'],class2['x2'],class2['x3']])
covMatrix2 = np.cov(class2_Data,bias=True)

#Covariance Matrix for class3
class3_Data = np.array([class3['x1'],class3['x2'],class3['x3']])
covMatrix3 = np.cov(class3_Data,bias=True)

#print ("covariance for class 1:", covMatrix1, '\n')
#print ("covariance for class 2:", covMatrix2, '\n')
#print ("covariance for class 3:", covMatrix3, '\n')

#defining discriminant function, then
#substituting mean and variance in the discriminant function for each class
def discriminant_func(covMatrix,feature_vector,mean):
    ainv_covMatrix = np.linalg.inv(covMatrix)
    row_vector = -0.5*np.log(np.linalg.det(covMatrix)) - 0.5*(feature_vector - mean)
    col_vector = np.dot(ainv_covMatrix,(feature_vector - mean)) + np.log(1/3)
    return np.dot(row_vector,col_vector)

g1 = discriminant_func(covMatrix1,x,mean1)
g2 = discriminant_func(covMatrix2,x,mean2)
g3 = discriminant_func(covMatrix3,x,mean3)

#print(g1)
#print(g2)
#print(g3)

#comparing the discriminant functions with each other
if (g1 > g2) & (g1 > g3):
    print('The classification result for the unknown pattern x is that it belongs to class 1')

elif (g2 > g1) & (g2 > g3):
    print('The classification result for the unknown pattern x is that it belongs to class 2')

else:
    print('The classification result for the unknown pattern x is that it belongs to class 3')

