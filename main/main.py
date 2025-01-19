import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# Classe principal da janela
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Primeira Janela")
        self.setGeometry(100, 100, 600, 400)  # Posição (x, y) e tamanho (largura, altura)

# Inicialização da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
