class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color
    def fly(self):
        print(f'{self.name} летает')

    def eat(self):
        print(f'{self.name} клюёт')

    def sing(self):
        print(f'{self.name} поёт чирик')

    def info(self):
        print(f'{self.name} - имя')
        print(f'{self.voice} - имя')
        print(f'{self.color} - цвет')

class Pigeon(Bird):
    def __init__(self, name, voice, color, food):
        super(). __init__(name, voice, color)
        self.food = food

    def walk(self):
        print(f'{self.name} гуляет')

    def sing(self):
        print(f'{self.name} поёт курлык')


bird1 = Pigeon('Голубь', 'курлык', 'серый', 'хлебные крошки')
bird2 = Bird('Джек', 'чирик', 'грязный')

bird1.sing()
bird1.info()
bird1.walk()

bird2.sing()
bird2.info()
