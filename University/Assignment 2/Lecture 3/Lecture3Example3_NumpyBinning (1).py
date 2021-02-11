# This program reads a data file which is read in
# and uses numpy to group the data into "nbins" bins
# which is also read in
# Usage:
# python Lecture3Example3_NumpyBinning.py
# You will be prompted to enter the filename and the
# number of bins you require. In that way, the code is
# more general and you can use it to analyse any data
# file with a single column of data
import numpy
import os

filename = input("Enter the filename (you must NOT include quotation marks): ")
# The number of bins that we are going to
nbins = int(input("Enter the number of bins: "))


# Having fewer than 1 bins is not sensible. We can check for user input error.
if(nbins<1):
    # Print an error to the screen
    print("\n***Error: the number of bins cannot be less than 1***\n\n")
    # And exit
    quit()

print("")
# Some output so the user can see the file and nbins has been read correctly
print("Analysing file,",filename," by grouping data into ",nbins," bins")

# A print statement to divide the output
print("--------------------------------------------------------------")


# Double check that the file exists and try to open it
if(os.path.exists(filename)):
    try:
        f=open(filename,"r")
    except:
        print("Could not open the file,",filename)

# At this point, the file should be open


# The next step is to work out the min/max of our data and how many points
# we have
minval=float(f.readline())
maxval=float(minval)

# To store the number of points read in. Starts from 1 because
# we have read in a line above
sumlines=1


# Algorithm to work out how many lines there are in the file
# and the max/min values
for line in darray:
    datum=float(line)

    if(datum<minval):
        minval=datum
    if(datum>maxval):
        maxval=datum

    sumlines+=1

# The range (max-min)
rangedat=maxval-minval

# Let's output some information on our data set
print("")
print("The number of data points is:",sumlines,"\n")
print("The maximum of the data is:",maxval,"\n")
print("The minimum of the data is:",minval,"\n")
print("The range of the data is:",rangedat,"\n")


# Declare an array that can contain the data
data=numpy.zeros(sumlines)

# Start the file again so we can read the data into the array
f.seek(0)

# Sumlinnes here is going to be the array lookup
sumlines=0
for line in f:
    data[sumlines]=float(line)
    sumlines+=1

f.close


print(numpy.histogram(data,bins=nbins,range=(minval,maxval)))
