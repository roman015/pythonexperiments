"""
Simple Program that uses time module to determine the runtime. 
Doesn't do anything interesting, just code for reference.
"""
import time
import numpy
from sklearn import datasets

# Start the clock
start_time = time.clock()

# Do something
digits = datasets.load_digits()

#End the Clock
end_time = time.clock()

#Calculate the time in seconds
print("\nTime : " + str(end_time - start_time));
