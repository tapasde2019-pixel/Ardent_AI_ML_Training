#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║              S U P E R C A L C  v1.0                ║
║   Arithmetic · Type Casting · Statistics · More      ║
╚══════════════════════════════════════════════════════╝
"""

from collections import Counter


# ─────────────────────────────────────────────
#  DISPLAY HELPERS
# ─────────────────────────────────────────────

def banner():
    print("""
╔══════════════════════════════════════════════════════╗
║              S U P E R C A L C  v1.0                ║
║   Arithmetic · Type Casting · Statistics · More      ║
╚══════════════════════════════════════════════════════╝
""")

def divider(title=""):
    if title:
        pad = (50 - len(title) - 2) // 2
        print(f"\n{'─' * pad} {title} {'─' * pad}")
    else:
        print("─" * 52)

def menu():
    print("""
  ┌─────────────────────────────────────────────┐
  │  MODES                                      │
  │  [1] Standard Calculator  (+ - * / %)       │
  │  [2] Statistics           (mean/median/mode)│
  │  [3] Type Casting Demo                      │
  │  [4] Help & Examples                        │
  │  [0] Exit                                   │
  └─────────────────────────────────────────────┘""")


# ─────────────────────────────────────────────
#  TYPE CASTING
# ─────────────────────────────────────────────

def cast_value(value, target_type: str):
    """Cast a value to int, float, or str. Returns (result, type_name, success)."""
    try:
        if target_type == "int":
            result = int(float(value))          # e.g. "3.9" → 3
        elif target_type == "float":
            result = float(value)
        elif target_type == "str":
            result = str(value)
        else:
            return None, None, False
        return result, type(result).__name__, True
    except (ValueError, TypeError) as e:
        return None, None, False


def get_number(prompt: str, allow_float=True):
    """Prompt user for a number with type casting."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("  ⚠  Please enter a value.")
            continue

        # Let user specify a cast: e.g. "3.7 as int"
        if " as " in raw.lower():
            parts = raw.lower().split(" as ")
            val_str, ttype = parts[0].strip(), parts[1].strip()
            result, tname, ok = cast_value(val_str, ttype)
            if ok:
                print(f"  ✓  Cast: {repr(val_str)} → {tname}({result})")
                return float(result)
            else:
                print(f"  ✗  Cannot cast '{val_str}' to {ttype}. Try again.")
                continue

        # Auto parse
        try:
            if allow_float and '.' in raw:
                return float(raw)
            else:
                return int(raw)
        except ValueError:
            try:
                return float(raw)
            except ValueError:
                print(f"  ✗  '{raw}' is not a valid number. Try again.")


