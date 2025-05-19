from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMenuBar, QAction, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QWidget

class DocumentationWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Documentation")
        self.setMinimumSize(600, 500)

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)

        content_widget = QWidget()
        scroll.setWidget(content_widget)

        layout = QVBoxLayout(content_widget)
        layout.setSpacing(15)

        doc_text = """
            <h2>Matrix Solver - Full Documentation</h2>

            <p>This application provides numerical tools to perform matrix-based operations, including:</p>

            <ul>
                <li>Computing the <b>determinant</b> of a square matrix</li>
                <li>Finding the <b>inverse</b> of a matrix using Gauss-Jordan elimination</li>
                <li>Solving <b>linear systems</b> using Gaussian elimination with back-substitution</li>
            </ul>

            <h3>📌 Input Matrix Guidelines:</h3>
            <ul>
                <li><b>Determinant:</b> Requires a square matrix (n x n). If the matrix is not square, determinant is undefined.</li>
                <li><b>Inverse:</b> Input must be a square matrix. Singular matrices (det = 0) have no inverse.</li>
                <li><b>Solving Equations:</b> Requires an <b>augmented matrix</b> of size (n x n+1), where the last column represents the constants from the right-hand side of the equations.</li>
            </ul>

            <h3>🔍 How the Methods Work</h3>

            <h4>1. Gaussian Elimination</h4>
            <p>Transforms the matrix into an upper-triangular form using row operations, and then solves for variables using <b>back-substitution</b>.</p>
            <p><i>Used in: Determinant, Solving systems</i></p>

            <h4>2. Gauss-Jordan Elimination</h4>
            <p>Extends Gaussian elimination to fully reduce the matrix to the identity form. This method uses forward and backward elimination to find the inverse matrix.</p>
            <p><i>Used in: Matrix Inverse</i></p>

            <h3>🧮 Example: Solving a System</h3>
            <p>System of equations:</p>
            <pre>
            2x - y +  z = 3
            x + 3y + 2z = 7
                -2y + z = 4
            </pre>
            <p>Corresponding augmented matrix (3x4):</p>
            <pre>
            [[2, -1, 1, 3],
            [1,  3, 2, 7],
            [0, -2, 1, 4]]
            </pre>

            <h3>📘 Example: Matrix Inversion</h3>
            <p>Matrix:</p>
            <pre>
            [[1, 2],
            [3, 4]]
            </pre>
            <p>Result (inverse):</p>
            <pre>
            [[-2.0, 1.0],
            [1.5, -0.5]]
            </pre>

            <h3>📏 Determinant Example</h3>
            <p>Matrix:</p>
            <pre>
            [[2, -1, 0],
            [1,  3, 4],
            [0, -2, 5]]
            </pre>
            <p>Determinant (using Gaussian elimination): <b>det = 40</b></p>

            <h3>⚠️ Numerical Considerations</h3>
            <ul>
                <li>Row swapping is applied automatically to avoid division by zero (pivoting).</li>
                <li>Floating-point precision can affect accuracy in large or ill-conditioned matrices.</li>
                <li>Results are rounded to a few decimal places for display clarity.</li>
            </ul>

            <h3>🎓 Educational Value</h3>
            <p>This application is suitable for students learning linear algebra, numerical analysis, or working on engineering/math problems. It emphasizes step-by-step transformations similar to textbook algorithms.</p>

            <h3>📚 References</h3>
            <ul>
                <li>Introduction to Linear Algebra – Gilbert Strang</li>
                <li>Numerical Linear Algebra – Trefethen and Bau</li>
                <li>MIT OpenCourseWare – Linear Algebra (Video Lectures)</li>
            </ul>

            <h3>✅ Tips for Use</h3>
            <ul>
                <li>Always double-check matrix dimensions before solving.</li>
                <li>If a matrix has no solution or is singular, an appropriate error will be shown.</li>
                <li>You can copy-paste matrix values from a CSV or spreadsheet.</li>
            </ul>

            <p>Enjoy learning and exploring matrix operations!</p>
            """


        label = QLabel()
        label.setText(doc_text)
        label.setWordWrap(True)
        label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)


        layout.addWidget(label)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

class CustomToolBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.menu_bar = QMenuBar()

         
        self.menu_bar.setStyleSheet("""
            QMenuBar {
                background-color: #cdc6c5;
                color: black;
            }
            QMenuBar::item {
                background: transparent;
                padding: 6px 12px;
                spacing: 3px;
            }
            QMenuBar::item:selected {
                background: #444444;
            }
            QMenu {
                background-color: black;
                color: white;
                border: 1px solid #222;
            }
            QMenu::item:selected {
                background-color: #555555;
            }
        """)

         
        file_menu = self.menu_bar.addMenu("File")
        edit_menu = self.menu_bar.addMenu("Edit")
        view_menu = self.menu_bar.addMenu("View")
        help_menu = self.menu_bar.addMenu("Help")
        about_menu = self.menu_bar.addMenu("About")

         
        # file_menu.addAction(QAction("New", self))
        # file_menu.addAction(QAction("Open", self))
        # file_menu.addAction(QAction("Save", self))
        # file_menu.addSeparator()
        # file_menu.addAction(QAction("Exit", self))

        # edit_menu.addAction(QAction("Undo", self))
        # edit_menu.addAction(QAction("Redo", self))
        # edit_menu.addSeparator()
        # edit_menu.addAction(QAction("Cut", self))
        # edit_menu.addAction(QAction("Copy", self))
        # edit_menu.addAction(QAction("Paste", self))

        # view_menu.addAction(QAction("Zoom In", self))
        # view_menu.addAction(QAction("Zoom Out", self))
        # view_menu.addAction(QAction("Reset Zoom", self))

        help_menu.addAction(QAction("Documentation", self, triggered=self.show_documentation_window))
        help_menu.addAction(QAction("Support", self, triggered=self.show_support))
        

        about_menu.addAction(QAction("About This App", self, triggered=self.show_about))
        about_menu.addAction(QAction("Version Info", self ,triggered=self.show_version_info))

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.addWidget(self.menu_bar)
        self.setLayout(layout)
    def show_support(self):
        QMessageBox.information(self, "Help",
            "Usage Tips:\n\n"
            "1. Determinant:\n"
            "- Only for square matrices.\n"
            "- Gauss elimination transforms the matrix into an upper triangular form.\n"
            "- The determinant is the product of the diagonal elements.\n"
            "- Row swapping changes the sign of the determinant.\n\n"
            "2. Matrix Inversion:\n"
            "- Only for square, non-singular matrices (det ≠ 0).\n"
            "- Uses Gauss-Jordan elimination.\n"
            "- Combine the matrix with an identity matrix and reduce the original matrix to identity form.\n"
            "- The transformed identity matrix becomes the inverse.\n\n"
            "3. Solving Linear Systems:\n"
            "- Input must be an augmented matrix [A|b] with one extra column for constants.\n"
            "- For 'n' variables, the matrix must have 'n' rows and 'n+1' columns.\n"
            "- Gauss elimination is applied to create zeros below the diagonal.\n"
            "- Then back-substitution is used to find variable values.\n\n"
            "Note:\n"
            "- Ensure you input valid numeric entries.\n"
            "- Avoid zero pivots when possible (row swapping can help).")
    def show_about(self):
            QMessageBox.information(self, "About This App",
                "This application is designed to perform matrix operations:\n"
                "- Calculate the determinant of a matrix\n"
                "- Solve systems of linear equations using Gauss or Gauss-Jordan elimination\n"
                "- Compute the inverse of a matrix\n\n"
                "You can input a matrix and select the desired operation to perform.")
    def show_documentation_window(self):
            doc_win = DocumentationWindow(self)
            doc_win.exec_()
    def show_version_info(self):
        version_text = (
            "<h3>Matrix Solver Application</h3>"
            "<p><b>Version:</b> 1.0.0</p>"
            "<p><b>Author:</b> Armin Dehghan</p>"
            "<p><b>GitHub:</b> "
            "<a href='https://github.com/armin-dgh'>https://github.com/armin-dgh</a></p>"
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Version Info")
        msg.setTextFormat(Qt.RichText)
        msg.setTextInteractionFlags(Qt.TextBrowserInteraction)
        msg.setText(version_text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()




