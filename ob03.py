class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Реализация абстрактного метода")

    def eat(self):
        print(f"{self.name} поглащает корм")


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} щебечит")


class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} ревет.")


class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} пищит")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Employee:
    def __init__(self, name):
        self.name = name


class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} разместил в зоопарке {animal.name}.")


class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} вылечил {animal.name}.")


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f":Новое животное {animal.name} размещено в зоопарке.")

    def add_staff(self, employee):
        self.staff.append(employee)
        print(f"Новый работник {employee.name} трудоустроен в зоопарке")

    def show_all_animals(self):
        for animal in self.animals:
            print(f"Животное: {animal.name}, Возраст: {animal.age}")

    def show_all_staff(self):
        for employee in self.staff:
            print(f"Работник: {employee.name}")


if __name__ == "__main__":
    zoo = Zoo()

    bird = Bird("Вуди", 3)
    mammal = Mammal("Стив", 5)
    reptile = Reptile("Дино", 4)

    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)

    zookeeper = ZooKeeper("Вася")
    veterinarian = Veterinarian("Влад")

    zoo.add_staff(zookeeper)
    zoo.add_staff(veterinarian)

    zoo.show_all_animals()
    zoo.show_all_staff()

    animal_sound(zoo.animals)
    zookeeper.feed_animal(mammal)
    veterinarian.heal_animal(bird)