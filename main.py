from game import game, lose  # Из модуля game импортируем функцию game()
from constants import *  # Из модуля constants импортируем ВСЕ
from pygame.locals import *  # Импорт всех констант PyGame
import sys  # Импорт sys для взаимодействия с интерпретатором
from Player import Player  # Из модуля Player импортируем класс Player
from Platform import Platform  # Из модуля Platform импортируем класс Platform
import random
import os
import pickle

pygame.init()  # Активация всех импортируемых модулей


def game_loop():
    global end
    global score
    player = Player()  # Создаем персонажа
    main_platform = Platform()  # Создаем главную платформу и распологаем ее без возможности получить очко
    main_platform.rect = main_platform.im.get_rect(center=(10, 440))
    main_platform.point = False

    platforms.add(main_platform)

    for x in range(random.randint(5, 7)):  # Генерируем первые платформы в окне
        pl = Platform()
        pl.generate_coin()
        platforms.add(pl)

    game(ACOUNT, win, background, vol, m_pause, player, end)
    lose(win, font, background, vol, m_pause, player, end, score)


def main_menu():  # Функция главного меню
    global score
    if os.path.getsize('score.pkl') > 0:        # Получение счета
        with open('score.pkl', 'rb') as file:
            score = int(pickle.load(file))

    text1 = font.render('Нажмите SPACE...', True, (0, 0, 0))  # Создаем текст, второй параметр - сглаживание
    text2 = font.render('Ваш рекорд: ' + str(score), True, (0, 0, 0))

    win.blit(background, (0, 0))  # Заполняем окно фоном
    win.blit(text1, (70, HEIGHT / 2))  # Распологаем текст
    win.blit(text2, (75, HEIGHT / 4))

    pygame.display.flip()  # Обновляем содержимое всего окна


win = pygame.display.set_mode((WIDTH, HEIGHT))  # Создаем окно
pygame.display.set_caption("Game")  # Называем его Game
background = pygame.image.load('./Resurce/background.png')  # Загружаем фон
font = pygame.font.SysFont('Verdana', 30)  # Загружаем шрифт

pygame.mixer.music.load('./Resurce/music/fonmusic.mp3')  # Загрузка фоновой музыки

pygame.mixer.music.play(-1)  # Бесконечное повторение(-1)
pygame.mixer.music.set_volume(vol)

m_pause = False  # Переменная для отслежки паузы
end = False

score = 0

while True:  # Бесконечный цикл, пока не нажмем на крестик - из программы не выйдем
    for e in pygame.event.get():  # Отлавливаем события
        if e.type == QUIT:  # Если событие - выход из программы, то выходим
            pygame.quit()
            sys.exit()  # Выход из Python
        if e.type == KEYDOWN:
            if e.key == K_EQUALS:  # Если нажимаем +, то громкость >
                vol += 0.1
                if vol > 1.0:
                    vol = 1.0
                pygame.mixer.music.set_volume(vol)
            elif e.key == K_MINUS:  # Если -, то громкость <
                vol -= 0.1
                if vol < 0:
                    vol = 0
                pygame.mixer.music.set_volume(vol)
            elif e.key == K_s:  # Если s, то или стоп, или плей
                m_pause = not m_pause
                if m_pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif e.key == K_SPACE:
                game_loop()
            elif e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    main_menu()  # Запуск функции главного меню
