import numpy as np
import matplotlib.pyplot as plt

# Create an x-axis that goes from 0 to 10 in steps of 0.1
x=np.arange(0.0,10.0,0.1)

plt.xlabel('x-axis title [units]')
plt.ylabel('y-axis title [units]')

plt.plot(x,x*x,'r-')
plt.show()
