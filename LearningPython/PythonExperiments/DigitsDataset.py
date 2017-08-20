import time
import numpy
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

# Adjust these values to adjust the size of training and test sets
numTest = -1500 # The last ones

# Note the Start time
start_time = time.clock()

# Load the digits dataset
# KEYS : ['data', 'target', 'target_names', 'images', 'DESCR']
digits = datasets.load_digits()

# Print the values
print("\nData : \n" + str(digits["data"]) + "\nTarget : \n" + str(digits["target"]));
print("\nTarget Names : \n" + str(digits["target_names"]) + "\nimages : \n" + str(digits["images"]));
print("\nDesc : \n" + str(digits["DESCR"]));

# Create an clasifier and train it
clf = KNeighborsClassifier()
clf.fit(digits.data[:numTest], digits.target[:numTest])  

# Try the classifier on the last one in the dataset
predicted = clf.predict(digits.data[numTest:])
target = digits.target[numTest:]

# Display the results
print("Predicted : " + str(predicted) + "\nActual : " + str(digits.target[numTest:]));

# Calculate the number of digits predicted correctly
numSuccess = 0
for pred,trgt in zip(predicted,target) :
    if(pred == trgt) : 
        numSuccess+=1

print("\nSizeof Test Set : " + str(-1*numTest) + "\nSizeof Training Set : " + str(len(digits.data)+numTest) + "\n" )
print("Success rate : " + str(numSuccess/len(target) * 100))
# Note the End time and display the result
end_time = time.clock()
print("\nProgram took " + str(end_time-start_time) + " seconds");