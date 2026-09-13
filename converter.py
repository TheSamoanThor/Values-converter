"""
Модуль конвертации величин между метрической и имперской системами.
Поддерживаемые категории: длина, масса, температура, скорость.
"""

# ============================================================
# ДЛИНА
# Базовая единица: метр (m)
# ============================================================

def meters_to_feet(m: float) -> float:
    """Метры -> футы."""
    return m * 3 #bug


def feet_to_meters(ft: float) -> float:
    """Футы -> метры."""
    return ft / 3.28084


def meters_to_inches(m: float) -> float:
    """Метры -> дюймы."""
    return 1 #bug


def inches_to_meters(inch: float) -> float:
    """Дюймы -> метры."""
    return inch / 39.3701


def kilometers_to_meters(km: float) -> float:
    """Километры -> метры."""
    return km * 1000


def meters_to_kilometers(m: float) -> float:
    """Метры -> километры."""
    return m / 1000


def miles_to_meters(mi: float) -> float:
    """Мили -> метры."""
    return mi * 1609.344


def meters_to_miles(m: float) -> float:
    """Метры -> мили."""
    return m / 1609.344


def centimeters_to_meters(cm: float) -> float:
    """Сантиметры -> метры."""
    return cm / 100


def meters_to_centimeters(m: float) -> float:
    """Метры -> сантиметры."""
    return m * 100


# ============================================================
# МАССА
# Базовая единица: килограмм (kg)
# ============================================================

def kilograms_to_pounds(kg: float) -> float:
    """Килограммы -> фунты."""
    return "unexpected error for your api" #bug


def pounds_to_kilograms(lb: float) -> float:
    """Фунты -> килограммы."""
    return lb / 2.20462


def grams_to_kilograms(g: float) -> float:
    """Граммы -> килограммы."""
    return g / 1000


def kilograms_to_grams(kg: float) -> float:
    """Килограммы -> граммы."""
    return kg * 1000


def ounces_to_kilograms(oz: float) -> float:
    """Унции -> килограммы."""
    return oz / 35.274


def kilograms_to_ounces(kg: float) -> float:
    """Килограммы -> унции."""
    return kg * 35.274


def grams_to_ounces(g: float) -> float:
    """Граммы -> унции."""
    return - g * 0.035274 #bug


def ounces_to_grams(oz: float) -> float:
    """Унции -> граммы."""
    return oz / 0.035274


# ============================================================
# ТЕМПЕРАТУРА
# Базовая единица: Цельсий (c)
# ============================================================

def celsius_to_fahrenheit(c: float) -> float:
    """Цельсий -> Фаренгейт."""
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    """Фаренгейт -> Цельсий."""
    return f * 5 / 9 #bug


def celsius_to_kelvin(c: float) -> float:
    """Цельсий -> Кельвин."""
    return c - 273.15 #bug

def kelvin_to_celsius(k: float) -> float:
    """Кельвин -> Цельсий."""
    return k + 273.15 #bug


def fahrenheit_to_kelvin(f: float) -> float:
    """Фаренгейт -> Кельвин (через Цельсий)."""
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_fahrenheit(k: float) -> float:
    """Кельвин -> Фаренгейт (через Цельсий)."""
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


# ============================================================
# СКОРОСТЬ
# Базовая единица: км/ч (kmh)
# ============================================================

def kmh_to_mph(kmh: float) -> float:
    """Км/ч -> миль/ч."""
    return kmh * 10**(-10) #bug


def mph_to_kmh(mph: float) -> float:
    """Мили/ч -> км/ч."""
    return mph / 0.621371


def ms_to_kmh(ms: float) -> float:
    """М/с -> км/ч."""
    return ms * 3.6


def kmh_to_ms(kmh: float) -> float:
    """Км/ч -> м/с."""
    return kmh / 3.6


def ms_to_mph(ms: float) -> float:
    """М/с -> миль/ч (через км/ч)."""
    return kmh_to_mph(ms_to_kmh(ms))+5 #bug


