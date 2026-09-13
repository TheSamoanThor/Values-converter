"""
Модульные тесты для блока конвертации температуры.

Проверяются функции из converter_only_temperature.py:
    - celsius_to_fahrenheit
    - fahrenheit_to_celsius
    - celsius_to_kelvin
    - kelvin_to_celsius
    - fahrenheit_to_kelvin
    - kelvin_to_fahrenheit
    - is_number
    - round_result
    - format_result
    - convert (для category="temperature")
"""

import pytest

from converter.temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
    get_supported_categories
)

from converter.helpers import (
    is_number,
    round_result,
    format_result,
)

from converter import convert


# ============================================================
# ЦЕЛЬСИЙ -> ФАРЕНГЕЙТ
# ============================================================

class TestCelsiusToFahrenheit:
    """Тесты для функции celsius_to_fahrenheit."""

    def test_freezing_point(self):
        """0 °C = 32 °F (точка замерзания воды)."""
        assert celsius_to_fahrenheit(0) == pytest.approx(32.0)

    def test_boiling_point(self):
        """100 °C = 212 °F (точка кипения воды)."""
        assert celsius_to_fahrenheit(100) == pytest.approx(212.0)

    def test_negative_temperature(self):
        """-40 °C = -40 °F (точка совпадения шкал)."""
        assert celsius_to_fahrenheit(-40) == pytest.approx(-40.0)

    def test_body_temperature(self):
        """36.6 °C ≈ 97.88 °F (нормальная температура тела)."""
        assert celsius_to_fahrenheit(36.6) == pytest.approx(97.88)

    def test_zero_returns_32(self):
        """Проверка, что при 0 не возвращается 0 (защита от мутанта)."""
        assert celsius_to_fahrenheit(0) != 0

    def test_negative_celsius(self):
        """-10 °C = 14 °F."""
        assert celsius_to_fahrenheit(-10) == pytest.approx(14.0)

    def test_sign_positive_input(self):
        """Для положительного °C результат в °F больше 32."""
        assert celsius_to_fahrenheit(50) > 32

    def test_sign_negative_input(self):
        """Для отрицательного °C результат в °F меньше 32."""
        assert celsius_to_fahrenheit(-50) < 32


# ============================================================
# ФАРЕНГЕЙТ -> ЦЕЛЬСИЙ
# ============================================================

class TestFahrenheitToCelsius:
    """Тесты для функции fahrenheit_to_celsius."""

    def test_freezing_point(self):
        """32 °F = 0 °C."""
        assert fahrenheit_to_celsius(32) == pytest.approx(0.0)

    def test_boiling_point(self):
        """212 °F = 100 °C."""
        assert fahrenheit_to_celsius(212) == pytest.approx(100.0)

    def test_negative_temperature(self):
        """-40 °F = -40 °C."""
        assert fahrenheit_to_celsius(-40) == pytest.approx(-40.0)

    def test_body_temperature(self):
        """98.6 °F ≈ 37 °C."""
        assert fahrenheit_to_celsius(98.6) == pytest.approx(37.0, abs=0.1)

    def test_zero_fahrenheit_not_zero_celsius(self):
        """0 °F ≠ 0 °C (защита от забытого вычитания 32)."""
        assert fahrenheit_to_celsius(0) != 0

    def test_zero_fahrenheit_value(self):
        """0 °F ≈ -17.78 °C."""
        assert fahrenheit_to_celsius(0) == pytest.approx(-17.7778, abs=1e-3)

    def test_sign_direction(self):
        """Для 100 °F результат должен быть меньше 100 °C."""
        assert fahrenheit_to_celsius(100) < 100


# ============================================================
# ЦЕЛЬСИЙ -> КЕЛЬВИН
# ============================================================

class TestCelsiusToKelvin:
    """Тесты для функции celsius_to_kelvin."""

    def test_absolute_zero(self):
        """-273.15 °C = 0 K."""
        assert celsius_to_kelvin(-273.15) == pytest.approx(0.0)

    def test_freezing_point(self):
        """0 °C = 273.15 K."""
        assert celsius_to_kelvin(0) == pytest.approx(273.15)

    def test_boiling_point(self):
        """100 °C = 373.15 K."""
        assert celsius_to_kelvin(100) == pytest.approx(373.15)

    def test_positive_shift(self):
        """Результат должен быть БОЛЬШЕ входного значения."""
        assert celsius_to_kelvin(25) > 25

    def test_negative_celsius(self):
        """-100 °C = 173.15 K."""
        assert celsius_to_kelvin(-100) == pytest.approx(173.15)


# ============================================================
# КЕЛЬВИН -> ЦЕЛЬСИЙ
# ============================================================

