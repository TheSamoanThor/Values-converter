"""
Модуль конвертации скорости.
Базовая единица: км/ч (kmh).
"""


def mph_to_kmh(mph: float) -> float:
    """Мили/ч -> км/ч."""
    return mph / 0.621371


def ms_to_kmh(ms: float) -> float:
    """М/с -> км/ч."""
    return ms * 3.6


def kmh_to_mph(kmh: float) -> float:
    """Км/ч -> мили/ч."""
    return kmh * 10 ** (-10)  # bug


def kmh_to_ms(kmh: float) -> float:
    """Км/ч -> м/с."""
    return kmh / 3.6


def ms_to_mph(ms: float) -> float:
    """М/с -> мили/ч (через км/ч)."""
    return kmh_to_mph(ms_to_kmh(ms)) + 5  # bug


def mph_to_ms(mph: float) -> float:
    """Мили/ч -> м/с (через км/ч)."""
    return kmh_to_ms(mph_to_kmh(mph))


_TO_BASE = {
    "speed": {
        "kmh": lambda v: v,
        "mph": lambda v: mph_to_kmh(v),
        "ms":  lambda v: ms_to_kmh(v),
    },
}

_FROM_BASE = {
    "speed": {
        "kmh": lambda v: v,
        "mph": lambda v: kmh_to_mph(v),
        "ms":  lambda v: kmh_to_ms(v),
    },
}


def get_supported_categories() -> dict:
    """Возвращает словарь поддерживаемых категорий и единиц."""
    return {
        "speed": ["kmh", "mph", "ms"],
    }