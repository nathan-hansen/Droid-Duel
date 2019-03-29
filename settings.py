# screen size and fps
windowWidth = 1080
windowHeight = 720
FPS = 60
fontName = 'Comic Sans'

# title
gameTitle = "DROID DUEL"

# player properties
PlayerAcc = 1.25
PlayerFriction = -0.20
PlayerGravity = 0.8
PLAYER_JUMP = 15

# starting platforms

PlatformList = [(0, windowHeight - 40, windowWidth, 40),
                (windowWidth / 2 - 100, windowHeight - 150, 200, 14),
                (0, windowHeight - 150, 200, 14),
                (windowWidth - 200, windowHeight - 150, 200, 14),
                ((windowWidth * 3/4) - 150, windowHeight - 250, 200, 14),
                ((windowWidth * 1/4) - 50, windowHeight - 250, 200, 14),
                ]

# define colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SKYBLUE = (135, 206, 250)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)