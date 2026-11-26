"""Веб-интерфейс калькулятора на Flask."""
from flask import Flask, request, jsonify
from src.calculator import add, subtract, multiply, divide, power, modulo

app = Flask(__name__)

OPS = {
    "add": add,
    "sub": subtract,
    "mul": multiply,
    "div": divide,
    "pow": power,
    "mod": modulo,
}

@app.route("/")
def index():
    return (
        "<h1>Калькулятор API</h1>"
        "<p>Пример: <a href='/calc?op=add&a=2&b=3'>/calc?op=add&a=2&b=3</a></p>"
        "<p>Доступные op: add, sub, mul, div, pow, mod</p>"
    )

@app.route("/calc")
def calc():
    op = request.args.get("op", "")
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
    except ValueError:
        return jsonify({"error": "a и b должны быть числами"}), 400
    if op not in OPS:
        return jsonify({"error": f"Неизвестная операция: {op}"}), 400
    try:
        result = OPS[op](a, b)
        return jsonify({"op": op, "a": a, "b": b, "result": result})
    except (ValueError, NotImplementedError) as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
