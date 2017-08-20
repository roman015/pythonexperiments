import numpy
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris();
iris_X = iris.data
iris_Y = iris.target

# Split iris data in train and test data
# A random permutation, to split the data randomly
numpy.random.seed(0)
indices = numpy.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_Y[indices[:-10]]
iris_X_test  = iris_X[indices[-10:]]
iris_y_test  = iris_Y[indices[-10:]]

# Create and fit a nearest-neighbor classifier
knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train) 

#print(iris_X_test[0:1]);
#print("\nNearest Neighbour: ");
#print(knn.kneighbors(iris_X_test[0:1]))

print("IRIS Predicted : ");
print(knn.predict(iris_X_test))

print("IRIS Actual : ");
print(iris_y_test)