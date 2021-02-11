"""
 This piece of code finds the maximum and minimum values
 in file3.txt
"""
import numpy as np

# I am declaring my filename as a string variable as I will reuse it
filename="file3.txt"

# Open my file. Note, this is bad programming practice as I should have checked
# that the file existed first, but we will come back to this when we think about
# error handling. Let's just assume that the file exists in this direcory.
f = open(filename,"r")


# maximum and minimum variables are going to be initialise below
# to the first value in the file
max=0.0
min=0.0

max=float(f.readline())
min=max

# Line counter (number of data points)
lcount=0

for line in f:
    # This will read the data line-by-line BUT as a string
    datum=float(line)

    if(datum>max):
        max=datum

    if(datum<min):
        min=datum

    # Add one to the line counter
    lcount+=1

range=max-min
print("The maximum of the ",lcount," numbers in the file",filename, "is: ",max)
print("The minimum of the ",lcount," numbers in the file",filename, "is: ",min)
