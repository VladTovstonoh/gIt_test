"""
 Написать функцию которая будет добавлять 2 числа
2) Модифицировать функцию (калькулятор) , которая будет принимать число и знак операции, и в зависимости от этого выполнять операцию

--
Написать функцию, которая будет принмать списки, а не строки
"""
"""
def function(num1,num2):
    return num1 + num2
print(function(12,23))

def calculator(num1,operation,num2):
    if operation == '-':
        return num1 - num2
    elif operation == '+':
        return num1 + num2
    elif operation == '/':
        return num1 / num2
    elif operation == '*':
        return num1 * num2
    elif operation == '**':
        return num1 ** num2
    elif operation == '//':
        return num1 // num2
    elif operation == '%':
        return num1 % num2
print(calculator(89,"**",4))
"""
"""
def list_proceed(our_list1,our_list2, number=5,):
    print("Что сделать, контактенация или умножения на число?")
    if input() == "к":
        return our_list1 + our_list2
    elif input() == "у":
        print("What list you want multiply 1/2")
        if input() == 1:
            return our_list1 * number
        elif input() == 2:
            return our_list2 * number
    else:
        print("Error")

def print_list(list1):
    print("How you want print your list?")
    if input() == "i":
        for i in list1:
            print(i)
    elif input() == "s":
        print(list1)
print(list_proceed([23,45,65,89],[34,5,98,2]))
print_list([82,56,34,7])

"""
"""
написать функцию, которая принимает *args **kwargs

args: 1) Считаем суму всех элементов массива
      2) calculate avg
      3) выводим все аргументы в консоль, находим max and min element
      4) --- красиво печатаем
kwargs:        
1) выводит все ключи и значения из словаря в цикле
"""
"""
def filter_function(*args):
    new_list = []
    for arg in args:
        if isinstance(arg, int) or isinstance(arg, float):
            new_list.append(arg)
    print(f"Your list after iterations-{len(new_list)}")
    print(new_list)
    return new_list
filter_function(23,434,54,76,"fsdgfhd",(3232,43))


def function(*args,**kwargs):
    filter_list = filter_function(*args)
    sum_list =  sum(filter_list)
    avg_list = sum_list / len(filter_list)
    print(*args, min(filter_list), max(filter_list), sum_list, avg_list,sep= "\n")
function(323,43,76,"47hfdjxkf",(324,"dshkg",32),32.43)
"""
"""
my_data = [i**2 for i in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(my_data)

# Стоит задача : применить функцию корня к каждому элементу

# Solution #1
new_list = []
for r in my_data:
    r **= 0.5
    new_list.append(r)
print(new_list)
"""
"""
Task:
1) Generate the list of random numbers in inputed range  --> F1
2) Filter the list of random numbers by inputed condition --> F2 + F3 ??
3) Iterate through the list and apply the function to each element (on your choice) --> F4   

H/W
Additional requirements:
1) Use decorators for F1, F2, F3, F4
2) Beautify the output
3) Use map, filter
"""

