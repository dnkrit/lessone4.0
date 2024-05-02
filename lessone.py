class Warrior():

    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color
    def sleep(self):
        print(f'{self.name} лег спать')
        self.endurance += 9

    def eat(self):
        print(f'{self.name} присел покушать')
        self.power += 3

    def hit(self):
        print(f'{self.name} бъет сильно')
        self.endurance -= 3

    def walk(self):
        print(f'{self.name} бродит')
        self.power -= 1

    def info(self):
        print(f'Имя воина - {self.name}')
        print(f'Цвет волос воина - {self.hair_color}')
        print(f'Сила воина - {self.power}')
        print(f'Выносливость воина - {self.endurance}')

war1 = Warrior('Первый', 130, 89, 'Русый')
war2 = Warrior('Второй', 129, 90, 'Блонд')

print(war1.endurance)
print(war1.power)
war1.sleep()
war1.eat()
war1.hit()
war1.walk()
war1.info()
print(war1.endurance)
print(war1.power)


print(war2.endurance)
print(war2.power)
war2.sleep()
war2.eat()
war2.hit()
war2.walk()
war2.info()
print(war2.endurance)
print(war2.power)







print(war1.name)
print(war1.power)
print(war1.hair_color)












