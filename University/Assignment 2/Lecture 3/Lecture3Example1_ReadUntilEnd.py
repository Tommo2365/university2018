"""
 As the aim of this piece of code is to find the mean and standard deviation
 from a set of data. We equation for the standard deviation is:

 sigma = (1/N)*sum_{i=1}^N (x_i - mean)^2

 Therefore, we need to know the mean before we can calculate this sum, hence
 we will either have to store the data in an array, or re-read the file.
 Re-reading of files is generally slower because it involves reading data
 from the hard disk. Storing data in an array means that the information
 is stored in RAM and is transacted to the CPU much more quickly.
 As the amount of information is small and we are more interested in reading
 and manipulating files in this session, this code re-reads the data from the
 file.
"""
import numpy as np

# I am declaring my filename as a string variable as I will reuse it
filename="file3.txt"

# Open my file. Note, this is bad programming practice as I should have checked
# that the file existed first, but we will come back to this when we think about
# error handling. Let's just assume that the file exists in this direcory.
f = open(filename,"r")


# initialise the sum to zero
sum=0.0
# Line counter (number of data points)
lcount=0


for line in f:
    # This will read the data line-by-line BUT as a string
    datum=float(line)

    # Before we add to the sum variable, we need to convert our string
    # to a number (in this case a float)
    sum+=float(datum)
    # Add one to the line counter
    lcount+=1

mean=sum/float(lcount)

print("The average of the ",lcount," numbers in the file",filename, "is: ",mean)

# Put the object file back to the beginning so the data can be read again
f.seek(0)

# Variable to store the sum of the square deviation
sumsqdev=0.0

for line in f:
    # This will read the data line-by-line BUT as a string
    datum=float(line)

    # NOTE: we don't need to count the number of lines, we did that last time
    sumsqdev+=(datum-mean)**2

print("The standard deviation of the ",lcount," numbers in the file",filename, "is: ",np.sqrt(sumsqdev/float(lcount)))
