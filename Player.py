from pygame.locals import *
from constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # Вызов конструктора родительского класса (Sprite).
        # Конструктор - метод, который автоматически вызывается при создании объекто
        self.im = pygame.image.load('Resurce/Characters/Frog/IDLE/0.png')
        self.rect = self.im.get_rect()

        self.pos = vector((30, 440))  # Изначальная позиция
        self.speed = vector(0, 0)  # Скорость по x = 0, т.к. не двигаемся изначально
        self.vel = vector(0, 0)  # Так же по y

        self.idle = False  # Игрок стоит
        self.moveR = False  # Игрок двигается вправо
        self.moveL = False  # Игрок двигается влево
        self.sideL = False  # Игрок смотрит влево
        self.fall = False  # Игрок падает
        self.jumpP = False  # Игрок прыгает

        self.score = 0  # Счет

    def move(self):  # Метод, отвечающий за передвижение
        self.speed = vector(0, 0.5)  # Делаем скорость вниз, чтобы герой имел, грубо говоря, силу тяжести

        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.speed.x = -SPEED
            self.moveL = True
            self.moveR = False
            self.idle = False
            self.sideL = True
            self.fall = False
            self.jumpP = False
        elif keys[K_RIGHT]:
            self.speed.x = SPEED
            self.moveR = True
            self.moveL = False
            self.idle = False
            self.sideL = False
            self.fall = False
            self.jumpP = False
        else:
            self.speed.x = 0
            self.moveR = False
            self.moveL = False
            self.idle = True
            self.fall = False
            self.jumpP = False

        if self.vel.y > 0:
            self.moveR = False
            self.moveL = False
            self.idle = False
            self.fall = True
            self.jumpP = False

        self.speed.x += self.vel.x * SLOW  # Замедляем персонажа после нажатия клавиши
        self.vel += self.speed  # Сохраняем положение по y, позволяя изменять x
        self.pos += self.vel + 0.5 * self.speed  # Замедляем игрока в верхней точке прыжка и ускоряем его при падении

        if self.pos.x > WIDTH:  # Возможность выходить за правую сторону экрана и оказаться в левой
            self.pos.x = 0  # И наоборот
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos  # Присваиваем позицию спрайту на экране

    def jump(self):  # Прыжок игрока
        hits = pygame.sprite.spritecollide(self, platforms, False)  # Возвращаем список, содержащий все спрайты,
        if hits and not self.jumpP:  # которые пересекаются с игроком
            self.vel.y = -17  # Если игрок касается платформы, то только
            self.jumpP = True  # тогда можно прыгнуть
            self.moveR = False
            self.moveL = False  # vel.y - скорость прыжка
            self.idle = False
            self.fall = False

    def update(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)  # Не дает игроку упасть, если он касается
        if self.vel.y > 0:  # Только при падении игрок приземляется
            if hits:    # Игрок призмляется на платформу только тогда
                if self.pos.y < hits[0].rect.bottom - 5:  # Когда низ модельки касается верха платформы
                    if hits[0].point == True:
                        hits[0].point = False
                        self.score += 1  # Засчитывем очко за платформу
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0
