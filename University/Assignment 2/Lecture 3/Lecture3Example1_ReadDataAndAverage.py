# I am declaring my filename as a string variable as I will reuse it
filename="file2.txt"

# Open my file. Note, this is bad programming practice as I should have checked
# that the file existed first, but we will come back to this when we think about
# error handling. Let's just assume that the file exists in this direcory.
f = open(filename,"r")


# initialise the sum to zero
sum=0

for i in range(0,10):
    # This will read the data line-by-line BUT as a string
    datum=f.readline()

    # Before we add to the sum variable, we need to convert our string
    # to a number (in this case an integer)
    sum+=int(datum)

print("The average of the 10 numbers in the file",filename, "is: ",float(sum)/10.0)
