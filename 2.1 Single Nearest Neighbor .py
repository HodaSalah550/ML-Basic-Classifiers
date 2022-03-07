import numpy as np
import math

#feature vector of unknown pattern
x = np.array([1.8 , -0.56 , 1.51]).reshape(3,1) 
#print("feature vector of unknown pattern: ",x)

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

trans_class1 = np.array([class1['x1'],class1['x2'],class1['x3']]).reshape(10,3)
trans_class2 = np.array([class2['x1'],class2['x2'],class2['x3']]).reshape(10,3)
trans_class3 = np.array([class3['x1'],class3['x2'],class3['x3']]).reshape(10,3)

#print("class 1:", trans_class1, '\n')
#print("class 2:", trans_class2, '\n')
#print("class 3:", trans_class3, '\n')


def Euclidean_distance(training_data,feature_vector):
    euclidean_distances = []
    for row in range(10):
           euclidean_distances.append(math.sqrt((feature_vector[0][0] - training_data[row][0])**2 + (feature_vector[1][0] - training_data[row][1])**2 +(feature_vector[2][0] - training_data[row][2])**2))
    return euclidean_distances   

dclass1 = Euclidean_distance(trans_class1, x)
dclass2 = Euclidean_distance(trans_class2, x)
dclass3 = Euclidean_distance(trans_class3, x)

#To sort the distances from the smallest to the largest
dclass1.sort()
dclass2.sort()
dclass3.sort()

#print("Distances for class 1: ",dclass1, '\n')
#print("Distances for class 2: ",dclass2, '\n')
#print("Distances for class 3: ",dclass3, '\n')

#To find the smallest distance for each class and the minimum between them
Single_nearest_neighbor = {'Class 1':dclass1[0],'Class 2':dclass2[0],'Class 3':dclass3[0]}
print("The unknown pattern belongs to: ",min(Single_nearest_neighbor, key=Single_nearest_neighbor.get))
