class Person:
  def __init__(self,name, age):
    self.name = name
    self.age = age

  def myfunc(self,gen):
    print("Hello my name is " + self.name+".Gender is a "+gen)
  def myFullName(self,lname):
   print("my full name is "+self.name +" "+lname)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc("male")
#del p1.age  Person instance has no attribute 'age'
#print(p1.age)

#del p1 name 'p1' is not defined
#print(p1)

class Student(Person):
  pass

c1 = Student("nagaraju",23)
print(c1.name)
c1.myFullName("killivalasa")

class Student1(Person):
  def __init__(self,fname,lname):
    self.fullname = fname+" "+lname
    self.fname = fname
    self.lname = lname
    print("child full name is "+self.fname+" "+self.lname)

c2 = Student1("nagaraju","kollivalasa")
print(c2.fname)


class Animal:
    def __init__(self):
      print(self)

a1 = Animal()
