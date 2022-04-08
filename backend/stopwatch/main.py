# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QTimer

from stopwatch.time import Time




if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    time = Time(0)

    engine.rootContext().setContextProperty("time", time)
    engine.load(os.fspath(Path(__file__).resolve().parent / "../../frontend/qml/main.qml"))


    def timer_callback():
        time.millis = time.millis + 1

    timer = QTimer()
    timer.timeout.connect(timer_callback)
    timer.start(100)

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
