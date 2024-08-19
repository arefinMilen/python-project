# class Animal:
#     # def __int__(self,name):
#     #   self.name = name
#     def showname(self):
#         print("self.name")
#     def sound(self):
#         print("meow meow")
#
# class Human(Animal):
#     # def __int__(self,name):
#    def showname(self):
#     print("self.name")

# obj1 = Human()
# obj1.showname()
# obj1.sound()

# animal = Animal()
# human = Human()

# human.showname()
# animal.showname()


class cat:
    # def __init__(self):
     def sound(self, name):
        self.name= name
        print(f'my {self.name} sound meow,meow!!')

class Dog:
    # def __init__(self):
        def sound(self,name):
            self.name = name
            print(f'my {self.name} sound boww boww')

myCat = cat()
myDog = Dog()
myCat.sound('petCat')
myDog.sound('PetDog')


# try:
#
#   div = 1/0
#
# except:
#     print("your division is not proper way ")
#
# else:
#     print('your result is' ,div)
#     print('your code is correct ')
#
# finally:
#     print("try again your code formation is not correct you need to recheck your program !!")

# import numpy as np
# array = np.array([[ x for x in range(10,1,-2)],[ x for x in range (9,0,-2)]])
# num = np.array([[1,2,2],[3,4,3]])
#
# type(array)
# print(f'n dimention :{array.ndim}')
# print( f'array type :{type(array)}')
# print('dtype:')
# print(array.dtype)
#
# print(num.dtype)
# print("array shape: ")
# print(array.shape)
# print("array size: ")
# print(array.size)
# print("array item size: ")
# print(array.itemsize)
# print("array max : ")
# print(array.max())
# print("array min: ")
# print(array.min())
# print("array std : ")
# print(array.std())
# print("array var : ")
# print(array.var())
# print(f'axis = 0 is {array.mean(axis=0)}')
# print(f'axis = 1 is {array.mean(axis=1)}')