def get_numbers_list(prompt: str):
    """Prompt user for a comma/space separated list of numbers."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("  ⚠  Please enter at least one number.")
            continue
        parts = raw.replace(',', ' ').split()
        nums = []
        errors = []
        for p in parts:
            try:
                nums.append(float(p) if '.' in p else int(p))
            except ValueError:
                errors.append(p)
        if errors:
            print(f"  ✗  Skipped invalid values: {errors}")
        if nums:
            return nums
        print("  ✗  No valid numbers found. Try again.")


# ─────────────────────────────────────────────
#  ARITHMETIC
# ─────────────────────────────────────────────

def fmt(n):
    """Format number: show int if whole, else float."""
    if isinstance(n, float) and n.is_integer():
        return str(int(n))
    return f"{n:.10g}"


def standard_calculator():
    divider("STANDARD CALCULATOR")
    print("  Tip: You can type values like '3.9 as int' to cast before using.\n")

    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else None,
        '%': lambda a, b: a % b if b != 0 else None,
        '**': lambda a, b: a ** b,
        '//': lambda a, b: a // b if b != 0 else None,
    }

    history = []

    while True:
        print("\n  Operations: +  -  *  /  %  **  //  | [b]ack")
        a = get_number("  Enter first number  : ")

        op = input("  Enter operator      : ").strip()
        if op.lower() == 'b':
            break
        if op not in ops:
            print(f"  ✗  Unknown operator '{op}'. Supported: {list(ops.keys())}")
            continue

        b = get_number("  Enter second number : ")

        result = ops[op](a, b)

        if result is None:
            print("  ✗  Math error (e.g. division by zero).")
            continue

        # Determine result type
        if isinstance(a, int) and isinstance(b, int) and op not in ('/', '**'):
            result = int(result)

        expr = f"{fmt(a)} {op} {fmt(b)} = {fmt(result)}"
        rtype = type(result).__name__
        print(f"\n  ┌─ Result ──────────────────────────┐")
        print(f"  │  {expr}")
        print(f"  │  Type: {rtype}")
        print(f"  └───────────────────────────────────┘")

        history.append(expr)

        # Percentage helper
        if op in ('+', '-', '*', '/'):
            pct_ask = input("  Show as % of first number? [y/N]: ").strip().lower()
            if pct_ask == 'y' and a != 0:
                pct = (result / a) * 100
                print(f"  → Result is {fmt(pct)}% of {fmt(a)}")

        again = input("\n  Another calculation? [Y/n]: ").strip().lower()
        if again == 'n':
            break

    if history:
        divider("HISTORY")
        for i, h in enumerate(history, 1):
            print(f"  {i:>2}. {h}")


# ─────────────────────────────────────────────
#  STATISTICS
# ─────────────────────────────────────────────

def calc_mean(nums):
    return sum(nums) / len(nums)

def calc_median(nums):
    s = sorted(nums)
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    return s[mid]

def calc_mode(nums):
    freq = Counter(nums)
    max_freq = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_freq]
    if len(modes) == len(set(nums)):
        return None, max_freq   # No mode
    return modes, max_freq

def calc_percentage_of_total(nums):
    total = sum(nums)
    if total == 0:
        return [(n, 0.0) for n in nums]
    return [(n, (n / total) * 100) for n in nums]


def statistics_mode():
    divider("STATISTICS")
    print("  Enter numbers separated by commas or spaces.\n")

    nums = get_numbers_list("  Numbers: ")

    print(f"\n  Input  : {nums}")
    print(f"  Sorted : {sorted(nums)}")
    divider()

    n       = len(nums)
    total   = sum(nums)
    mean    = calc_mean(nums)
    median  = calc_median(nums)
    modes, freq = calc_mode(nums)
    minimum = min(nums)
    maximum = max(nums)
    rng     = maximum - minimum

    print(f"  Count   : {n}")
    print(f"  Sum     : {fmt(total)}")
    print(f"  Mean    : {fmt(mean)}")
    print(f"  Average : {fmt(mean)}   (same as mean)")
    print(f"  Median  : {fmt(median)}")

    if modes is None:
        print(f"  Mode    : No mode (all values appear {freq}x)")
    elif len(modes) == 1:
        print(f"  Mode    : {fmt(modes[0])}  (appears {freq}x)")
    else:
        print(f"  Mode    : {[fmt(m) for m in modes]}  (each appears {freq}x)")

    print(f"  Min     : {fmt(minimum)}")
    print(f"  Max     : {fmt(maximum)}")
    print(f"  Range   : {fmt(rng)}")

    divider("% OF TOTAL")
    pcts = calc_percentage_of_total(nums)
    for val, pct in pcts:
        bar = '█' * int(pct / 5)
        print(f"  {fmt(val):>10}  →  {pct:6.2f}%  {bar}")

    divider()
    print(f"  Type of inputs : {set(type(n).__name__ for n in nums)}")


# ─────────────────────────────────────────────
#  TYPE CASTING DEMO
# ─────────────────────────────────────────────

def type_casting_demo():
    divider("TYPE CASTING DEMO")
    print("  Cast any value to int, float, or str.\n")

    while True:
        raw = input("  Enter a value (or [b]ack): ").strip()
        if raw.lower() == 'b':
            break

        print()
        for ttype in ("int", "float", "str"):
            result, tname, ok = cast_value(raw, ttype)
            if ok:
                print(f"  → {ttype:5s} : {repr(result)}  (type: {tname})")
            else:
                print(f"  → {ttype:5s} : ✗ Cannot cast '{raw}' to {ttype}")

        # Show what Python sees
        print(f"\n  Original input type: {type(raw).__name__} → {repr(raw)}")
        print()


# ─────────────────────────────────────────────
#  HELP
# ─────────────────────────────────────────────

def show_help():
    divider("HELP & EXAMPLES")
    print("""
  STANDARD CALCULATOR
  ───────────────────
  Operator  │ Meaning          │ Example
  ──────────┼──────────────────┼─────────────────
  +         │ Addition         │ 10 + 5   = 15
  -         │ Subtraction      │ 10 - 5   = 5
  *         │ Multiplication   │ 10 * 5   = 50
  /         │ Division         │ 10 / 3   = 3.333...
  %         │ Modulus (remain) │ 10 % 3   = 1
  **        │ Power/Exponent   │ 2  ** 8  = 256
  //        │ Floor division   │ 10 // 3  = 3

  TYPE CASTING
  ────────────
  When entering a number, append "as int/float/str":
    e.g.  3.9 as int    → int(3) 
    e.g.  7   as float  → float(7.0)
    e.g.  42  as str    → str('42')

  STATISTICS
  ──────────
  Mean    = sum of all values / count
  Average = same as mean
  Median  = middle value when sorted
  Mode    = most frequently occurring value
  Range   = max − min
  % Total = (value / sum) × 100
""")
    input("  Press Enter to return to menu...")


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    banner()
    while True:
        menu()
        choice = input("\n  Your choice: ").strip()

        if choice == '1':
            standard_calculator()
        elif choice == '2':
            statistics_mode()
        elif choice == '3':
            type_casting_demo()
        elif choice == '4':
            show_help()
        elif choice == '0':
            print("\n  Goodbye! 👋\n")
            break
        else:
            print("  ✗  Invalid choice. Enter 0–4.")


if __name__ == "__main__":
    main()
    