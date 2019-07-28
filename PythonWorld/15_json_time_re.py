import datetime

x = datetime.datetime.now()
print(x)

print("\n")

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("\n")

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if (x):
  print("YES! We have a match!")
else:
  print("No match")
