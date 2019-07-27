myList = [1,2,3,4,5]
print(myList)
print(myList[0])
myList[0]= "zero"
print(myList)

for x in myList:
  print(x)


print("length of myList :: ")
print(len(myList))
print("append to myList ::")
myList.append(6)
print(myList)
myList.insert(0,"zero index")#not replace zero index element added to that place shift remaining elemnts
print(myList)
#myList.remove(0) Error o not in myList
myList.remove("zero")
print(myList)
myList.pop()
print(myList)
myList.pop(0)
print(myList)
#del myList[0]
#print(myList)
#del myList
#print(myList) delete elements and reference also
#myList.clear()
#print(myList)
#newMyList = myList.copy()
#print(newMyList)
mylist = list(myList)
print(mylist)

myList1 = list((1,12))
print(myList1)

myList2 = [1,2,3,4,1,6,1]
print(myList2.count(1))
print(myList2.index(1))
print(myList2.index(2))
myList2.reverse()
print(myList2)
myList2.sort()
print(myList2)
