import numpy as np
from PyQt5.QtWidgets import QVBoxLayout, QDialog, QTextEdit


class GaussJordanSolver:
    def __init__(self, A_aug):
        self.A_aug = A_aug.astype(float)
        self.m, self.n_aug = self.A_aug.shape
        self.n = self.n_aug - 1  # تعداد متغیرها

    def make_swap_matrix(self, i, j):
        E = np.eye(self.m)
        E[[i, j]] = E[[j, i]]
        return E

    def make_scale_matrix(self, i, scalar):
        E = np.eye(self.m)
        E[i][i] = scalar
        return E

    def make_add_multiple_matrix(self, src, dest, scalar):
        E = np.eye(self.m)
        E[dest][src] = scalar
        return E

    def eliminate(self):
        for i in range(min(self.m, self.n)):
            # Pivoting
            if self.A_aug[i][i] == 0:
                for j in range(i + 1, self.m):
                    if self.A_aug[j][i] != 0:
                        E = self.make_swap_matrix(i, j)
                        self.A_aug = E @ self.A_aug
                        break

            pivot = self.A_aug[i][i]
            if pivot == 0:
                continue

            # Normalize pivot row
            E = self.make_scale_matrix(i, 1 / pivot)
            self.A_aug = E @ self.A_aug

            # Eliminate other entries in the column
            for j in range(self.m):
                if j != i and self.A_aug[j][i] != 0:
                    factor = -self.A_aug[j][i]
                    E = self.make_add_multiple_matrix(i, j, factor)
                    self.A_aug = E @ self.A_aug

        return self.A_aug

    def check_solution(self):
        # Check inconsistency
        for i in range(self.m):
            if np.allclose(self.A_aug[i, :-1], 0) and not np.isclose(self.A_aug[i, -1], 0):
                return "No solution"

        # Count pivot rows
        rank = 0
        for i in range(self.m):
            if not np.allclose(self.A_aug[i, :-1], 0):
                rank += 1

        if rank < self.n:
            return "Infinite solutions"
        else:
            return "Unique solution"

    def get_solution(self):
        return self.A_aug[:, -1]

  
    def show_result_dialog(self, parent=None):
        dialog = QDialog(parent)
        dialog.setWindowTitle("Gauss-Jordan Result")
        dialog.resize(500, 300)

        layout = QVBoxLayout()
        text = QTextEdit()
        text.setReadOnly(True)

        formatted = "📌 Matrix after Gauss-Jordan elimination (RREF):\n"
        for row in self.A_aug:
            formatted += "  ".join(f"{x:.2f}" for x in row) + "\n"

        sol_type = self.check_solution()

        formatted += "\n📋 Solution Type:\n"
        if sol_type == "No solution":
            formatted += "❌ The system has no solution.\n"
        elif sol_type == "Infinite solutions":
            formatted += "♾️ The system has infinitely many solutions.\n"
        else:
            formatted += "✅ Unique solution:\n"
            solution = self.get_solution()
            for idx, val in enumerate(solution):
                formatted += f"   x{idx + 1} = {val:.4f}\n"

        text.setText(formatted)
        layout.addWidget(text)
        dialog.setLayout(layout)
        dialog.exec_()
