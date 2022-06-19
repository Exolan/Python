import pygame

HEIGHT = 450
WIDTH = 400
FPS = 60
SPEED = 0.4  # Скорость игрока по x
SLOW = -0.12  # Скорость замедления игрока
ACOUNT = 0  # Счетчик анимаций
vol = 0.4  # Изначальная громкость музыки

clock = pygame.time.Clock()  # Счет времени с запуска программы
vector = pygame.math.Vector2  # Вектор для удобной работы со скоростями(2 потому что x и y, есть еще 3, там + z)
platforms = pygame.sprite.Group()  # Массив спрайтов платформ
coins = pygame.sprite.Group()  # Массив спрайтов монет

# Массивы и переменные со спрайтами
playerIdle = [pygame.image.load('Resurce/Characters/Frog/IDLE/0.png'),
              pygame.image.load('Resurce/Characters/Frog/IDLE/1.png'),
              pygame.image.load('Resurce/Characters/Frog/IDLE/2.png'),
              pygame.image.load('Resurce/Characters/Frog/IDLE/3.png'),
              pygame.image.load('Resurce/Characters/Frog/IDLE/4.png'),
              pygame.image.load('Resurce/Characters/Frog/IDLE/5.png'),
              pygame.image.load('Resurce/Characters/Frog/IDLE/6.png'),
              pygame.image.load('Resurce/Characters/Frog/IDLE/7.png'),
              pygame.image.load('Resurce/Characters/Frog/IDLE/8.png'),
              pygame.image.load('Resurce/Characters/Frog/IDLE/9.png')]
playerMove = [pygame.image.load('Resurce/Characters/Frog/MOVE/0.png'),
              pygame.image.load('Resurce/Characters/Frog/MOVE/1.png'),
              pygame.image.load('Resurce/Characters/Frog/MOVE/2.png'),
              pygame.image.load('Resurce/Characters/Frog/MOVE/3.png'),
              pygame.image.load('Resurce/Characters/Frog/MOVE/4.png'),
              pygame.image.load('Resurce/Characters/Frog/MOVE/5.png'),
              pygame.image.load('Resurce/Characters/Frog/MOVE/6.png'),
              pygame.image.load('Resurce/Characters/Frog/MOVE/7.png'),
              pygame.image.load('Resurce/Characters/Frog/MOVE/8.png'),
              pygame.image.load('Resurce/Characters/Frog/MOVE/9.png'),
              pygame.image.load('Resurce/Characters/Frog/MOVE/10.png'),
              pygame.image.load('Resurce/Characters/Frog/MOVE/11.png')]
playerJump = pygame.image.load('Resurce/Characters/Frog/JUMP/Jump.png')
playerFall = pygame.image.load('Resurce/Characters/Frog/FALL/Fall.png')

coinAnim = [pygame.image.load('Resurce/Moneda/0.png'),
            pygame.image.load('Resurce/Moneda/1.png'),
            pygame.image.load('Resurce/Moneda/2.png'),
            pygame.image.load('Resurce/Moneda/3.png'),
            pygame.image.load('Resurce/Moneda/4.png')]
