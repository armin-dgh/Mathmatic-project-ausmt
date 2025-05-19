
# 🧮 Matrix Solver

A simple PyQt5-based desktop application for solving matrix problems such as:

- Gaussian Elimination
- Matrix Inversion
- Determinant Calculation
- Solving Systems of Linear Equations

## 🖥️ Features

- Solve linear systems using **Gaussian Elimination**
- Calculate **matrix determinant**
- Compute the **inverse of a matrix**
- Select between **Gauss** and **Gauss-Jordan** methods
- Simple and clean graphical interface (GUI)
- Useful help and documentation sections
- Dark mode style (custom QSS)

## 📸 Screenshot

![Screenshot](images/screenshot.png) <!-- Add your screenshot here -->

## 🧠 How It Works

- For solving systems of equations: input an `n x (n+1)` matrix
- For determinant and inverse: input a square `n x n` matrix
- The selected method (Gauss or Gauss-Jordan) is applied to perform the calculations

## 📂 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/armin-dgh/matrix-solver.git
   cd matrix-solver
   ```

2. Install the required libraries:
   ```bash
   pip install PyQt5 numpy
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## 📄 Documentation

You can find useful notes inside the application under the **Help** and **Documentation** menus. It explains:

- How to format your matrix input
- How Gaussian Elimination works
- Limitations and requirements

## 👤 Author

Developed by **Armin Dehghan**  
[🔗 GitHub Profile](https://github.com/armin-dgh)

## 📜 License

This project is licensed under the MIT License.
