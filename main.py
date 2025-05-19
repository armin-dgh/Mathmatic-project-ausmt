import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QSpinBox, QPushButton, QTableWidget, QTableWidgetItem,
    QDesktopWidget, QComboBox, QMessageBox
)
from PyQt5.QtGui import QIcon 
from ToolBar import CustomToolBar
from GaussJordanSolver import GaussJordanSolver
from MatrixInversionTool import MatrixInversionTool
from MatrixDeterminantTool import MatrixDeterminantTool
from PyQt5.QtCore import Qt
import numpy as np
import os
 



def load_stylesheet_from_file(file_path):
        with open(file_path, "r") as f:
            return f.read()
        
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matrix Solver")
        self.resize(600, 450)
        self.setWindowIcon(QIcon("images/matrix_logo_icon_169963.ico")) 
        self.center_window()
        self.setup_ui()
        self.setStyleSheet(load_stylesheet_from_file("style.qss"))
   
    def center_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setup_ui(self):
        layout = QVBoxLayout()

         
        self.toolbar = CustomToolBar(self)
        layout.addWidget(self.toolbar)

    
        input_layout = QHBoxLayout()
        self.row_input = QSpinBox()
        self.row_input.setRange(1, 20)
        self.row_input.setValue(3)

        self.col_input = QSpinBox()
        self.col_input.setRange(1, 20)
        self.col_input.setValue(3)

        input_layout.addWidget(QLabel("Rows:"))
        input_layout.addWidget(self.row_input)
        input_layout.addWidget(QLabel("Columns:"))
        input_layout.addWidget(self.col_input)

         
        self.create_button = QPushButton("Create Matrix")
        self.create_button.clicked.connect(self.create_matrix)

         
        self.table = QTableWidget()
        self.table.setMinimumSize(400, 200)

         
        self.operation_selector = QComboBox()
        self.operation_selector.addItems([
            "Select Operation",
            "Determinant (Gauss)",
            "Solve Problem (Gauss-Jordan)",
            "Inverse Matrix (Gauss)"
        ])

         
        self.solve_button = QPushButton("Solve")
        self.solve_button.clicked.connect(self.solve_matrix)
        self.solve_button.setFixedHeight(40)

         
        layout.addLayout(input_layout)
        layout.addWidget(self.create_button)
        layout.addWidget(self.table, stretch=1)
        layout.addWidget(self.operation_selector)
        layout.addWidget(self.solve_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def create_matrix(self):
        rows = self.row_input.value()
        cols = self.col_input.value()
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)

        for i in range(rows):
            for j in range(cols):
                self.table.setItem(i, j, QTableWidgetItem(""))

    def solve_matrix(self):
        operation = self.operation_selector.currentText()
        print(operation)

        try:
            matrix = []
            for i in range(self.table.rowCount()):
                row = []
                for j in range(self.table.columnCount()):
                    item = self.table.item(i, j)
                    value = float(item.text()) if item and item.text() else 0
                    row.append(value)
                matrix.append(row)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "All matrix entries must be numeric.")
            return

        matrix = np.array(matrix, dtype=float)

        if operation == "Solve Problem (Gauss-Jordan)":
            rows, cols = matrix.shape
            if cols == rows + 1:
                    solver = GaussJordanSolver(matrix)
                    solver.eliminate()
                    solver.show_result_dialog(self) 
            else:
                QMessageBox.warning(self, "Invalid Matrix", "For solving equations, matrix must be augmented (cols = rows + 1).")
            
             
        elif operation == "Determinant (Gauss)":
            rows, cols = matrix.shape[0], matrix.shape[1]
            if rows != cols:
                QMessageBox.warning(self, "Invalid Input", "Determinant can only be calculated for square matrices.")
                return
            tool = MatrixDeterminantTool(parent=self)
            A = np.array(matrix)
            det = tool.gauss_determinant(A)
            tool.show_determinant_dialog(A, det)
        elif operation == "Inverse Matrix (Gauss)":
            rows, cols = matrix.shape
            if rows != cols:
                QMessageBox.warning(self, "Invalid Input", "Inverse can only be calculated for square matrices.")
                return
            A = np.array(matrix)
            tool = MatrixInversionTool(parent=self)
            A_inv = tool.gauss_jordan_inverse(A)


            if A_inv is None:
                QMessageBox.warning(self, "No Inverse", "Matrix is singular and has no inverse.")
                return

            tool.show_inverse_dialog(A, A_inv)


        else:
            QMessageBox.information(self, "Coming Soon", f"{operation} will be implemented next.")
 

    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
