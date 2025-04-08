import pygame
import sys
from pygame.color import THECOLORS
from src.triangle import Triangle


class GameUI:
    def __init__(self, game_logic: Triangle):
        pygame.init()
        pygame.display.set_caption("Sierpinski Triangle Drawing")
        self.window_size = [800, 600]
        self.screen = pygame.display.set_mode(self.window_size)
        self.fps = 30
        self.game_logic = game_logic

        THECOLORS.get("red")

    def start_game(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # BG fill
            self.screen.fill(THECOLORS.get("white"))

            # Triagnle lines
            pygame.draw.polygon(
                self.screen,
                THECOLORS.get("black"),
                [(p.x, p.y) for p in self.game_logic.apexes],
                2,
            )

            # Triagle apexes
            for vertex in self.game_logic.apexes:
                pygame.draw.circle(
                    self.screen,
                    THECOLORS.get("blue"),
                    (int(vertex.x), int(vertex.y)),
                    5,
                )

            # Draw starting point
            pygame.draw.circle(
                self.screen,
                THECOLORS.get("green"),
                (int(self.game_logic.points[0].x), int(self.game_logic.points[0].y)),
                3,
            )

            # Find next point, add to array, print them all
            self.game_logic.add_next_point()
            for point in self.game_logic.points[1:]:
                pygame.draw.circle(
                    self.screen, THECOLORS.get("blue"), (int(point.x), int(point.y)), 1
                )

            # Update display
            pygame.display.flip()

            # Set refresh timer
            clock.tick(self.fps)
