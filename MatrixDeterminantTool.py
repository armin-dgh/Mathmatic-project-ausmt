import numpy as np
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit

class MatrixDeterminantTool:
    def __init__(self, parent=None):
        self.parent = parent

    def gauss_determinant(self, A):
        A = A.copy().astype(float)
        n = A.shape[0]
        det = 1
        swap_count = 0

        for i in range(n):
            if A[i][i] == 0:
                for j in range(i + 1, n):
                    if A[j][i] != 0:
                        A[[i, j]] = A[[j, i]]
                        swap_count += 1
                        break
                else:
                    return 0  # یک ستون کامل صفر است، دترمینان صفر می‌شود

            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                A[j] = A[j] - factor * A[i]

        for i in range(n):
            det *= A[i][i]

        if swap_count % 2 == 1:
            det *= -1

        return det

    def show_determinant_dialog(self, matrix, determinant):
        dialog = QDialog(self.parent)
        dialog.setWindowTitle("Determinant Result")
        dialog.resize(400, 200)

        layout = QVBoxLayout()
        text = QTextEdit()
        text.setReadOnly(True)

        formatted = "Input Matrix:\n"
        for row in matrix:
            formatted += "  ".join(f"{x:.2f}" for x in row) + "\n"

        formatted += f"\n✅ Determinant: {determinant:.4f}"

        if np.isclose(determinant, 0):
            formatted += "\n⚠️ Matrix is singular (det = 0) → No inverse."
        else:
            formatted += "\n✔️ Matrix is non-singular (has an inverse)."

        text.setText(formatted)
        layout.addWidget(text)
        dialog.setLayout(layout)
        dialog.exec_()
