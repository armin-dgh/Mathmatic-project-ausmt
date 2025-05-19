# Matrix Solver Qt App

A GUI-based matrix calculator built with Python and PyQt5 that allows users to perform various matrix operations such as:

- Determinant Calculation (using Gauss method)
- Matrix Inversion
- Solving Linear Systems using Gauss or Gauss-Jordan elimination
- Analyzing the system's solution (unique, infinite, or no solution)

## Features

- 🧮 Intuitive matrix input through a user-friendly GUI  
- 📐 Supports square and augmented matrices  
- 🔄 Performs operations step-by-step using matrix transformation techniques  
- 📊 Displays detailed results in formatted dialogs  
- 🚫 Handles edge cases such as singular matrices or inconsistent systems  

## Technologies Used

- Python 3
- PyQt5
- NumPy

## How to Run

1. Clone this repository or download the code.
2. Install dependencies:

```bash
pip install PyQt5 numpy
```

3. Run the main file:

```bash
python matrix.py
```

## Screenshots

You can add screenshots by placing image files in your project directory and using this markdown syntax:

```markdown
![Screenshot Description](images/screenshot1.png)
```

For example, create a folder named `images` in your project root, put your screenshots there, and reference them like:

```markdown
![Main Window](images/main_window.png)
```

## Future Improvements

- Add support for complex numbers
- Visualize transformation matrices
- Export results to LaTeX or CSV

## License

This project is open-source and free to use under the MIT License.
