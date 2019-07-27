print("welcome to conditional statements") 
a = 10
b = 20
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print("while loop")
i = 1
while i < 6:
  print(i)
  i += 1

print("while loop and break")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("while loop and continue")

i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)

print("for loop")
numbers = [10,11,12,13,14]
for number in numbers:
  print(number)

print("for loop with range 1")
for x in range(6):
  print(x)

print("for loop with range 2")
for x in range(2,6):
  print(x)

print("for loop with range 3")
for x in range(2,6,2):
  print(x)

print("for loop with range 4 with else")

for x in range(6):
  print(x)
else:
  print("Finally finished!")
