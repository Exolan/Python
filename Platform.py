from constants import *
import random
from Coin import Coin


class Platform(pygame.sprite.Sprite):  # pygame.sprite.Sprite - Простой базовый класс для видимых игровых объектов.
    def __init__(self):
        super().__init__()  # Вызов конструктора родительского класса (Sprite).
        # Конструктор - метод, который автоматически вызывается при создании объекто
        self.im = pygame.image.load('Resurce/platform.png')
        self.rect = self.im.get_rect(center=(random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 30)))
        self.point = True  # Означает, что за эту платформу можно получить очко

        self.coinChance = 0  # Переменная для рандомной отрисовки монет

    def generate_coin(self):  # Генерация монеты
        self.coinChance = random.randint(1, 100)
        if 0 < self.coinChance < 11:
            coins.add(Coin((self.rect.centerx, self.rect.centery - 50)))