"""
import random


def generate_numbers():
    start = int(input("Input the start number:"))
    end = int(input("Input the end number:"))
    ammount_of_numbers = int(input("Input the ammount of numbers :"))
    return [random.randint(start, end) for i in range(ammount_of_numbers)]


# print(generate_numbers())
numbers = generate_numbers()


def filter_condition(num):
    return num ** 0.5 > 20


new_numbers = list(filter(filter_condition, numbers))


def map_data(num):
    return num ** 3


new_numbers_1 = list(map(map_data, new_numbers))
print(new_numbers)
print(new_numbers_1)
"""
"""
def foo(x,y):
    return  x,y
def foo_1(x):
    print(x)
print(foo(10,43))
print(foo_1("Hello"))
def foo_2(x,y):
    return x,y
print(foo_2)
function = foo_2
print(function(32,56))
function_2 = lambda x, y: x + y
print(function_2(98, 65)
def foo_5(*args,*,x=12,):
    return x,args
print(foo_5(34))
"""
"""
Task 2   ---> Write a Python function to sum all the numbers in a list.



def sum_all_numbers(num_list: list) -> list:
    # The function sum all the numbers in a list
    if not isinstance(num_list, list):
        print("The data is incorrect!")
        return False
    num_list = list(filter(lambda x: False if type(x) != int else True, num_list))
    return sum(num_list)


print(sum_all_numbers([i for i in range(1, 20, 2)]))
print(sum_all_numbers([i for i in range(1, 13)]))
print(sum_all_numbers([i for i in range(20, 50, 1)]))
print(sum_all_numbers([12, "rer", 67]))
"""
"""
Task 2   ---> Write a Python function to multiply all the numbers in a list. Go to the editor
def multiply_all_numbers(num_list:list,) ->int:
    #The function multiply all the numbers in a list
    multiply_num = 1
    for i in num_list:
         multiply_num *= i
    return multiply_num
print(multiply_all_numbers([i for i in range(1, 13)]))


Task 3   ---> Write a Python program to reverse a string.
def reverse_string(reverse_str:str) ->str:
    #The function reverse a string
    if not isinstance(reverse_str,str):
        print("The data is incorrect!")
        return False
    return reverse_str[::-1]
print(reverse_string("Hello"))
print(reverse_string("2434"))
print(reverse_string(3245))
"""
"""
Task 4   ---> Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def calculate_factorial_number(num:int) ->int:
    #The function calculate the factorial of a number
    factorial = 1
    for i in range(1,num):
        factorial *= i
    return factorial
print(calculate_factorial_number(10))


Task 5  ---> Write a Python function to check whether a number falls in a given range
def contains_only_integers(tup):
    for item in tup:
        if not isinstance(item, int):
            return False
    return True
def check_falls_range(num:int,*args) ->bool:
    #The function check a number falls in a given range
    if not isinstance(num, int) and contains_only_integers(args):
        print("The data is incorrect!")
        return False
    return True if num in range(*args) else False
print(check_falls_range(12,"sd",67))
"""
'''Task 6 -->Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.

def bold_decorator(func):
    def inner(str_bold):
        str_bold = "<b>" + str_bold + "<b>"
        func(str_bold)
    return bold_decorator()
'''
"""

import os
#Написати програму що складається з різних функцій
#Програма має дати користовачу можливість створити або вибрати файл,вибрати йому розширення та можливість записати в нього щось або щось читати

#1.Написати вибір - створення нового файлу або вибрати існуючий файл
#2.Написати функцію, яка при створенні нового файлу дає можливість вибрати розширення
#3.Написати функцію, яка при створенні нового файлу дає можливість записати щось
#4.Написати функцію, яка при виборі існуючого файлу дає можливість прочитати його
#5.Створити  файли з різною інформацією
def menu() ->int:
    choice = input(f"What you want?\n1-create new file\n2-choose file")
    return choice
def create_file():
    name_of_file = input("Print name:")
    ext = input("Print ext")
    new_file = open(f"{name_of_file}.{ext}","x")
def write_to_file():
    name_of_file = input("Print name file")
    print("What you want write?")
    str_input = input()
    with open(name_of_file,"w") as input_file:
        input_file.write(str_input)

def filter_function():
    list_of_files = os.listdir(r"C:\\Users\\User\PycharmProjects\pythonProject")
    filtered_list = []
    for file in list_of_files:
        if  file.endswith(".py") or file.endswith(".txt"):
            filtered_list.append(file)
    return filtered_list

def read_file():
    print(filter_function())
    choose_file = input("Choose the file")
    if choose_file in filter_function():
        with open(choose_file,"r") as reading_file:
            data = reading_file.read()
    return data
    


#create_file()

#write_to_file() #TODO решить проблему со вставкой
#print(filter_function())
#print(read_file())
"""
"""
import csv
name  = ["Victor","Julia","Dima","Anton"]
age = [20,23,18,31]
salary = [12000,21000,30000,25000]
test_data_dict = {
    "name": name,
    "age": age,
    "salary": salary
}
for key, value in test_data_dict.items():
    print(key, value)
with open("test.csv","w") as test_file_csv:
    writer = csv.writer(test_file_csv)
    writer.writerow(test_data_dict.items())
"""
"""
class Student():

    def __init__(self, name, age):  # конструктор
        self.name = name  # атребут класа
        self.age = age

    def study(self):
        return f"{self.name} вчиться"

    def birthday(self):
        self.age += 1

    def info(self):
        return self.name, self.age


Vlad = Student("Vlad", 16)
Egor = Student("Egor", 20)

print(Vlad.name)
print(Vlad.age)
print(Vlad.study())
print(Vlad.info())
"""

