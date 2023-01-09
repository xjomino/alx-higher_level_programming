#!/usr/bin/python3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        p = Person("John", 30)
        attributes_and_methods = lookup(p)
        print(attributes_and_methods)

