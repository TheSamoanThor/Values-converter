"""
Пакет конвертации величин.

Объединяет четыре изолированных модуля:
    - length       — длина
    - mass         — масса
    - temperature  — температура
    - speed        — скорость

Каждый модуль предоставляет:
    - функции прямого/обратного перевода в базовую единицу,
    - словари _TO_BASE и _FROM_BASE для универсальной конвертации,
    - функцию get_supported_categories() (для своего модуля).
"""

from . import length, mass, temperature, speed

# Итоговые таблицы: собираются из таблиц всех модулей
_TO_BASE = {}
_FROM_BASE = {}

for module in (length, mass, temperature, speed):
    _TO_BASE.update(module._TO_BASE)
    _FROM_BASE.update(module._FROM_BASE)


def get_supported_categories() -> dict:
    """Возвращает словарь всех поддерживаемых категорий и их единиц."""
    result = {}
    for module in (length, mass, temperature, speed):
        result.update(module.get_supported_categories())
    return result


def convert(category: str, from_unit: str, to_unit: str, value: float) -> float:
    """
    Универсальная функция конвертации через базовую единицу категории.
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


# Реэкспорт вспомогательных функций — чтобы app.py мог по-прежнему
# писать `from converter import is_number, format_result, ...`
from .helpers import is_number, round_result, format_result