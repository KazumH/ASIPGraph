"""
Reference: http://zetcode.com/gui/pyqt5/firstprograms/
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == "__main__":

    sample = QApplication(sys.argv) #PyQtのアプリなら必ず入れる。sys.argvはコマンドライン引数のリスト

    w = QWidget() #全UIオブジェクトのベース
    w.resize(500, 600) #サイズ
    w.move(100, 200) #ディスプレイ左上から何ピクセルずらすか
    w.setWindowTitle("Sample(July 10, 2016)")

    w.show()

    sys.exit(sample.exec_()) #アンダースコアはPythonの組み込み関数と区別するため





