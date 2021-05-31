from typing import Callable


def short_description(description: str) -> Callable:
    """Adds attribute 'short_description' with given value to a wrapped 'Callable'"""
    def wrapper(function: Callable) -> Callable:
        setattr(function, "short_description", description)
        return function
    return wrapper
