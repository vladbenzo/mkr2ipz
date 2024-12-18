from abc import ABC, abstractmethod
from typing import List

# Фабричний метод

# Абстрактний клас Персонажа
class Character(ABC):
    def __init__(self, health: int, attack_power: int):
        self.health = health
        self.attack_power = attack_power
        self.position = (0, 0)

    @abstractmethod
    def get_type(self):
        pass

    def move(self, x, y):
        self.position = (x, y)

    def attack(self):
        print(f"{self.get_type()} атакує з потужністю {self.attack_power}")

class Warrior(Character):
    def get_type(self):
        return "Воїн"

class Mage(Character):
    def get_type(self):
        return "Маг"

class Archer(Character):
    def get_type(self):
        return "Лучник"

# Фабрика для створення персонажів
class CharacterFactory:
    @staticmethod
    def create_character(character_type: str):
        if character_type == "Воїн":
            return Warrior(health=150, attack_power=20)
        elif character_type == "Маг":
            return Mage(health=100, attack_power=40)
        elif character_type == "Лучник":
            return Archer(health=120, attack_power=30)
        else:
            raise ValueError("Невідомий тип персонажа")


# Медіатор

# Центральний об'єкт "Арена" для координації дій персонажів
class Arena:
    def __init__(self):
        self.characters: List[Character] = []

    def add_character(self, character: Character):
        self.characters.append(character)
        print(f"{character.get_type()} доданий на арену.")

    def notify_action(self, actor: Character, action: str):
        print(f"[Арена]: {actor.get_type()} : {action}.")


# Спостерігач для відстеження змін у персонажах
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class ArenaObserver(Observer):
    def update(self, message: str):
        print(f"[Сповіщення]: {message}")

# ===== Гра =====

# Основний клас гри
class Game:
    def __init__(self):
        self.arena = Arena()
        self.observer = ArenaObserver()

    def add_character_to_arena(self, character_type: str):
        character = CharacterFactory.create_character(character_type)
        self.arena.add_character(character)
        self.observer.update(f"{character.get_type()} з'явився на арені!")
        return character

    def character_action(self, character: Character, action: str):
        self.arena.notify_action(character, action)
        self.observer.update(f"{character.get_type()} : {action}.")


# ===== Запуск гри
if __name__ == "__main__":
    game = Game()

    # Створення персонажів через фабричний метод
    warrior = game.add_character_to_arena("Воїн")
    mage = game.add_character_to_arena("Маг")

    # Виконання дій через Медіатора
    game.character_action(warrior, "атакує")
    game.character_action(mage, "відправляється на позицію (5, 5)")

    # Сповіщення про зміни
    game.observer.update("Бій на арені не зупиняється!")
