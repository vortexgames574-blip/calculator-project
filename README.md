# Calculator Project

Учебный проект — простой калькулятор на Python с веб-интерфейсом.

## Установка
git clone https://github.com/username/calculator-project.git
cd calculator-project
pip install -r requirements.txt

## Запуск (консоль)
python src/calculator.py

## Запуск (веб-интерфейс)
python app.py

Откройте в браузере: http://127.0.0.1:5000/calc?op=add&a=2&b=3
Доступные операции: add, sub, mul, div, pow, mod.

## Тестирование
python -m unittest discover tests -v

## Структура проекта
calculator-project/
├── src/               # исходный код
├── tests/             # тесты
├── docs/              # документация
├── .github/workflows/ # CI/CD
├── app.py             # Flask-приложение
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE

## Автор
Нисифиров Ярослав, гр. ИС-4
ПРОЕКТ ГОТОВ К СДАЧЕ