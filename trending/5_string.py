string1 = "hello"
string2 = 'world'
string3 = string1 + string2

print(string1)
print(string2)
print(string3)

string4 = """welcome to string operations"""
print(string4)

string5 = '''welcome to string oprations on 3 single quotes'''
print(string5)

string = "I am learning python"
print("original string :: "+string)
print("[0]" +" :: " + string[0])
print("[0:]" +" :: " + string[0:])
print("[0:3]" +" :: " + string[0:3])
print("[2:7]" +" :: " + string[2:7])

str_op = " String Oprations "
print("orignal string :: "+ str_op)
print("before strip() :: ")
print(len(str_op))
str_op = str_op.strip()
print("after strip() ::")
print(len(str_op))
print("lowercase :: "+str_op.lower())
print("uppercse :: "+str_op.upper())
print("replace :: "+str_op.replace("String", "XXXXXX"))
print("split :: " )
print(str_op.split(" "))

print("string format")
name = "Nagaraju"
age = 23
dob = "01-06-1996"
format_str1 = "My name is {}.Born Date of Birth is {} ,Now age is {}."
format_str2 = "My name is {0}.Born Date of Birth is {2} ,Now age is {1}."
print(format_str1.format(name,dob,age))
print(format_str2.format(name,age,dob))
