import numpy
import time
from sklearn import datasets

start_time = time.clock()
digits = datasets.load_digits()
end_time = time.clock()

print("DIGITS : \n" + str(digits.keys()) + "\nTime : " + str(end_time - start_time));