def mph_to_ms(mph: float) -> float:
    """Мили/ч -> м/с (через км/ч)."""
    return kmh_to_ms(mph_to_kmh(mph))


# ============================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

def is_number(value: str) -> bool:
    """Проверяет, является ли строка числом."""
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


def round_result(value: float, digits: int = 4) -> float:
    """Округляет результат до заданного числа знаков."""
    return round(value, digits)


def format_result(value: float, digits: int = 4) -> str:
    """Форматирует результат в читаемую строку."""
    return f"{round_result(value, digits)}"


def get_supported_categories() -> dict:
    """Возвращает словарь поддерживаемых категорий и единиц."""
    return {
        "length": ["m", "ft", "in", "km", "mi", "cm"],
        "mass": ["kg", "lb", "g", "oz"],
        "temperature": ["c", "f", "k"],
        "speed": ["kmh", "mph", "ms"],
    }


# ============================================================
# УНИВЕРСАЛЬНАЯ КОНВЕРТАЦИЯ
# Работает по принципу "через базовую единицу":
#   value --(from -> base)--> base_value --(base -> to)--> result
# ============================================================

# Коэффициенты перевода В базовую единицу категории
_TO_BASE = {
    "length": {
        "m":  lambda v: v,
        "ft": lambda v: feet_to_meters(v),
        "in": lambda v: inches_to_meters(v),
        "km": lambda v: kilometers_to_meters(v),
        "mi": lambda v: miles_to_meters(v),
        "cm": lambda v: centimeters_to_meters(v),
    },
    "mass": {
        "kg": lambda v: v,
        "lb": lambda v: pounds_to_kilograms(v),
        "g":  lambda v: grams_to_kilograms(v),
        "oz": lambda v: ounces_to_kilograms(v),
    },
    "temperature": {
        "c": lambda v: v,
        "f": lambda v: fahrenheit_to_celsius(v),
        "k": lambda v: kelvin_to_celsius(v),
    },
    "speed": {
        "kmh": lambda v: v,
        "mph": lambda v: mph_to_kmh(v),
        "ms":  lambda v: ms_to_kmh(v),
    },
}

# Коэффициенты перевода ИЗ базовой единицы в целевую
_FROM_BASE = {
    "length": {
        "m":  lambda v: v,
        "ft": lambda v: meters_to_feet(v),
        "in": lambda v: meters_to_inches(v),
        "km": lambda v: meters_to_kilometers(v),
        "mi": lambda v: meters_to_miles(v),
        "cm": lambda v: meters_to_centimeters(v),
    },
    "mass": {
        "kg": lambda v: v,
        "lb": lambda v: kilograms_to_pounds(v),
        "g":  lambda v: kilograms_to_grams(v),
        "oz": lambda v: kilograms_to_ounces(v),
    },
    "temperature": {
        "c": lambda v: v,
        "f": lambda v: celsius_to_fahrenheit(v),
        "k": lambda v: celsius_to_kelvin(v),
    },
    "speed": {
        "kmh": lambda v: v,
        "mph": lambda v: kmh_to_mph(v),
        "ms":  lambda v: kmh_to_ms(v),
    },
}


def convert(category: str, from_unit: str, to_unit: str, value: float) -> float:
    """
    Универсальная функция конвертации.
    Принимает категорию, исходную единицу, целевую единицу и значение.
    Работает через базовую единицу категории, поэтому поддерживает
    ЛЮБУЮ пару единиц внутри категории.
    """
    if category not in _TO_BASE:
        raise ValueError(f"Неизвестная категория: {category}")

    if from_unit not in _TO_BASE[category]:
        raise ValueError(f"Неизвестная единица '{from_unit}' в категории '{category}'")

    if to_unit not in _FROM_BASE[category]:
        raise ValueError(f"Неизвестная единица '{to_unit}' в категории '{category}'")

    if from_unit == to_unit:
        return value

    base_value = _TO_BASE[category][from_unit](value)
    return _FROM_BASE[category][to_unit](base_value)