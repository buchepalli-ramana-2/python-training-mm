############################################################ importing libraries ################
# method1
import math  ## importing all the methods to your program space
print(math.log(2))
print(math.sin(1))


# method2 - using alias name
#pip install matplotlib
import matplotlib.pyplot as plt
plt.plot([10,20],[30,40])
plt.show()


# method3 - imorting required methods nly
from math import log,tan   # we ar importing required methods only   # we are not aimporting all the methods
print(log(3))