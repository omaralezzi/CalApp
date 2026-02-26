"""Entry point for the calculator application."""

from calculator import add, subtract, multiply, divide


def run():
    print("Simple Python Calculator")
    while True:
        try:
            expr = input("Enter expression (or 'quit' to exit): ")
            if expr.lower() in ("quit", "exit"):
                break
            # naive parsing
            a, op, b = expr.split()
            a, b = float(a), float(b)
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print("Unsupported operator")
                continue
            print("Result:", result)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    run()
