# 🧮 Python Calculator 

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Statistics](https://img.shields.io/badge/Statistics-Module-green?logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

This project implements a **fully functional command-line calculator** built in Python. It supports both **basic arithmetic operations** and **statistical computations**, demonstrating core Python programming concepts such as user input, type casting, functions, loops, and use of the built-in `statistics` module.

---

## 🎯 Objectives

- Accept and process **user input** via the terminal
- Apply **type casting** to convert string inputs into numeric types
- Implement all standard **arithmetic operations** (`+`, `-`, `*`, `/`, `%`)
- Perform **statistical calculations** (Mean, Median, Mode, Average)
- Handle **edge cases** like division by zero and invalid input gracefully
- Practice Python fundamentals through a real, interactive project

---

## ⚙️ Features

| Feature | Description |
|---|---|
| ➕ Addition | Sum of two numbers |
| ➖ Subtraction | Difference of two numbers |
| ✖️ Multiplication | Product of two numbers |
| ➗ Division | Quotient of two numbers |
| **%** Modulus | Remainder of division |
| 📊 Mean | Average of a list of numbers |
| 📊 Median | Middle value of a sorted list |
| 📊 Mode | Most frequently occurring value(s) |
| 📊 Average | Alias for Mean |

---

## 🛠️ Tech Stack

- **Python 3.x**
- **`statistics`** module — for Mean, Median, Mode calculations
- **No external libraries required**

---

## 📋 Project Workflow

### Step 1 — Display Menu
A numbered menu is printed to the terminal listing all available operations (0–9).

### Step 2 — Take User Input
The user selects an operation by entering a number. Input is read as a string using `input()`.

### Step 3 — Type Casting
All numeric inputs are cast from `str → float` using `float()`, enabling decimal support for all operations.

### Step 4 — Perform Operation
Based on the user's choice, the corresponding function is called:
- **Basic ops** take two numbers
- **Statistical ops** take a space-separated list of numbers

### Step 5 — Display Result
The result is printed in a clean, readable format.

### Step 6 — Loop / Exit
The calculator loops back to the menu until the user selects `0` to exit.

---

## 🐍 Python Concepts Practiced

| Concept | Usage |
|---|---|
| `input()` | Capturing all user input from the terminal |
| **Type Casting** | `float(input(...))`, `list(map(float, ...))` |
| `while` loop | Keeps calculator running until exit |
| `if / elif / else` | Branching logic for menu choices |
| **Functions** | Modular functions for input, menu, and operations |
| **Error Handling** | `try / except ValueError` for invalid inputs |
| `statistics` module | `mean()`, `median()`, `mode()`, `multimode()` |
| **f-strings** | Clean result formatting |

---

## 🔍 Key Highlights

- All inputs are captured as strings and **explicitly cast** to `float`, making the concept of type casting central to the project
- The **modulus (`%`)** operation is included as both an arithmetic and practical concept
- `multimode()` is used instead of `mode()` to correctly handle datasets with **multiple modes or no mode**
- Division and modulus by zero are caught and reported with a user-friendly error message
- Invalid non-numeric input triggers a `ValueError` which is caught and handled cleanly

---

## 🚀 Getting Started

### Prerequisites

No external packages needed — uses Python's standard library only.

```bash
python --version   # Ensure Python 3.x is installed
```

### Run the Calculator

1. Clone this repository:
   ```bash
   git clone https://github.com/programmer-akash/your-repo-name.git
   ```

2. Navigate into the project folder:
   ```bash
   cd your-repo-name
   ```

3. Run the script:
   ```bash
   python calculator.py
   ```

---

## 🖥️ Sample Output
<img width="320" height="376" alt="image" src="https://github.com/user-attachments/assets/1ffb5261-51a6-444b-8066-089f872e4030" />


<img width="411" height="445" alt="image" src="https://github.com/user-attachments/assets/4e94792f-9af6-4d79-8a17-4c40d2672262" />

---

## 📁 Repository Structure

```
📦 Mini Project
 ┣ 🐍 calculator.py    # Main calculator script
 ┗ 📄 README.md        # Project documentation
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

**BUBAI DE**
- GitHub: [@Developer-Bubai](https://github.com/Developer-Bubai)
- LinkedIn: [Developer-Bubai](www.linkedin.com/in/bubai-de-0599093b1)

---

> *"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."* — Martin Fowler
