from random import randint
from SlovGame import *
from time import sleep
from FunkGame import *

name = input("Введи своё имя, путник:")
player['name'] = name
current_vrag = 0

while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка
3 - Информация об игроке
4 - Закончить игру            
''')
    if action == "1":
        fight(current_vrag)
        current_vrag = 1
        if current_vrag == 3:
            break
        
    elif action == "2":
        training_player = input('''Начать тренировку 
1-да
2-нет
''')
        training(training_player)
    elif action == "3":
        display_player()
    elif action == "4":
        end = input("Если хотите закончить игру напишите stop, если продолжить 1:")
        if end == "stop":
            break
        else:
            print()

