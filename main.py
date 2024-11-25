from character import Hero
from monster import Goblin, Orc, Dragon
from battle import Battle
import random

def main():
    print("게임 시작")
    name = input("이름 입력: ")
    role = input("직업 입력(전사/마법사/궁수): ")
    hero = Hero(name, 100, 20, 5, speed=12, role=role)
    print(hero)
    battle = Battle()

    monsters = [
        Goblin("고블린", 30, 10, 2, speed=10, level=1),
        Orc("오크", 50, 15, 5, speed=8, level=1),
        Dragon("드래곤", 100, 20, 10, speed=6, level=1)
    ]

    for _ in range(5):  # 5번 전투 진행
        monster = random.choice(monsters)
        battle.fight(hero, monster)
        monster.level_up()

    print(hero)

if __name__ == "__main__":
    main()
