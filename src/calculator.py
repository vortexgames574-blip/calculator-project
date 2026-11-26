"""
Модуль калькулятора с базовыми арифметическими операциями.
"""

def add(a, b):
    """Сложение двух чисел."""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел."""
    return a - b

def multiply(a, b):
    """Умножение двух чисел."""
    return a * b

def divide(a, b):
    """Деление двух чисел с проверкой деления на ноль."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def power(a, b):
    """Возведение в степень. (заглушка)"""
    raise NotImplementedError("Реализуется в ветке feature/power-function")

def modulo(a, b):
    """Остаток от деления. (заглушка)"""
    raise NotImplementedError("Реализуется в ветке feature/modulo-function")

def main():
    """Точка входа: демонстрация работы калькулятора."""
    print("=== Калькулятор ===")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print("Готово!")

if __name__ == "__main__":
    main()