"""
# Определяем задачи! --> БАЗА данних людини
# Описание примерного алгоритма этой задачи--> атрибути: name, age, sex, height, weight city, hobby, work, salary,
#                                             iq, family status, education.
# 1) class human-> init -> return-> екземпляр класа
# 2) methods of class: init - initialize all atrs
#                     info -> return all values
#                     input -> get the data from keyboard
# Реализация -->
from typing import Optional
class Human:
    def __init__(self, name: str, age: int, sex: str, height: int, weight: int, city: str, hobbies: Optional[list],
                 works: Optional[list], salary: Optional[float], iq: int, family_status, education):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.city = city
        self.hobbies = hobbies
        self.works = works
        self.salary = salary
        self.iq = iq
        self.family_status = family_status
        self.education = education

    def info(self):
        return f"name = {self.name} ,age = {self.age},sex = {self.sex} ,height =  {self.height},weight = {self.weight},city = {self.city}, hobbiews = {self.hobbies}, works = {self.works},salary = {self.salary},iq = {self.iq},family_status = {self.family_status},education = {self.education}"

    def input(self):
        name = input("Input the name =")
        age = int(input("Input the age ="))
        sex = input("Input the sex =")
        height = int(input("Input the height ="))
        weight = int(input("Input the weight ="))
        city = input("Input the city =")
        hobbies = [input("Input the hobbies =")]
        works = [input("Input the works =")]
        salary = float(input("Input the salary ="))
        iq = int(input("Input the iq ="))
        family_status = input("Input the family_status =")
        education = input("Input the education =")
        return Human(name, age, sex, height, weight, city, hobbies, works, salary, iq, family_status, education)
Human_1 = Human(name="Vlad", age=16, sex="man", height=190, weight=83, city="Vinnytsia", hobbies=["basketball"],
                works=None, salary=None, iq=120, family_status=None, education="School")

print(Human_1.input().info())
#Human_2 = Human(name="Vlad", age=16, sex="man", height=190, weight=83, city="Vinnytsia", hobbies=["basketball"],
                #works=None, salary=None, iq=120, family_status=None, education="School N 22")
"""
"""
class Vector:
    def __init__(self,x1:int,x2:int,y1:int,y2:int):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    # This function add  two vectors
    def addition(self) -> str:
        addition =  self.x1 + self.y1, self.x2 + self.y2
        return f"Addition of the vectors: {addition}"

    # This function subtract two vectors
    def subtraction(self) -> str:
        subtraction = self.x1 - self.y1, self.x2 - self.y2
        return f"Subtraction of the vectors: {subtraction}"

    # This function find the length of two vectors
    def vectors_length(self) -> str:
        return f"The length of Vector x = {(self.x1 ** 2 + self.x2 ** 2)** 0.5},\nThe length of Vector y = {(self.y1 ** 2 + self.y2 ** 2)** 0.5}"

    # This function define  are vectors collinear
    def collinear_vectors(self) ->str:
        if self.x1 / self.y1 == self.x2 / self.y2:
            return "This vectors are collinear"
        return "This vectors are not collinear"

    # This function find dot_product_of_vectors
    def dot_product_of_vectors(self) -> str:
        dot_product_vectors =  self.x1 * self.y1 + self.x2 * self.y2
        return f"Dot product of vectors: {dot_product_vectors}"

    # This function print info of two vectors
    def info(self) -> str:
        return f"Vector x = {self.x1,self.x2}, Vector y = {self.y1,self.y2}"

    # This function print all  functions  of this class
    def all(self):
        return f"{self.info()},\n{self.addition()},\n{self.subtraction()},\n{self.vectors_length()},\n{self.collinear_vectors()},\n{self.dot_product_of_vectors()}"




Test = Vector(1,2,2,4)

print(Test.addition())
print(Test.subtraction())
print(Test.vectors_length())
print(Test.collinear_vectors())
print(Test.dot_product_of_vectors())
print(Test.info())

Test_1 = Vector(23,45,43,2)

print(Test_1.addition())
print(Test_1.subtraction())
print(Test_1.vectors_length())
print(Test_1.collinear_vectors())
print(Test_1.dot_product_of_vectors())
print(Test_1.info())

Test_2 = Vector(90,12,1,71)

print(Test_2.addition())
print(Test_2.subtraction())
print(Test_2.vectors_length())
print(Test_2.collinear_vectors())
print(Test_2.dot_product_of_vectors())
print(Test_2.info())

Test_3 = Vector(22,56,32,45)

print(Test_3.addition())
print(Test_3.subtraction())
print(Test_3.vectors_length())
print(Test_3.collinear_vectors())
print(Test_3.dot_product_of_vectors())
print(Test_3.info())

Test_4 = Vector(11,99,901,134)

print(Test_4.addition())
print(Test_4.subtraction())
print(Test_4.vectors_length())
print(Test_4.collinear_vectors())
print(Test_4.dot_product_of_vectors())
print(Test_4.info())

class Triangle:
    def __init__(self,a:int,b:int,c:int):
        self.a = a
        self.b = b
        self.c = c

    # This function take the length of sides the triangle and return it
    def input_the_length_sides(self):
        a = int(input("Input the a:"))
        c = int(input("Input the b:"))
        b = int(input("Input the c:"))
        return Triangle(a, b, c)

    # This function take the angle of the sides and return it
    def input_the_angle_of_sides(self):
        a = int(input("Input the a:"))
        b = int(input("Input the b:"))
        c = int(input("Input the c:"))
        return Triangle(a, b, c)

    # This function return the type of triangle
    def type_of_triangle(self) ->str:
        if all(self.a, self.b, self.c) < 90:
            return "This triangle is acute"
        elif any([self.a, self.b, self.c]) > 90:
            return "This triangle is obtuse"
        elif any([self.a, self.b, self.c]) == 90:
            return "This triangle is right"

    # This function return the perimeter of triangle
    def perimeter_of_triangle(self) ->str:
        perimeter = self.a + self.b + self.c
        return f"The perimetr of a triangle = {perimeter}"

    # This function return the area of triangle
    def area_of_triangle(self) ->str:
        p = (self.a + self.b + self.c) / 2 # half perimeter
        area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return f"The area of a triangle = {area}"

    # This function return the info of triangle
    def info(self) ->str:
        return f"The side a = {self.a},\nThe side b = {self.b},\nThe side c = {self.c},"

Triangle_0 = Triangle(1,91,3)
print(Triangle_0.input_the_length_sides().info())
print(Triangle_0.perimeter_of_triangle())
print(Triangle_0.area_of_triangle())


from math import pi
class Circle:
    def __init__(self, radius:int):
        self.radius = radius

    # This function return a diameter the circle
    def diameter(self) -> str:
        return f"Diameter a circle = {2 * self.radius}"

    # This function return a circle length
    def circle_length(self) -> str:
        return f"The circle length = {2 * pi * self.radius }"

    # This function return a area of circle
    def area_circle(self) -> str:
        return f"The circle area = {pi * (self.radius ** 2)}"

    # This function take the radius of circle and return it
    def input_radius(self):
        radius = int(input("Input the radius:"))
        return Circle(radius)
    # This function take a name of circle and return it
    def name_circle(self) -> str:
        name = input("Input the name of circle")
        return f"This circle has name : {name} "

Circle_0 = Circle(23)
print(Circle_0.input_radius().circle_length())
print(Circle_0.diameter())
print(Circle_0.input_radius().area_circle())


class Shop:
    def __init__(self,products:list,price:dict,):
        self.products = products
        self.price = price

    # This function take a list of products for purchase  and  return which  products which products are not in the store
    def products_purchase_list(self):
        products_buy = list(input("Input the products which you want to buy"))

    # This function return the price of products
    def price_of_products(self):
        return f"Products:{self.price.keys()},Price:{self.price.values()}"

    # This function take a name of shop and return it
    def name_shop(self):
        name = input("Input the name of shop")
        return f"This shop named {name}"

    def price_products(self,products_buy):
        price = 0
        for i in products_buy:
            price += i.values()
            return price


"""
class ValidateVector:

    @classmethod
    def validate_vector(cls, vector) -> bool:
        # cls - это ссылка на сам класс (ValidateVector)
        # Если у нас метод не взаимодействует с экземпляром класса, то мы можем сделать его staticmethod/classmethod
        if isinstance(vector, Vector):
            return True
        return False

    @staticmethod  # метод не принимает self/cls
    def validate_sides(x1, x2, y1, y2):
        # этот метод ожидает на вход self --> ссылку на экземпляр класса
        # Простая функция, которая не взаимодействует не с классом не с экземпляром класса!
        if isinstance(x1, int) and isinstance(x2, int) and isinstance(y1, int) and isinstance(y2, int):
            return True
        raise TypeError("Все аргументы должны быть целыми числами")


