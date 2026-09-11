"""
Точка входа приложения.
Запускает Flask-сервер и автоматически открывает браузер
с интерфейсом конвертера.
"""

import threading
import webbrowser

from flask import Flask, render_template, request

from converter import (
    convert,
    format_result,
    get_supported_categories,
    is_number,
)

app = Flask(__name__)

# Человекочитаемые названия единиц
UNIT_LABELS = {
    # length
    "m": "Метры (m)",
    "ft": "Футы (ft)",
    "in": "Дюймы (in)",
    "km": "Километры (km)",
    "mi": "Мили (mi)",
    "cm": "Сантиметры (cm)",
    # mass
    "kg": "Килограммы (kg)",
    "lb": "Фунты (lb)",
    "g": "Граммы (g)",
    "oz": "Унции (oz)",
    # temperature
    "c": "Цельсий (°C)",
    "f": "Фаренгейт (°F)",
    "k": "Кельвин (K)",
    # volume
    "l": "Литры (L)",
    "gal": "Галлоны (gal)",
    "ml": "Миллилитры (ml)",
    "fl_oz": "Жидкие унции (fl oz)",
    # speed
    "kmh": "Км/ч (km/h)",
    "mph": "Мили/ч (mph)",
    "ms": "М/с (m/s)",
    # area
    "m2": "Кв. метры (m²)",
    "ft2": "Кв. футы (ft²)",
    "ha": "Гектары (ha)",
    "ac": "Акры (ac)",
}

CATEGORY_LABELS = {
    "length": "Длина",
    "mass": "Масса",
    "temperature": "Температура",
    "volume": "Объём",
    "speed": "Скорость",
    "area": "Площадь",
}


@app.route("/", methods=["GET", "POST"])
def index():
    categories = get_supported_categories()
    result = None
    error = None

    # Значения по умолчанию
    selected_category = "length"
    from_unit = "m"
    to_unit = "ft"
    input_value = ""

    if request.method == "POST":
        selected_category = request.form.get("category", "length")
        from_unit = request.form.get("from_unit", "m")
        to_unit = request.form.get("to_unit", "ft")
        input_value = request.form.get("value", "").strip()

        # Валидация
        if not input_value:
            error = "Введите значение для конвертации."
        elif not is_number(input_value):
            error = "Введённое значение не является числом."
        else:
            try:
                value = float(input_value)
                converted = convert(selected_category, from_unit, to_unit, value)
                result = (
                    f"{format_result(value)} {UNIT_LABELS.get(from_unit, from_unit)}"
                    f" = "
                    f"{format_result(converted)} {UNIT_LABELS.get(to_unit, to_unit)}"
                )
            except ValueError as e:
                error = str(e)

    return render_template(
        "index.html",
        categories=categories,
        category_labels=CATEGORY_LABELS,
        unit_labels=UNIT_LABELS,
        selected_category=selected_category,
        from_unit=from_unit,
        to_unit=to_unit,
        input_value=input_value,
        result=result,
        error=error,
    )


def open_browser():
    """Открывает браузер с интерфейсом приложения."""
    webbrowser.open_new("http://127.0.0.1:5000/")


if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    try:
        app.run(host="127.0.0.1", port=5000, debug=False)
    except KeyboardInterrupt:
        print("\nСервер остановлен пользователем.")