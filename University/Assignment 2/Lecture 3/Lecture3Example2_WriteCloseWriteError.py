# Open a file, newfile.txt. If the file does not exist, open a new file (because we use w+)
f=open("anotherfile.txt","w+")
f.write("The quick brown fox...")
f.close()
f.write("...jumped over the lazy dog"
