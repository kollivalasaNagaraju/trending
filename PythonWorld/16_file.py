f = open("python_doc.txt","r") # if file not exist error is:: No such file or directory: 'demofile.txt'

#print(f.read()) - complete data comes
#print(f.read(5)) - 5 is number of characters
#print(f.readline()) - single line comes

"""for x in f:
  print(x) line by line using for loop"""
#f.close() - close file

f = open("demofile.txt", "w")
f.write("Now the file has more content!")
f.close()

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()



import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

os.mkdir("myfolder")
os.rmdir("myfolder")
#The system cannot find the file specified: 'myfolder'
