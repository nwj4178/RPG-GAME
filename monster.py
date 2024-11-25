from abc import ABC, abstractmethod
import random
from character import Equipment  # Equipment 클래스 임포트


class Monster(ABC):  # 추상 클래스
    def __init__(self, name, hp, attack, defense, speed, level):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.level = level

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def is_alive(self):
        return self.hp > 0

    def level_up(self):
        self.level += 1
        self.hp += 10
        self.attack += 2
        self.defense += 1
        self.speed += 1

    def exp_reward(self):
        return self.level * 20

    @abstractmethod
    def special_attack(self):
        pass

    @abstractmethod
    def description(self):
        pass

    def drop_loot(self):
        if random.random() <= 0.5:
            is_weapon = random.random() <= 0.5
            grade_roll = random.random()
            if grade_roll <= 0.5:
                grade = "일반"
                bonus = random.randint(1, 5)
            elif grade_roll <= 0.8:
                grade = "레어"
                bonus = random.randint(5, 10)
            else:
                grade = "전설"
                bonus = random.randint(10, 15)

            if is_weapon:
                return Equipment(f"{grade} 무기", grade, attack_bonus=bonus)
            else:
                return Equipment(f"{grade} 갑옷", grade, defense_bonus=bonus)
        return None


class Goblin(Monster):
    def special_attack(self):
        return self.attack * 1.5

    def description(self):
        return "약한 몬스터지만, 때때로 치명적인 공격을 합니다."


class Orc(Monster):
    def special_attack(self):
        return self.attack * 2

    def description(self):
        return "강력한 체력과 파괴력을 가진 몬스터입니다."


class Dragon(Monster):
    def special_attack(self):
        return self.attack * 3

    def description(self):
        return "엄청난 위력과 화염 공격을 가진 몬스터의 왕입니다."
