# Open a file, newfile.txt. If the file does not exist, open a new file (because we use w+)
f=open("newfile.txt","w+")
f.write("Something you want to write")
