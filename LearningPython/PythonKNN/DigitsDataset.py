import numpy
import time
from sklearn import svm
from sklearn import datasets

# Note the Start time
start_time = time.clock()

# Load the digits dataset
# KEYS : ['data', 'target', 'target_names', 'images', 'DESCR']
digits = datasets.load_digits()

# Print the values
print("\nData : \n" + str(digits["data"]) + "\nTarget : \n" + str(digits["target"]));
print("\nTarget Names : \n" + str(digits["target_names"]) + "\nimages : \n" + str(digits["images"]));
print("\nDesc : \n" + str(digits["DESCR"]));

# Create an svc and train it
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier() #svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])  

# Try the svc on the last one
print(str(clf.predict(digits.data[-1:])) + " | " + str(digits.target[-1:]));

# Note the End time and display the result
end_time = time.clock()
print("\nProgram took " + str(end_time-start_time) + " seconds");