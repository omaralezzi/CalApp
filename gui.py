"""Graphical calculator interface using Tkinter.

Layout and behavior are modeled loosely after the iPhone calculator.
"""

import tkinter as tk
from calculator import add, subtract, multiply, divide


class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # display entry
        self.display = tk.Entry(master, font=("Arial", 24), bd=10, relief="sunken", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # state variables
        self.current = ""
        self.operator = None
        self.operand = None

        # button specification: (text, row, col, width)
        buttons = [
            ("C", 1, 0), ("+/-", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3),
        ]

        for specs in buttons:
            text = specs[0]
            row = specs[1]
            col = specs[2]
            colspan = specs[3] if len(specs) > 3 else 1
            btn = tk.Button(master, text=text, font=("Arial", 18), command=lambda t=text: self._on_button(t))
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

        # make columns/rows expandable
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
        for j in range(4):
            master.grid_columnconfigure(j, weight=1)

    def _on_button(self, label):
        if label == "C":
            self._clear()
        elif label == "+/-":
            self._plus_minus()
        elif label == "%":
            self._percent()
        elif label == "=":
            self._calculate()
        elif label in "+-*/":
            self._set_operator(label)
        else:
            # digit or dot
            self._append(label)

    def _clear(self):
        self.current = ""
        self.operator = None
        self.operand = None
        self.display.delete(0, tk.END)

    def _plus_minus(self):
        if self.current:
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
            self.display_value(self.current)

    def _percent(self):
        try:
            value = float(self.current)
            value /= 100
            self.current = str(value)
            self.display_value(self.current)
        except ValueError:
            pass

    def _append(self, char):
        # avoid multiple dots
        if char == "." and "." in self.current:
            return
        self.current += char
        self.display_value(self.current)

    def _set_operator(self, op):
        if self.current:
            try:
                self.operand = float(self.current)
            except ValueError:
                self.operand = 0.0
            self.operator = op
            self.current = ""
            self.display.delete(0, tk.END)

    def _calculate(self):
        if self.operator and self.current:
            try:
                right = float(self.current)
            except ValueError:
                right = 0.0
            try:
                if self.operator == "+":
                    result = add(self.operand, right)
                elif self.operator == "-":
                    result = subtract(self.operand, right)
                elif self.operator == "*":
                    result = multiply(self.operand, right)
                elif self.operator == "/":
                    result = divide(self.operand, right)
                else:
                    result = right
            except Exception as e:
                result = "Error"
            self.current = str(result)
            self.display_value(self.current)
            self.operator = None
            self.operand = None

    def display_value(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, value)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
