# Machine Learning Classification Techniques
## Applying diffirent ways for classifying the same undefined pattern for the same 3 classes each class with 10 samples, then comparing the results in each technique
## The codes uses 3 classes, each class has 10 samples.
### 1. Bayes -For the Normally Distributed Classes- : 1.1 Univariate (1D vector) 1.2 Multivariate (2D or more) 
#### By using  an equation after calculating mean, variance, and covariance.

### 2. Nearest Neighbour: 2.1 Single Nearest Neighbour 2.2 K-Nearest Neighbour
#### By calculating distance between the unkown value and each sample then determine wich class is the closest.

### 3. Adaptive Decision Boundary:
#### The Bayesian decision procedures are optimal decision procedures if the conditional densities of the classes are known. If the densities are not known, 
#### nearest neighbor techniques can be used. However, experimentation may be required to choose K and the set of reference samples. Classification may be time 
#### consuming if the number of reference samples is large.
#### An alternative approach is to assume that the functional form of the decision boundary between each pair of classes is linear and we have to find that linear 
#### decision boundary.
#### In this technique, during the training phase, samples are presented to the current form of the classifier. Whenever a sample is correctly classified, no change 
#### made in the weights, but when a sample is incorrectly classified, each weight is changed in whichever direction will tend to correct the output, D.

### 4. Adaptive Discriminant Functions:
#### Another approach to classification when there are more than two classes is to drive a separate linear discriminant function for each class, and choose 
#### the class which has the largest discriminant function.
#### If there are N classes and M features, then the set of linear discriminant functions is:
#### D1 = w01 + w11 x1 + w21 x2 + ….…. + wM1 xM
#### D2 = w02 + w12 x1 + w22 x2 + ……… + wM1 xM
#### .
#### DN = w0N + w1N x1 + w2N + …………. + wMN xM
#### The technique for adapting the weights in these discriminant functions classification algorithm is as follows:
#### Whenever a sample X is classified as class Cj when it should have been classified as class Ci, the new weights for the two corresponding discriminant functions 
#### (Di and Dj) are adjusted as follows:
#### wmi = wmi + C xm,
#### wmj = wmj – C xm
#### where m = 1, 2, ……., M and 
#### w0i = w0i + CK, w0j = w0j – CK
#### No change is made in the discriminant functions for classes other than Ci and Cj.
#### This procedure has the effect of increasing Di for the class that should have been chosen and decreasing Dj for the class that was chosen but 
#### should not have been.
#### There is no reason to change the weights in the other discriminant functions.

### 5. Minimum Squared Error (MSE) Classification Technique:
#### In the adaptive decision boundary and adaptive discriminant function techniques, finding the decision boundary may require many iterations. In addition, the
#### adaptive algorithms terminate when they find the first set of weights that correctly classifies the training data, which might not correspond to what constitutes
#### a good decision boundary.
#### The minimum squared error (MSE) classification procedure does not require iterations and it may produce decision boundaries that more appealing than those
#### produced by the adaptive decision boundary techniques.
##### The minimum squared error algorithm uses a single discriminant function, regard less of the number of classes.
#### Let the true class of Xi be represented by di, which can have any numerical value. We want to find a set of weights wj, j= 0, 1, 2, …, M for a single linear
#### discriminant function:
#### D(Xi) = w0 + w1
#### xi1 + w2
#### xi2 + … + wM xiM
#### Such that D(Xi) = di for all the samples of class i.
#### In general, this will not be possible, but by properly choosing the weights w0, w1, w2, …, wM, the sum of the squared differences between the set of desired
#### values di and the actual values D(Xi) can be minimized. The sum of squared errors E is:
#### E = (D(X1)- d1)2 + (D(X2) – d2)2 + … + (D(Xi) – di)2+ … + (D(XV) – dV)2
#### The values of the weights that minimize E may be found by computing the partial derivatives of E with respect to each of the wj, setting each derivative to zero,
#### and solving for the weights.
#### Since E is a quadratic function of the wj, the derivatives will be linear in the wj, so the problem is reduced to solving a set of M+1 linear equations for the
#### M+1 weights w0, w1, …, wM.
#### When there are N classes, this technique still uses a single set of weights rather than N or N(N-1)/2 of them as in the two methods described previously for 
#### classes.

