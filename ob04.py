from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        action = self.weapon.attack()
        return f"Боец {action}."

class Monster:
    def __init__(self, health):
        self.health = health

    def is_defeated(self):
        return self.health <= 0

def battle(fighter, monster):
    print("Бой начинается!")
    while not monster.is_defeated():
        print(fighter.fight())
        monster.health -= 20
        if monster.is_defeated():
            print("Монстр побежден!")

fighter = Fighter(Sword())
monster = Monster(100)
battle(fighter, monster)

fighter.change_weapon(Bow())
monster = Monster(100)
battle(fighter, monster)
