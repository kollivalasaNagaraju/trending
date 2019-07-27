#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(x)

a = complex(y)
#b = float(1+1j) #cant convert complex to float
#c = int(2+2j) #can't convert complex to int

print(x)
print(y)
print(z)
print(a)
#print(b)
#print(c)

# print(d) # name 'd' is not defined

print(complex(1,1))
#whitespace = complex("1 + 2j") # ValueError: complex() arg is a malformed string
#passstring = complex("1+j", 2) #TypeError: complex() can't take second arg if first is a string
#passsecondarg  = complex(2, "-2j") #TypeError: complex() second arg can't be a string

