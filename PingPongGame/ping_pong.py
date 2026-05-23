from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, wight, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update_r(self):
        keys = key.get_pressed()
        # Move right paddle up
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        # Move right paddle down
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        # Move left paddle up
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        # Move left paddle down
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


# Window size
win_width = 700
win_height = 500

# Game window title
display.set_caption("Ping Pong Game")

# Create game window
window = display.set_mode((win_width, win_height))

# Load and resize background image
background = transform.scale(image.load("bg-4.jpg"),(win_width, win_height))

# Game settings
game = True
finish = False

# FPS controller
clock = time.Clock()
FPS = 60

racket1 = Player('racket-2.png', 30, 200, 20, 150, 4) 
racket2 = Player('racket-2.png', 650, 200, 20, 150, 4)
ball = GameSprite('ball-3.png', 200, 200, 50, 50, 4)

font.init()
lose_font = font.Font(None, 35)
lose1 = lose_font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = lose_font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

score_font = font.Font(None, 65)

speed_x = 3
speed_y = 3

score1 = 0
score2 = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background, (0, 0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
    
    