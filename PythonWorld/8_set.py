myset = {"apple", "banana", "cherry"}

print(myset)

for x in myset:
  print(x)

myset.add("orange")
print(myset)
myset.update(["grapes","mango"])
print(myset)

myset.remove("banana")
#myset.remove("banana1") #KeyError: 'banana1'
print(myset)
myset.discard("cherry")
myset.discard("cherry1")
print(myset)
myset.pop()
print(myset)
#myset.clear()
#del myset #name 'myset' is not definedx
print(myset)

myset1 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(myset1)
print("copy to another set")
myset2 = myset1.copy()
print(myset2)