class Vector:
    # class attributes
    vector_list = []
    count = 0

    def __init__(self, x1: int, x2: int, y1: int, y2: int):
        # атрибуты обьекта!
        if ValidateVector.validate_sides(x1, x2, y1, y2):
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
            Vector.update_class_attributes(self)

    @classmethod
    def update_class_attributes(cls, vector):
        if ValidateVector.validate_vector(vector):
            cls.vector_list.append(vector)
            cls.count += 1

    def addition(self) -> str:
        addition = self.x1 + self.y1, self.x2 + self.y2
        return f"Addition of the vectors: {addition}"

    # This function subtract two vectors
    def subtraction(self) -> tuple:
        subtraction = self.x1 - self.y1, self.x2 - self.y2
        print(f"Subtraction of the vectors: {subtraction}")
        return subtraction

    # This function find the length of two vectors
    def vectors_length(self) -> tuple:
        x_length = (self.x1 ** 2 + self.x2 ** 2) ** 0.5
        y_length = (self.y1 ** 2 + self.y2 ** 2) ** 0.5
        print(f"Length of vector x: {x_length}")
        print(f"Length of vector y: {y_length}")

        return x_length, y_length

        # This function define  are vectors collinear

    def collinear_vectors(self) -> bool:
        if self.x1 / self.y1 == self.x2 / self.y2:
            return True
        return False

    # This function find dot_product_of_vectors
    def dot_product_of_vectors(self) -> int:
        dot_product_vectors = self.x1 * self.y1 + self.x2 * self.y2
        print(f"Dot product of vectors: {dot_product_vectors}")
        return dot_product_vectors

    # This function print info of two vectors
    def info(self):
        print(f"Vector x = {self.x1, self.x2}, Vector y = {self.y1, self.y2}")

    # This function print all  functions  of this class
    def all(self):
        return f"{self.info()},\n{self.addition()},\n{self.subtraction()},\n{self.vectors_length()},\n{self.collinear_vectors()},\n{self.dot_product_of_vectors()}"


x = Vector(1, 2, 3, 4)
print(x.vector_list)

x = Vector(2, 4, 5, 1)
print(x.vector_list)