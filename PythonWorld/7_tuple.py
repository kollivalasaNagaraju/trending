myTuple = (1,2,3,4,5)
print(myTuple)
print(myTuple[0])
#myTuple[0] = "one" #TypeError: 'tuple' object does not support item assignment
#print(myTuple)
for x in myTuple:
  print(x)

print(len(myTuple))


#myTuple = ("1", "2", "3")
#del myTuple #del keyword can delete the tuple completely
#print(myTuple)#NameError: name 'myTuple' is not defined

myTuple1 = tuple((1,2,3))
print(myTuple1)

myTuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
pos = myTuple.count(5)
print(pos)

index = myTuple.index(3)
print(index)
