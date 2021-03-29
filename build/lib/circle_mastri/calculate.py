"""Circle package main functions."""
import math


def calculate_circumference(radius: float):
    """
    Calculate circumference and area of circle with given radius.
    """
    if radius < 0:
        raise ValueError("Radius must be positive!")
    return radius * 2 * math.pi


def calculate_area(radius: float):
    """
    Calculate circumference and area of circle with given radius.
    """
    if radius < 0:
        raise ValueError("Radius must be positive!")
    return radius ** 2 * math.pi
