import argparse

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

def main():
    parser = argparse.ArgumentParser(description='Фабрика животных')

    parser.add_argument('action', choices=['create', 'attributes'], help='Действие: создание или задание аттрибутов')
    parser.add_argument('--type', help='Вид животного (cat/dog)')
    parser.add_argument('--name', help='Кличка')
    parser.add_argument('--attribute_name', help='Название аттрибута')
    parser.add_argument('--attribute_value', help='Значение аттрибута')

    args = parser.parse_args()

    if args.action == 'create':
        animal_type = args.type
        name = args.name
        animal = AnimalFactory.create_animal(animal_type, name)
        print(f"Created {animal.name} ({animal_type})")

    elif args.action == 'attributes':
        animal_type = args.type
        name = args.name
        attribute_name = args.attribute_name
        attribute_value = args.attribute_value

        animal = AnimalFactory.create_animal(animal_type, name)
        animal.add_attribute(attribute_name, attribute_value)
        print(f"{animal.name} ({animal_type}) has attribute '{attribute_name}' with value '{attribute_value}'")

if __name__ == '__main__':
    main()
