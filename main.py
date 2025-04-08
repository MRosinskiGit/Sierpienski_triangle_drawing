from src.triangle import Point, Triangle
from src.ui import GameUI


def main():
    apex_a = Point(100, 100)
    apex_b = Point(500, 200)
    apex_c = Point(200, 400)
    tri = Triangle(apex_a, apex_b, apex_c)
    Game = GameUI(tri)
    Game.fps = 400
    Game.start_game()


if __name__ == "__main__":
    main()
