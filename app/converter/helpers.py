"""
Вспомогательные функции, общие для всех модулей конвертации.
"""


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