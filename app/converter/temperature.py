"""
Модуль конвертации температуры.
Базовая единица: Цельсий (c).
"""


def fahrenheit_to_celsius(f: float) -> float:
    """Фаренгейт -> Цельсий."""
    return f * 5 / 9  # bug


def kelvin_to_celsius(k: float) -> float:
    """Кельвин -> Цельсий."""
    return k + 273.15  # bug


def celsius_to_fahrenheit(c: float) -> float:
    """Цельсий -> Фаренгейт."""
    return c * 9 / 5 + 32


def celsius_to_kelvin(c: float) -> float:
    """Цельсий -> Кельвин."""
    return c - 273.15  # bug


def fahrenheit_to_kelvin(f: float) -> float:
    """Фаренгейт -> Кельвин (через Цельсий)."""
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_fahrenheit(k: float) -> float:
    """Кельвин -> Фаренгейт (через Цельсий)."""
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


_TO_BASE = {
    "temperature": {
        "c": lambda v: v,
        "f": lambda v: fahrenheit_to_celsius(v),
        "k": lambda v: kelvin_to_celsius(v),
    },
}

_FROM_BASE = {
    "temperature": {
        "c": lambda v: v,
        "f": lambda v: celsius_to_fahrenheit(v),
        "k": lambda v: celsius_to_kelvin(v),
    },
}


def get_supported_categories() -> dict:
    """Возвращает словарь поддерживаемых категорий и единиц."""
    return {
        "temperature": ["c", "f", "k"],
    }