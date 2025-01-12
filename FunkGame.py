from random import randint
from time import sleep
from SlovGame import *

def fight (current_vrag):
    round = randint(1,2)
    vrag = vrags[current_vrag]
    vrag_hp = vrags[current_vrag]["hp"]
    print(f'Противник - {vrag["name"]}:{vrag["script"]}')
    input("Enter чтобы продолжить")
    print()
    while player["hp"] > 0 and vrag_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {vrag["name"]}.')
            crit = randint(1,100)
            if crit < player["luck"]:
                vrag_hp -= player["attack"] * 3
            else:
                vrag_hp = player["attack"]
        else:
            print(f'{vrag["name"]} атакует{player["name"]}.')
            player["hp"] -= vrag["attack"] * player["def"]
            sleep(1)
        print(f'''{player["name"]}:{player["hp"]}, {vrag["name"]}: {vrag_hp}''')
        print()
        sleep(1)
        round += 1

        if player["hp"] > 0:
            print(f'Противник - {vrag["name"]}: {vrag["win"]}')
            current_vrag +=1
        else:
            print(f'Противник - {vrag["name"]}: {vrag["lose"]}')
        player["hp"] = 200
        print()
        return current_vrag
    
def training (training_player):
    skip = input('''Желаете пропустить тренировку? 
1-да
2- нет
''')
    if skip == 2:
        for i in range(0,101,10):
            print(f'Тренировка завершена на {i}%')
            sleep(2)
            player['attack'] += 5
            player['def'] += 1.5
            print(f'Тренировка окончательно завершена! Теперь ваша атака равна {player["attack"]}')
    else:
        print("Приходи в следующий раз потренироватся")

def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Сила аттаки равна {player['attack']}, Шанс критического удара({player["attack"] * 3} ед.) равен {player["luck"]}%')
    print(f'Защита равна {player["def"]}')
    print()




