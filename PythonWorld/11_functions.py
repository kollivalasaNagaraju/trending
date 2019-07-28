def myFunction(name="nagaraju"):
   print("my name is "+name)

myFunction()
myFunction("satyanarayana")

#return example

def my_function(x):
  return 5 * x

print(my_function(4))

#recursion example

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\nRecursion Results")
tri_recursion(-1)

#lambda function
print("lambda function")
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

def myLambdaFunction(n):
  return lambda a : a * n

mydoubler = myLambdaFunction(2)

print(mydoubler(11))
print(mydoubler(12))
