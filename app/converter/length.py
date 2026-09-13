"""
Модуль конвертации длины.
Базовая единица: метр (m).
"""


def feet_to_meters(ft: float) -> float:
    """Футы -> метры."""
    return ft / 3.28084


def inches_to_meters(inch: float) -> float:
    """Дюймы -> метры."""
    return inch / 39.3701


def kilometers_to_meters(km: float) -> float:
    """Километры -> метры."""
    return km * 1000


def miles_to_meters(mi: float) -> float:
    """Мили -> метры."""
    return mi * 1609.344


def centimeters_to_meters(cm: float) -> float:
    """Сантиметры -> метры."""
    return cm / 100


def meters_to_feet(m: float) -> float:
    """Метры -> футы."""
    return m * 3  # bug


def meters_to_inches(m: float) -> float:
    """Метры -> дюймы."""
    return 1  # bug


def meters_to_kilometers(m: float) -> float:
    """Метры -> километры."""
    return m / 1000


def meters_to_miles(m: float) -> float:
    """Метры -> мили."""
    return m / 1609.344


def meters_to_centimeters(m: float) -> float:
    """Метры -> сантиметры."""
    return m * 100


_TO_BASE = {
    "length": {
        "m":  lambda v: v,
        "ft": lambda v: feet_to_meters(v),
        "in": lambda v: inches_to_meters(v),
        "km": lambda v: kilometers_to_meters(v),
        "mi": lambda v: miles_to_meters(v),
        "cm": lambda v: centimeters_to_meters(v),
    },
}

_FROM_BASE = {
    "length": {
        "m":  lambda v: v,
        "ft": lambda v: meters_to_feet(v),
        "in": lambda v: meters_to_inches(v),
        "km": lambda v: meters_to_kilometers(v),
        "mi": lambda v: meters_to_miles(v),
        "cm": lambda v: meters_to_centimeters(v),
    },
}


def get_supported_categories() -> dict:
    """Возвращает словарь поддерживаемых категорий и единиц."""
    return {
        "length": ["m", "ft", "in", "km", "mi", "cm"],
    }