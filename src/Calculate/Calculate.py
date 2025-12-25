from asteval import Interpreter
import math

aeval = Interpreter()

superscript_map = {
    "²": "**2",
    "³": "**3",
    "⁴": "**4",
    "⁵": "**5",
    "⁶": "**6",
    "⁷": "**7",
    "⁸": "**8",
    "⁹": "**9",
    "¹⁰": "**10",
    "１": "1",
    "２": "2",
    "３": "3",
    "４": "4",
    "５": "5",
    "６": "6",
    "７": "7",
    "８": "8",
    "９": "9",
    "０": "0",
    "＋": "+",
    "－": "-",
    "×": "*",
    "÷": "/",
    "（": "(",
    "）": ")"
}

def normalize(expr: str) -> str:
    for k, v in superscript_map.items():
        expr = expr.replace(k, v)
    return expr

def eval(expr: str):
    expr = normalize(expr)
    aeval.error = []

    result = aeval(expr)

    if aeval.error:
        return None

    return result