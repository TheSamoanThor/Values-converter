"""
Модуль конвертации массы.
Базовая единица: килограмм (kg).
"""


def pounds_to_kilograms(lb: float) -> float:
    """Фунты -> килограммы."""
    return lb / 2.20462


def grams_to_kilograms(g: float) -> float:
    """Граммы -> килограммы."""
    return g / 1000


def ounces_to_kilograms(oz: float) -> float:
    """Унции -> килограммы."""
    return oz / 35.274


def kilograms_to_pounds(kg: float) -> float:
    """Килограммы -> фунты."""
    return kg * 2.20462


def kilograms_to_grams(kg: float) -> float:
    """Килограммы -> граммы."""
    return kg * 1000


def kilograms_to_ounces(kg: float) -> float:
    """Килограммы -> унции."""
    return kg * 35.274


def grams_to_ounces(g: float) -> float:
    """Граммы -> унции."""
    return g * 0.035274

def ounces_to_grams(oz: float) -> float:
    """Унции -> граммы."""
    return oz / 0.035274


_TO_BASE = {
    "mass": {
        "kg": lambda v: v,
        "lb": lambda v: pounds_to_kilograms(v),
        "g":  lambda v: grams_to_kilograms(v),
        "oz": lambda v: ounces_to_kilograms(v),
    },
}

_FROM_BASE = {
    "mass": {
        "kg": lambda v: v,
        "lb": lambda v: kilograms_to_pounds(v),
        "g":  lambda v: kilograms_to_grams(v),
        "oz": lambda v: kilograms_to_ounces(v),
    },
}


def get_supported_categories() -> dict:
    """Возвращает словарь поддерживаемых категорий и единиц."""
    return {
        "mass": ["kg", "lb", "g", "oz"],
    }