class TestKelvinToCelsius:
    """Тесты для функции kelvin_to_celsius."""

    def test_absolute_zero(self):
        """0 K = -273.15 °C."""
        assert kelvin_to_celsius(0) == pytest.approx(-273.15)

    def test_freezing_point(self):
        """273.15 K = 0 °C."""
        assert kelvin_to_celsius(273.15) == pytest.approx(0.0)

    def test_boiling_point(self):
        """373.15 K = 100 °C."""
        assert kelvin_to_celsius(373.15) == pytest.approx(100.0)

    def test_negative_shift(self):
        """Результат должен быть МЕНЬШЕ входного значения."""
        assert kelvin_to_celsius(300) < 300

    def test_high_kelvin(self):
        """1000 K = 726.85 °C."""
        assert kelvin_to_celsius(1000) == pytest.approx(726.85)


# ============================================================
# СОВМЕЩЁННЫЕ КОНВЕРТАЦИИ (ЧЕРЕЗ ЦЕЛЬСИЙ)
# ============================================================

class TestFahrenheitKelvin:
    """Тесты для fahrenheit_to_kelvin и kelvin_to_fahrenheit."""

    def test_fahrenheit_to_kelvin_freezing(self):
        """32 °F = 273.15 K."""
        assert fahrenheit_to_kelvin(32) == pytest.approx(273.15)

    def test_fahrenheit_to_kelvin_boiling(self):
        """212 °F = 373.15 K."""
        assert fahrenheit_to_kelvin(212) == pytest.approx(373.15)

    def test_kelvin_to_fahrenheit_freezing(self):
        """273.15 K = 32 °F."""
        assert kelvin_to_fahrenheit(273.15) == pytest.approx(32.0)

    def test_kelvin_to_fahrenheit_boiling(self):
        """373.15 K = 212 °F."""
        assert kelvin_to_fahrenheit(373.15) == pytest.approx(212.0)

    def test_fahrenheit_to_kelvin_absolute_zero(self):
        """-459.67 °F = 0 K."""
        assert fahrenheit_to_kelvin(-459.67) == pytest.approx(0.0, abs=1e-2)

    def test_kelvin_to_fahrenheit_absolute_zero(self):
        """0 K = -459.67 °F."""
        assert kelvin_to_fahrenheit(0) == pytest.approx(-459.67, abs=1e-2)


# ============================================================
# ГРАНИЧНЫЕ СЛУЧАИ
# ============================================================

class TestTemperatureBoundary:
    """Граничные случаи температуры."""

    def test_below_absolute_zero_no_crash(self):
        """Ниже абсолютного нуля функция не падает."""
        assert celsius_to_kelvin(-300) == pytest.approx(-26.85)

    def test_very_large_value(self):
        """Очень большие значения не переполняют float."""
        assert celsius_to_fahrenheit(1e6) == pytest.approx(1800032.0)

    def test_very_small_value(self):
        """Очень малые значения обрабатываются корректно."""
        assert celsius_to_fahrenheit(1e-6) == pytest.approx(32.0000018, abs=1e-5)

    def test_roundtrip_c_f(self):
        """c -> f -> c возвращает исходное значение."""
        for v in [-273.15, -40, 0, 25, 100]:
            assert fahrenheit_to_celsius(celsius_to_fahrenheit(v)) == pytest.approx(v)

    def test_roundtrip_c_k(self):
        """c -> k -> c возвращает исходное значение."""
        for v in [-273.15, 0, 100, 1000]:
            assert kelvin_to_celsius(celsius_to_kelvin(v)) == pytest.approx(v)

    def test_roundtrip_f_k(self):
        """f -> k -> f возвращает исходное значение."""
        for v in [-40, 0, 32, 100, 212]:
            assert kelvin_to_fahrenheit(fahrenheit_to_kelvin(v)) == pytest.approx(v, abs=1e-4)

    def test_sign_direction_c_to_k(self):
        """Для положительных °C результат в K больше."""
        assert celsius_to_kelvin(50) > 50

    def test_sign_direction_k_to_c(self):
        """Для положительных K результат в °C меньше."""
        assert kelvin_to_celsius(300) < 300

    def test_zero_celsius_to_kelvin(self):
        """Ноль по Цельсию — не ноль по Кельвину."""
        assert celsius_to_kelvin(0) != 0

    def test_zero_kelvin_to_celsius(self):
        """Ноль по Кельвину — не ноль по Цельсию."""
        assert kelvin_to_celsius(0) != 0


# ============================================================
# УНИВЕРСАЛЬНАЯ ФУНКЦИЯ convert() ДЛЯ ТЕМПЕРАТУРЫ
# ============================================================

