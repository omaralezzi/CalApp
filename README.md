# Python Calculator App

A simple command-line calculator implemented in Python. Supports addition, subtraction, multiplication, and division.

## Usage

```
python main.py
```

Enter expressions like `3 + 4` or `10 / 2`. Type `quit` to exit.

## GUI Mode

A graphical interface resembling an iPhone calculator is available using Tkinter.

> ⚠️ **Python/Tkinter requirement**
>
> The GUI requires a Python build that includes the `_tkinter` module. On macOS,
> the system Python or some Homebrew installations (e.g. Python 3.13) may lack
> this support. Use Python 3.12 or another install with `tcl-tk` enabled. For
> example, you can install via Homebrew with:
>
> ```bash
> brew install python@3.12 --with-tcl-tk
> ```
>
> or download the macOS installer from https://python.org which bundles Tk.
>
> After installing, make sure your `python` command points to the 3.12 interpreter.

```
python gui.py
```

Click buttons or use the onscreen keys to perform calculations. The GUI supports clear, sign toggle, percent, and basic arithmetic.
