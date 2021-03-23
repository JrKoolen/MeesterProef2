import pygame
from pygame.locals import *
import config
import math
from player import Player
from game_state import GameState


def get_random_question():
    question = ''

    return question


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []
        self.camera = [0, 0]

    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        self.game_state = GameState.RUNNING

        self.load_map("map01")

    def draw_text(self, text_col, x, y, ):
        text_font = pygame.font.SysFont('Bauhaus 93', 30)
        question = get_random_question()
        img = text_font.render(question, True, text_col)
        self.screen.blit(img, (x, y))

    def update(self):
        self.screen.fill(config.BLACK)
        self.handle_events()
        bg = pygame.image.load("bg2.png")
        self.screen.blit(bg, (0, 0))

        self.render_map(self.screen)
        self.draw_text(text_col=config.WHITE, x=10, y=10)

        for object in self.objects:
            object.render(self.screen, self.camera)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_w:  # up
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_s:  # down
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_a:  # up
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_d:  # up
                    self.move_unit(self.player, [1, 0])

    def load_map(self, file_name):
        with open(file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)
            print(self.map)

    def render_map(self, screen):
        self.determine_camera()

        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE - (self.camera[1] * config.SCALE),
                                   config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map) - 1):
            return

        if self.map[new_position[1]][new_position[0]] == "W":
            return

        if self.map[new_position[1]][new_position[0]] == "Q":
            question = get_random_question()
            self.draw_text(config.WHITE, 10, 10)
            print("QUIZ VRAAG")

        unit.update_position(new_position)

    def determine_camera(self):
        max_y_position = len(self.map) - config.SCREEN_HEIGHT / config.SCALE
        y_position = self.player.position[1] - math.ceil(round(config.SCREEN_HEIGHT / config.SCALE / 2))

        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position


map_tile_image = {
    "G": pygame.transform.scale(pygame.image.load("grass.png"), (config.SCALE, config.SCALE)),
    "W": pygame.transform.scale(pygame.image.load("wall.png"), (config.SCALE, config.SCALE)),
    "F": pygame.transform.scale(pygame.image.load("floor.png"), (config.SCALE, config.SCALE)),
    "Q": pygame.transform.scale(pygame.image.load("floor.png"), (config.SCALE, config.SCALE)),
}
