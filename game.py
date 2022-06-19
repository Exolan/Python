from pygame.locals import *
import random
import sys
from constants import *
from Platform import Platform  # Из модуля Platform импортируем класс Platform
import pickle


def plat_gen():  # Функция, отвечающая за генеацию платформ
    while len(platforms) < 8:  # Пока длина массива платформ < 8
        p = Platform()  # Создаем платформу
        p.rect.center = (random.randrange(0, WIDTH), random.randrange(-50, 0))  # Даем ей рандоиное положение
        check(p)  # Проверяем на наложение с другими платформами
        p.generate_coin()  # Запускаем функцию рандомной генерации монеты
        platforms.add(p)  # Добавляем платформу в массив платформ


def check(platform):  # Функция проверки наложения платформ
    for pl in platforms:  # Перебираем массив платформ
        if pl.rect.colliderect(platform):  # Если находим наложение, то удаляем старую платформу
            pl.kill()


def coin_update(player):  # Проверка монет
    for c in coins:  # Перебираем массив монет
        if player.rect.colliderect(c):  # Если игрок касается монеты, то монету удаляем, а счет увеличиваем
            c.kill()
            player.score += 5


def lose(win, font, background, vol, m_pause, player, end, score):  # Функция проигрыша
    player_answer = False  # Переменная для проверки нажатия клавиши пользователем
    for item in platforms:  # Удаляем все с окна, кроме фона
        item.kill()
    with open("score.pkl", 'wb') as file:  # Открываем файл для изменения
        if player.score > score:  # Проверка на score
            pickle.dump(player.score, file)  # Изменяем в файле score на новый
        else:
            pickle.dump(score, file)  # Оставляем старый
    while not player_answer:
        win.blit(background, (0, 0))
        go = font.render("Ваш счёт: " + str(player.score), True, (0, 0, 0))  # Выводим надпись Счета
        win.blit(go, (90, HEIGHT / 3))
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == KEYDOWN:
                if e.key == K_r:
                    end = True
                    player_answer = True
                elif e.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif e.key == K_EQUALS:  # Если нажимаем +, то громкость >
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
        pygame.display.update()


def game(ACOUNT, win, background, vol, m_pause, player, end):  # Функция самой игры
    while not end:  # Основной цикл, чтобы окно само не закрывалось
        player.update()  # Вызов функции класса Player, отслеживающая касания с плитами
        for e in pygame.event.get():  # Перебираем все события
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            if e.type == KEYDOWN:  # Если было совершено нажатие на клавишу
                if e.key == K_UP:  # Если K_UP, то игрок прыгает(вызов функции jump)
                    player.jump()
                elif e.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif e.key == K_EQUALS:
                    vol += 0.1
                    pygame.mixer.music.set_volume(vol)
                elif e.key == K_MINUS:
                    vol -= 0.1
                    pygame.mixer.music.set_volume(vol)
                elif e.key == K_s:
                    m_pause = not m_pause
                    if m_pause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        win.blit(background, (0, 0))  # Очистка окна от всего, кроме фона, чтобы не стакались спрайты
        font = pygame.font.SysFont('Verdana', 35)
        text1 = font.render('Счет: ', True, (0, 0, 0))  # Создаем Счет
        text2 = font.render(str(player.score), True, (0, 0, 0))

        for item in platforms:  # Перебираем все платформы и распологаем их в окне
            win.blit(item.im, item.rect)

        # Делаем бесконечный уровень
        if player.rect.top <= HEIGHT / 3:  # Если игрок перемещается вверх
            player.pos.y += abs(player.vel.y)  # Изменяем позицию игрока в окне
            for plat in platforms:  # Так же изменяем позиции платформ и монет относительно игрока
                plat.rect.y += abs(player.vel.y)  # И удаляем те, которые скрылись
                if plat.rect.top >= HEIGHT:  # ABS, чтобы получить целое положительное число (абсолютное)
                    plat.kill()
            for coin in coins:
                coin.rect.y += abs(player.vel.y)
                if coin.rect.top >= HEIGHT:
                    coin.kill()

        if ACOUNT >= FPS:  # Если счетчик анимаций вышел за предел FPS, то обнуляем
            ACOUNT = 0

        # Отрисовка всех спрайтов
        if player.idle:  # Если игрок стоит
            if player.sideL:  # Если игрок смотрит влево, то спрайты влево, иначе вправо
                win.blit(pygame.transform.flip(playerIdle[ACOUNT // 6], True, False), player.rect)
            else:
                win.blit(playerIdle[ACOUNT // 6], player.rect)
        if player.moveL:  # Если игрок перемещается влево
            win.blit(pygame.transform.flip(playerMove[ACOUNT // 5], True, False), player.rect)
        if player.moveR:  # Если вправо
            win.blit(playerMove[ACOUNT // 5], player.rect)
        if player.jumpP:  # Если прыгает
            if player.sideL:  # Если смотри влево
                win.blit(pygame.transform.flip(playerJump, True, False), player.rect)
            else:  # Если вправо
                win.blit(playerJump, player.rect)
        if player.fall:  # Падение игрока
            if player.sideL:
                win.blit(pygame.transform.flip(playerFall, True, False), player.rect)
            else:
                win.blit(playerFall, player.rect)

        player.move()  # Выполняем функцию движений игрока
        plat_gen()  # Выполняем функцию генерации платформ
        coin_update(player)  # Выполняем функцию проверки монет

        win.blit(text1, (WIDTH / 3 + 10, 10))  # Распологаем Счет в окне
        win.blit(text2, (WIDTH / 2 + 40, 10))

        for coin in coins:  # Отрисовка анимации для монет
            win.blit(coinAnim[ACOUNT // 12], coin.rect)
            coin.update()

        if player.rect.top > HEIGHT:  # Если игрок падает вниз за экран, то запускается lose
            end = True

        ACOUNT += 1  # Каждый раз увеличиваем счетчик анимации вместе с fps

        pygame.display.update()  # Обновляем все изменения на окне
        clock.tick(FPS)  # Указывем на то, что цикл должен работать в 60 кадров в секунду
