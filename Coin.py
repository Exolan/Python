import pygame


class Coin(pygame.sprite.Sprite):  # Класс Монет
    def __init__(self, pos): # Вызов конструктора родительского класса (Sprite).
        # Конструктор - метод, который автоматически вызывается при создании объекто
        super().__init__()  # Импорт
        self.im = pygame.image.load('Resurce/Moneda/0.png')  # Загружаем изображение
        self.rect = self.im.get_rect()  # Переделываем изображение в прямоугольник
        self.rect.topleft = pos  # Задаем расположение
