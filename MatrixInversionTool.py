import numpy as np
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit

class MatrixInversionTool:
    def __init__(self, parent=None):
        self.parent = parent  # می‌توانید QMainWindow یا QWidget را پاس دهید

    def gauss_jordan_inverse(self, A):
        n = A.shape[0]
        A = A.astype(float)
        I = np.eye(n)
        AI = np.hstack([A, I])   

        for i in range(n):
            if AI[i][i] == 0:
                for j in range(i + 1, n):
                    if AI[j][i] != 0:
                        AI[[i, j]] = AI[[j, i]]
                        break

            pivot = AI[i][i]
            if pivot == 0:
                return None  # ماتریس منفرد است و وارون ندارد

            AI[i] = AI[i] / pivot

            for j in range(n):
                if j != i:
                    AI[j] = AI[j] - AI[j][i] * AI[i]

        A_inv = AI[:, n:]
        return A_inv

    def show_inverse_dialog(self, A, A_inv):
        dialog = QDialog(self.parent)
        dialog.setWindowTitle("Inverse Matrix (Gauss-Jordan)")
        dialog.resize(500, 400)

        layout = QVBoxLayout()
        text = QTextEdit()
        text.setReadOnly(True)

        result = "Original Matrix (A):\n"
        for row in A:
            result += "  ".join(f"{x:.2f}" for x in row) + "\n"

        result += "\nInverse Matrix (A⁻¹):\n"
        if A_inv is None:
            result += "❌ Matrix is singular and has no inverse.\n"
        else:
            for row in A_inv:
                result += "  ".join(f"{x:.4f}" for x in row) + "\n"

        text.setText(result)
        layout.addWidget(text)
        dialog.setLayout(layout)
        dialog.exec_()
