import numpy
import time


start=time.time()

# arctan(x) = pi/6
# Thus, Pi = 6*arctan(x)

adj=numpy.sqrt(3)                           # Adjacent to pi/6
opp=1                                       # Opposite to pi/6
n=0
pi=0
x=opp/adj
z=0

#Calculate pi using the Gregory-Leiniz method.

for i in range(1,31):                       

    z=(2*i)-1                               # Ensures 'n' and 'z' remain odd numbers                               
    n=(2*i)-1                               # 
    if(i%2==0):                             # If there remainder of i/2 is zero, n must be even
        n=n*-1                                  #So, make 'n' negative by muliplying by -1 
    pi+=((6*((x**z)/n)))                    #Calculate Pi
    
    print(pi)
    
print ("This programme took")               
print ((time.time()-start),("Seconds"))



