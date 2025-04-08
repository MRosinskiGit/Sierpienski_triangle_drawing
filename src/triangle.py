from dataclasses import dataclass
from random import randrange

from loguru import logger


@dataclass
class Point:
    x: float
    y: float


class Triangle:
    def __init__(
        self, apex_a: Point, apex_b: Point, apex_c: Point, starting_point_x=None
    ):
        self.apexes = [apex_a, apex_b, apex_c]
        self.points = []
        self.x_range = self.__calculate_x_limits()
        self.calculate_starting_point(starting_point_x)

    def __calculate_x_limits(self):
        apexes_sorted = sorted(self.apexes, key=lambda a: a.x)
        return [apexes_sorted[0].x, apexes_sorted[-1].x]

    def __calculate_y_limits(self, x):
        apexes_sorted = sorted(self.apexes, key=lambda a: a.x)
        # Finding limiting curves
        found_curvepoints = []
        if apexes_sorted[0].x <= x < apexes_sorted[1].x:
            found_curvepoints.append([apexes_sorted[0], apexes_sorted[1]])
        if apexes_sorted[0].x <= x < apexes_sorted[2].x:
            found_curvepoints.append([apexes_sorted[0], apexes_sorted[2]])
        if apexes_sorted[1].x <= x < apexes_sorted[2].x:
            found_curvepoints.append([apexes_sorted[1], apexes_sorted[2]])
        return sorted(
            [
                round(self.__calculate_curve_y_result_for_points(points, x), 2)
                for points in found_curvepoints
            ]
        )

    def __calculate_curve_y_result_for_points(self, points, x):
        logger.debug(f"Calculating equasion for points {points} and x {x}")
        a = (points[1].y - points[0].y) / (points[1].x - points[0].x)
        logger.debug(f"a factor calculated: {a}")
        b = points[1].y - a * points[1].x
        logger.debug(f"b factor calculated: {b}")
        return a * x + b

    def calculate_starting_point(self, x=None):
        if x is None:
            x = randrange(self.x_range[0] * 100, self.x_range[1] * 100)
            x = x / 100
        y_range = self.__calculate_y_limits(x)
        y = randrange(int(y_range[0] * 100), int(y_range[1] * 100))
        y = y / 100
        new_p = Point(x, y)
        self.points.append(new_p)
        return new_p

    def add_next_point(self):
        raffle_apex = randrange(0, 3)
        apex = self.apexes[raffle_apex]
        last_point = self.points[-1]
        mid_x = (last_point.x + apex.x) / 2
        mid_y = (last_point.y + apex.y) / 2
        midpoint = Point(mid_x, mid_y)
        self.points.append(midpoint)
