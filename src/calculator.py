"""
Модуль калькулятора с базовыми арифметическими операциями.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def power(a, b):
    raise NotImplementedError("Реализуется в ветке feature/power-function")

def modulo(a, b):
    """Остаток от деления a на b."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a % b

def main():
    print("=== Калькулятор ===")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"17 % 5 = {modulo(17, 5)}")
    print("Готово!")

if __name__ == "__main__":
    main()
