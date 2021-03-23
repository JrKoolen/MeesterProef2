import pygame
from PIL import Image, ImageDraw
import config
from game_state import GameState
from game import Game

pygame.init()

win = pygame.display.set_mode((config.SCREEN_WIDHT, config.SCREEN_HEIGHT))

win.fill(config.BLACK)

pygame.display.flip()

pygame.display.set_caption("Proxy")

# walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
#             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
#             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
# walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
#           pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
#            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

player = Image.new('RGB', (config.SCALE, config.SCALE), color='red')
player.save('player.png')

grassImage = Image.new('RGB', (config.SCALE, config.SCALE), color='green')
grassImage.save('Grass.png')

QuizImage = Image.new('RGB', (config.SCALE, config.SCALE), color='red')
QuizImage.save('Quiz.png')

wallImage = Image.new('RGB', (config.SCALE, config.SCALE), color='black')
wallImage.save('wall.png')

floorImage = Image.new('RGB', (config.SCALE, config.SCALE), color='brown')
floorImage.save('floor.png')

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDHT, config.SCREEN_HEIGHT))


def draw_grid():
    tile_size = config.SCALE
    for line in range(0, 40):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (config.SCREEN_WIDHT, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, config.SCREEN_HEIGHT))


clock = pygame.time.Clock()

game = Game(screen)
game.set_up()
while game.game_state == GameState.RUNNING:
    clock.tick(50)
    game.update()
    draw_grid()
    pygame.display.flip()
