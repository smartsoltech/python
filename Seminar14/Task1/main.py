import doctest
import unittest
import argparse

# Your Animal Factory code here

class Animal:
    def __init__(self, name):
        self.name = name
        self.attributes = {}

    def add_attribute(self, attribute_name, attribute_value):
        self.attributes[attribute_name] = attribute_value

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

class Dog(Animal):
    def make_sound(self):
        return "Гав!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == 'cat':
            return Cat(name)
        elif animal_type == 'dog':
            return Dog(name)
        else:
            raise ValueError("Неизвестный вид животного")

# Command-line argument parsing with subcommands
parser = argparse.ArgumentParser(description='Run tests for Animal Factory')
subparsers = parser.add_subparsers(dest='test_type', help='Type of test to run')

# Doctest subcommand
subparsers.add_parser('doctest', help='Run doctest')

# Unittest subcommand
subparsers.add_parser('unittest', help='Run unittest')

# Pytest subcommand
subparsers.add_parser('pytest', help='Run pytest')

args = parser.parse_args()

if args.test_type == 'doctest':
    # Doctest
    doctest.testmod()

elif args.test_type == 'unittest':
    # Unittest
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(AnimalFactory))

elif args.test_type == 'pytest':
    # Import pytest only when needed
    import pytest
    pytest.main()

else:
    print('Пожалуйста, укажите тип теста, используя одну из подкоманд: doctest, unittest, pytest')
