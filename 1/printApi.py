import sys
from PyQt5.QtWidgets import QWidget

out = sys.stdout
sys.stdout = open(r"./QWidget.txt", "w")
help(QWidget)
sys.stdout.close()
sys.stdout = out