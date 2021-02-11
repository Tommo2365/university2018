import numpy
import time


start=time.time()

# arctan(x) = pi/6
# Thus, Pi = 6*arctan(x)

adj=numpy.sqrt(3)                           # Adjacent to pi/6
opp=1                                       # Opposite to pi/6
r=0 
n=0
pi=0
x=opp/adj
z=0


#Calculate pi using the Gregory-Leiniz method.

for i in range(1,26):                       

    z=(2*i)-1                               # Ensures 'n' and 'z' remain odd numbers                               
    n=(2*i)-1                               # 
    r=((-1)**i)                             # When 'i' is an odd number 'r' will be -ive and +ive when 'i' is even                                                           
    pi+=(6*(-r*((x**z)/n)))                 # Calculating Pi
    
    print(pi)                               # Execute conditions
    
print ("This programme took")               # Print how long it took to procces code 
print ((time.time()-start),("Seconds"))     # Discription of units of time

