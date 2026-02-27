"""Graphical calculator interface using Tkinter.

Layout and behavior are modeled loosely after the iPhone calculator.
"""

try:
    import tkinter as tk
except ImportError as e:
    raise ImportError(
        "Tkinter is not available. Make sure you are running a Python build with GUI support "
        "(e.g. use Python 3.12 installed from python.org or via Homebrew with --with-tcl-tk)."
    ) from e

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    negate,
    percent,
    sin,
    cos,
    tan,
    log,
    exp,
    sqrt,
    pi,
)
import math


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

        # scientific buttons (initially hidden)
        self.sci_mode = False
        self.sci_buttons = []
        sci_specs = [
            ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("log", 6, 3),
            ("sqrt", 7, 0), ("exp", 7, 1), ("pi", 7, 2),
        ]
        for text, row, col in sci_specs:
            btn = tk.Button(master, text=text, font=("Arial", 18), command=lambda t=text: self._on_button(t))
            self.sci_buttons.append(btn)
            btn.grid(row=row, column=col, sticky="nsew")
        # hide them initially
        for btn in self.sci_buttons:
            btn.grid_remove()

        # menu for mode switching
        menubar = tk.Menu(master)
        mode_menu = tk.Menu(menubar, tearoff=0)
        mode_menu.add_command(label="Basic", command=self._set_basic)
        mode_menu.add_command(label="Scientific", command=self._toggle_sci)
        mode_menu.add_command(label="Programmer", command=self._toggle_prog)
        menubar.add_cascade(label="Mode", menu=mode_menu)
        master.config(menu=menubar)

        # programmer buttons
        self.prog_mode = False
        self.prog_buttons = []
        prog_specs = [
            ("AND", 8, 0), ("OR", 8, 1), ("XOR", 8, 2), ("NOT", 8, 3),
            ("LSH", 9, 0), ("RSH", 9, 1), ("BIN", 9, 2), ("HEX", 9, 3), ("DEC", 9, 4),
        ]
        for text, row, col in prog_specs:
            btn = tk.Button(master, text=text, font=("Arial", 14), command=lambda t=text: self._on_button(t))
            self.prog_buttons.append((btn, row, col))
            # place some beyond grid if necessary
            try:
                btn.grid(row=row, column=col, sticky="nsew")
            except Exception:
                btn.grid(row=row, column=col, sticky="nsew")
        for btn, _, _ in self.prog_buttons:
            btn.grid_remove()

        # programmer display base
        self.prog_base = "DEC"  # DEC, BIN, HEX

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
        elif label in ("sin", "cos", "tan", "log", "sqrt", "exp", "pi"):
            self._sci_operation(label)
        elif label in ("AND", "OR", "XOR", "NOT", "LSH", "RSH", "BIN", "HEX", "DEC"):
            self._prog_operation(label)
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

    def _sci_operation(self, op):
        # unary scientific operations - operate on current value immediately
        try:
            value = float(self.current) if self.current else 0.0
        except ValueError:
            value = 0.0
        try:
            if op == "sin":
                result = sin(value)
            elif op == "cos":
                result = cos(value)
            elif op == "tan":
                result = tan(value)
            elif op == "log":
                result = log(value)
            elif op == "sqrt":
                result = sqrt(value)
            elif op == "exp":
                result = exp(value)
            elif op == "pi":
                result = pi()
            else:
                result = value
        except Exception:
            result = "Error"
        self.current = str(result)
        self.display_value(self.current)

    def _toggle_sci(self):
        self.sci_mode = not self.sci_mode
        for btn in self.sci_buttons:
            if self.sci_mode:
                btn.grid()
            else:
                btn.grid_remove()

    def _set_basic(self):
        self.sci_mode = False
        for btn in self.sci_buttons:
            btn.grid_remove()

    def _toggle_prog(self):
        # turn off scientific UI when enabling programmer
        self._set_basic()
        self.prog_mode = not self.prog_mode
        for btn, _, _ in self.prog_buttons:
            if self.prog_mode:
                btn.grid()
            else:
                btn.grid_remove()

    def _parse_current_int(self):
        s = self.current if self.current else self.display.get()
        if not s:
            return 0
        try:
            if self.prog_base == "BIN":
                return int(str(s), 2)
            elif self.prog_base == "HEX":
                return int(str(s), 16)
            else:
                return int(float(s))
        except Exception:
            return 0

    def _display_int(self, value):
        if self.prog_base == "BIN":
            self.display_value(to_bin(value))
        elif self.prog_base == "HEX":
            self.display_value(to_hex(value))
        else:
            self.display_value(str(int(value)))

    def _prog_operation(self, op):
        # handle base switch
        if op in ("BIN", "HEX", "DEC"):
            self.prog_base = op
            # refresh display
            try:
                val = self._parse_current_int()
                self._display_int(val)
            except Exception:
                pass
            return

        if op == "NOT":
            val = self._parse_current_int()
            res = bit_not(val, bits=32)
            self.current = str(res)
            self._display_int(res)
            return

        # binary ops consume operand and current
        if self.operator and self.current:
            a = int(self.operand)
            b = self._parse_current_int()
        else:
            # if no pending operator, use current as a and wait for next
            self.operand = self._parse_current_int()
            self.operator = op
            self.current = ""
            self.display.delete(0, tk.END)
            return

        try:
            if op == "AND":
                res = bit_and(a, b)
            elif op == "OR":
                res = bit_or(a, b)
            elif op == "XOR":
                res = bit_xor(a, b)
            elif op == "LSH":
                res = lshift(a, b)
            elif op == "RSH":
                res = rshift(a, b)
            else:
                res = b
        except Exception:
            res = "Error"

        self.current = str(res)
        self._display_int(res)
        self.operator = None
        self.operand = None

    def display_value(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, value)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
