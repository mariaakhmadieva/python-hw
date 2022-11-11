# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# Добавьте игру против бота

from random import randint

player1 = input("Имя первого игрока: ")
player2 = input("Придумай Мне имя 😊: ")
value = int(input("Количество конфет на столе: "))

def take_input(name):
    while True:
        x = int(input(f'\n{name}, cколько возьмёшь кофет? Не более 28 шт: '))
        if 1 > x or x > 28:
            print('Ты вводишь некорректные данные, попробуй заново)')
            continue
        return x

def res_print(name, k, counter, value):
    print(f"{name} взял(а) {k} конфет, теперь у него(неё) {counter}. На столе осталось {value} конфет.")

lottery = randint(0, 2)
if lottery:
    print(f"\nПервым ходит игрок {player1}.")
else:
    print(f"\nПервым ходит игрок - {player2}.")

count_p1 = 0
count_p2 = 0

while value > 28:
    if lottery:
        k = take_input(player1)
        value -= k
        count_p1 += k
        lottery = False
        res_print(player1, k, count_p1, value)
    else:
        k = randint(0, 29)
        print(f'\nЯ, пожалуй, возьму {k} конфет.')
        value -= k
        count_p2 += k
        lottery = True
        res_print(player2, k, count_p2, value)

if lottery:
    print(f"\nТы победитель!😉")
else:
    print(f"\nЯ победитель!😍")