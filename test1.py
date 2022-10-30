# # Public, Protected, Private

# class A:
#     public = "class_public"
#     _protected = "class_protected"
#     __private = "class_private"
#
#     def __init__(self):
#         self.public = "public_instance"
#         self._protected = "protected_instance"  # показатель, что переменная не должна использоваться вне класса
#         self.__private = "private_instance"  # показатель, что переменная не должна использоваться вне класса
#
#         # protected - доступен внутри класса и в наследниках
#
#     def print_instance_vars(self):
#         print(self.public)
#         print(self._protected)
#         print(self.__private)
#
#     # Public (generally methods declared in a class) are accessible from outside the class.
#
#
# print(A.public)
# print(A._protected)
# # print(A.__private)  # AttributeError: type object 'A' has no attribute '__private'
# print(A.__dict__)
# x = A()
# print(x.public)
# print(x._protected)
# # print(x.__private)  # AttributeError: 'A' object has no attribute '__private'
# x.print_instance_vars()


class Person:
    _list_of_persons = []

    def __init__(self, name, age, passport="1234567890"):
        self.name = name
        self.age = age
        self.__passport = passport
        Person._list_of_persons.append(self)

    def myfunc(self):
        print("Hello my name is " + self.name)

    def change_passport(self, new_passport):
        self.__passport = new_passport

    def get_passport(self):
        # тут мы типо проверяем есть ли у пользователя права на получение паспорта
        return self.__passport

    def __str__(self):
        # Строковое представление объекта
        return f"Person {self.name} {self.age} {self.__passport}"


vasya = Person("Vasya", 25)

print(vasya)
print(vasya.get_passport())
