mydist = {
	"name":"nagaraju",
	"age":23,
	"dob":"01-06-1996"
}
print(mydist)
print(mydist["name"])
print(mydist.get("age"))
mydist["name"] = "Nagaraju Kollivalasa"
print(mydist["name"])
print("\n")
for key in mydist:
  print("key :: "+key)
  print("  value :: ")
  print(mydist[key])


print(mydist.values())
print(mydist.keys())
print("\n")
for key, value in mydist.items():
  print(key, value)

print("\n")
if "name" in mydist:
  print("Yes, 'name' is one of the keys in the mydist dictionary")
else:
   print("No")

print("\n")
print(len(mydist))

print("\n")
mydist["flag"] = True
print(mydist)

print("\n")
mydist.pop("flag")
print(mydist)

print("\n")
mydist.popitem()
print(mydist)

print("\n")
del mydist["age"]
print(mydist)

print("\n")
#del mydist
#print(mydist)

#mydist.clear()
mydist1 = mydist.copy()
mydict2 = dict(mydist)

print("copy of object to another")
print(mydist1)
print(mydict2)

print("\n")
mydict3 = dict(one=1,two=2,three=3)
print(mydict3)

print("\n")
mydict4=dict.fromkeys(("key1","key2"), 1)
print(mydict4)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"brand": "volvo"})
car.update({"color": "White"})
print(car)