class TestConvertTemperature:
    """Тесты для convert() в категории temperature."""

    def test_c_to_f(self):
        assert convert("temperature", "c", "f", 100) == pytest.approx(212.0)

    def test_f_to_c(self):
        assert convert("temperature", "f", "c", 32) == pytest.approx(0.0)

    def test_c_to_k(self):
        assert convert("temperature", "c", "k", 0) == pytest.approx(273.15)

    def test_k_to_c(self):
        assert convert("temperature", "k", "c", 273.15) == pytest.approx(0.0)

    def test_f_to_k(self):
        assert convert("temperature", "f", "k", 32) == pytest.approx(273.15)

    def test_k_to_f(self):
        assert convert("temperature", "k", "f", 273.15) == pytest.approx(32.0)

    def test_same_unit_returns_same_value(self):
        """c -> c должно вернуть исходное значение."""
        assert convert("temperature", "c", "c", 42) == 42

    def test_same_unit_k(self):
        assert convert("temperature", "k", "k", 300) == 300

    def test_same_unit_f(self):
        assert convert("temperature", "f", "f", 100) == 100

    def test_unknown_category_raises(self):
        """Неизвестная категория — ValueError."""
        with pytest.raises(ValueError):
            convert("unknown", "c", "f", 100)

    def test_unknown_from_unit_raises(self):
        """Неизвестная исходная единица — ValueError."""
        with pytest.raises(ValueError):
            convert("temperature", "x", "f", 100)

    def test_unknown_to_unit_raises(self):
        """Неизвестная целевая единица — ValueError."""
        with pytest.raises(ValueError):
            convert("temperature", "c", "x", 100)

    def test_empty_from_unit_raises(self):
        with pytest.raises(ValueError):
            convert("temperature", "", "c", 100)

    def test_empty_to_unit_raises(self):
        with pytest.raises(ValueError):
            convert("temperature", "c", "", 100)

    def test_negative_value_works(self):
        """Отрицательные значения должны конвертироваться."""
        assert convert("temperature", "c", "f", -40) == pytest.approx(-40.0)

    def test_zero_c_to_c(self):
        assert convert("temperature", "c", "c", 0) == 0

    @pytest.mark.parametrize("value, expected", [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (37, 98.6),
    ])
    def test_c_to_f_parametrized(self, value, expected):
        """Параметризованная проверка c -> f."""
        assert convert("temperature", "c", "f", value) == pytest.approx(expected, abs=0.1)


# ============================================================
# ИСКЛЮЧИТЕЛЬНЫЕ СИТУАЦИИ
# ============================================================

class TestTemperatureErrors:
    """Проверка исключительных ситуаций."""

    def test_convert_empty_from_unit(self):
        with pytest.raises(ValueError):
            convert("temperature", "", "c", 100)

    def test_convert_empty_to_unit(self):
        with pytest.raises(ValueError):
            convert("temperature", "c", "", 100)

    def test_convert_unknown_category(self):
        with pytest.raises(ValueError):
            convert("weight", "c", "f", 100)

    def test_convert_unknown_from_unit(self):
        with pytest.raises(ValueError):
            convert("temperature", "xyz", "c", 100)

    def test_convert_unknown_to_unit(self):
        with pytest.raises(ValueError):
            convert("temperature", "c", "xyz", 100)


# ============================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

class TestHelpers:
    """Тесты вспомогательных функций."""

    def test_is_number_true_int(self):
        assert is_number("42") is True

    def test_is_number_true_float(self):
        assert is_number("3.14") is True

    def test_is_number_true_scientific(self):
        assert is_number("-1e5") is True

    def test_is_number_false_text(self):
        assert is_number("abc") is False

    def test_is_number_false_empty(self):
        assert is_number("") is False

    def test_is_number_false_none(self):
        assert is_number(None) is False

    def test_round_result_default(self):
        assert round_result(3.14159) == 3.1416

    def test_round_result_custom_digits(self):
        assert round_result(3.14159, 2) == 3.14

    def test_round_result_zero_digits(self):
        assert round_result(3.14159, 0) == 3.0

    def test_format_result_returns_string(self):
        assert isinstance(format_result(3.14159), str)

    def test_format_result_rounds(self):
        assert format_result(3.14159, 2) == "3.14"

    def test_format_result_default(self):
        assert format_result(3.14159) == "3.1416"


class TestHelpersTemperatureFile:
    """Тесты дополнительных функций в файле температур"""
    def test_get_supported_categories(self):
        result = get_supported_categories()
        assert "temperature" in result
        assert set(result["temperature"]) == {"c", "f", "k"}