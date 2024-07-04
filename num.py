"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def game_core_v1(number):
    """Просто угадываем на random ни как не используя информацию о больше или меньше,
    Функция принимает загаданное число и возвращает число попыток
     """
     
    count = 0
     
    while True:
         count += 1
         predict = np.random.randint(1, 500)
         if number == predict:
             break
    return(count)


def score_game(game_core_v1):
     """ Запускаем игру 1000 раз, чтобы узнать 
     как бстро игра угадывает число
     """
     
     count_ls = [] # список для сохранения количества попыток
     np.random.seed(1) # фиксируем сид для воспроизводимости
     random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
     
     for number in random_array:
         count_ls.append(game_core_v1(number))
         
     score = int(np.mean(count_ls)) # находим среднее количество попыток
     print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
     return(score)
 
score_game(game_core_v1)
      
     
     
             
    