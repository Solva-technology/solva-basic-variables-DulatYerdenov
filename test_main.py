import subprocess
import sys
import os
import re

def run_main_script():
    """Helper function to run main.py and capture its output."""
    command = [sys.executable, "main.py"]
    
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    env['PYTHONUTF8'] = '1'

    process = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding='utf-8',
        env=env
    )
    return process

def get_output_lines():
    """Runs the script and returns stripped output lines."""
    process = run_main_script()
    assert process.returncode == 0, f"Скрипт завершился с ошибкой:\n{process.stderr}"
    return process.stdout.strip().split('\n')

def test_name_is_filled():
    """Тест проверяет, что имя заполнено."""
    lines = get_output_lines()
    name_line = lines[0]
    assert "Меня зовут: " in name_line, "Первая строка должна содержать 'Меня зовут: '"
    name = name_line.replace("Меня зовут: ", "").strip()
    assert name != "", "Имя не должно быть пустым."
    assert name != '""', "Имя не должно быть пустой строкой."

def test_age_is_filled_and_positive():
    """Тест проверяет, что возраст — положительное число."""
    lines = get_output_lines()
    age_line = lines[1]
    assert "Мой возраст: " in age_line, "Вторая строка должна содержать 'Мой возраст: '"
    age_str = age_line.replace("Мой возраст: ", "").strip()
    assert age_str.isdigit(), "Возраст должен быть числом."
    age = int(age_str)
    assert age > 0, "Возраст должен быть больше нуля."

def test_future_age_is_correct():
    """Тест проверяет правильность расчета возраста через 10 лет."""
    lines = get_output_lines()
    age_line = lines[1]
    future_age_line = lines[2]
    
    age_str = age_line.replace("Мой возраст: ", "").strip()
    age = int(age_str)
    
    assert "Через 10 лет мне будет: " in future_age_line, "Третья строка должна содержать 'Через 10 лет мне будет: '"
    future_age_str = future_age_line.replace("Через 10 лет мне будет: ", "").strip()
    assert future_age_str.isdigit(), "Значение будущего возраста должно быть числом."
    future_age = int(future_age_str)
    
    assert future_age == age + 10, "Расчет будущего возраста неверный."

def test_apples_calculation_is_correct():
    """Тест проверяет правильность расчета оставшихся яблок."""
    lines = get_output_lines()
    apples_line = lines[3]
    assert "У меня осталось яблок: " in apples_line, "Четвертая строка должна содержать 'У меня осталось яблок: '"
    
    apples_left_str = apples_line.replace("У меня осталось яблок: ", "").strip()
    assert apples_left_str.isdigit(), "Количество оставшихся яблок должно быть числом."
    apples_left = int(apples_left_str)
    
    assert apples_left == 15 - 4, "Расчет оставшихся яблок неверный."
