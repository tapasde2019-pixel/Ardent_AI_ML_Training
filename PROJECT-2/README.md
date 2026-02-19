# 🧮 Mini Projects — Python & Machine Learning

> A collection of beginner-to-intermediate Python projects covering core programming concepts and machine learning fundamentals.

---

## 📁 Project Structure

```
Mini Project/
│
├── calculator.py                  # Project 1: Advanced Python Calculator
├── Project_2__HPR_.ipynb          # Project 2: House Price Prediction
└── house_price_prediction.csv     # Output: Model prediction results
```

---

## 🔢 Project 1 — Advanced Calculator

### Overview
A terminal-based calculator built with Python that supports arithmetic operations, statistical functions, and percentage calculations — all through user input with proper type casting.

### Features

| Feature | Description |
|--------|-------------|
| ➕ Addition | Adds two numbers |
| ➖ Subtraction | Subtracts two numbers |
| ✖️ Multiplication | Multiplies two numbers |
| ➗ Division | Divides two numbers (with zero-division check) |
| 📊 Average | Calculates the mean of a list of numbers |
| 📈 Median | Finds the middle value of a dataset |
| 🔁 Mode | Finds the most frequent value(s) |
| 💯 Percentage | Calculates X% of a given value |

### How to Run

```bash
python calculator.py
```

### Sample Interaction

```
===== Advanced Calculator =====
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Percentage (%)
6. Average
7. Median
8. Mode
9. Exit

Enter your choice (1-9): 3
Enter first number: 10
Enter second number: 5
Result: 50.0
```

### Key Concepts Used
- **User Input** — `input()` function for interactive prompts
- **Type Casting** — `float()` to convert string input to numbers
- **Python `statistics` module** — for median and mode
- **Control Flow** — `while` loop + `if/elif/else` for menu navigation
- **Error Handling** — handles no-unique-mode case gracefully

---

## 🏠 Project 2 — House Price Prediction (Linear Regression)

### Overview
A machine learning project that trains a **Linear Regression** model to predict house prices using the **California Housing Dataset** from `scikit-learn`. No external data download required.

### Tech Stack

| Library | Purpose |
|--------|---------|
| `NumPy` | Numerical computations |
| `Pandas` | Data manipulation & analysis |
| `Matplotlib` | Data visualization |
| `Scikit-Learn` | ML model, dataset, metrics |

### Dataset — California Housing

Built directly into `sklearn` — no download needed!

| Feature | Description |
|--------|-------------|
| `MedInc` | Median income in block group |
| `HouseAge` | Median house age |
| `AveRooms` | Average number of rooms |
| `AveBedrms` | Average number of bedrooms |
| `Population` | Block group population |
| `AveOccup` | Average house occupancy |
| `Latitude` | Block group latitude |
| `Longitude` | Block group longitude |
| `Price` *(target)* | Median house value (in $100,000s) |

- **Total Records:** 20,640
- **Features:** 8
- **Missing Values:** None ✅

### Workflow — Step by Step

```
Step 1  → Import Libraries
Step 2  → Load Dataset (fetch_california_housing)
Step 3  → Data Understanding (shape, info, describe)
Step 4  → Check Missing Values
Step 5  → Select Features (X) and Target (y)
Step 6  → Train-Test Split (80% train / 20% test)
Step 7  → Train Linear Regression Model
Step 8  → Make Predictions
Step 9  → Evaluate Model (RMSE + R²)
Step 10 → Visualization: Actual vs Predicted
Step 11 → Residual Plot (Error Analysis)
Step 12 → Feature Importance (Coefficients)
Step 13 → Improvement via Log Transform (Feature Engineering)
Step 14 → Save Predictions to CSV
```

### Model Results

| Metric | Baseline Model | After Log Transform |
|--------|---------------|---------------------|
| RMSE | 0.7456 | 0.2244 |
| R² Score | 0.5758 | 0.6006 |

> **RMSE** (Root Mean Square Error) — Lower is better  
> **R²** (R-Squared Score) — Closer to 1.0 is better

### Feature Importance (Coefficients)

| Feature | Coefficient | Impact |
|---------|------------|--------|
| AveBedrms | +0.783 | ⬆️ Increases price |
| MedInc | +0.449 | ⬆️ Increases price |
| HouseAge | +0.010 | ⬆️ Increases price |
| Population | -0.000002 | ⬇️ Decreases price |
| AveOccup | -0.004 | ⬇️ Decreases price |
| AveRooms | -0.123 | ⬇️ Decreases price |
| Latitude | -0.420 | ⬇️ Decreases price |
| Longitude | -0.434 | ⬇️ Decreases price |

### How to Run

Open in **Google Colab** or any Jupyter-compatible environment:

```bash
jupyter notebook Project_2__HPR_.ipynb
```

Or open directly in Google Colab:
> Upload the `.ipynb` file → Runtime → Run All

### Output
Predictions are saved to:
```
house_price_prediction.csv
```

---

## 🛠️ Requirements

```bash
pip install numpy pandas matplotlib scikit-learn
```

---

## 📌 Notes

- Project 1 was built using **Claude AI** as an AI coding assistant
- Project 2 uses the **California Housing dataset** available directly inside `sklearn` — no external dataset needed
- The notebook was developed and tested on **Google Colab**

---

## 👤 Author

> **BUBAI DE**
> GitHub: [@My-username](https://github.com/Developer-Bubai)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
