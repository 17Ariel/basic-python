# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def getName(self):
#         return self.name


# persons=person("Tim",12)
# print(persons)

class dog:
    def __init__(self,name,age):
       self.name=name
       self.age=age
    def bark(self):
        return f'arr arr my name is {self.name} and im {self.age} years old!'


dogName=input('Enter your name:')
dogAge=int(input('Enter your age:'))
Dog=dog(dogName,dogAge)
print(Dog.bark())
