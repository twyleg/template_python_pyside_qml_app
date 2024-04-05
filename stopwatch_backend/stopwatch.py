# Copyright (C) 2024 twyleg
import sys
import time
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QTimer

from stopwatch_model import Model


FILE_PATH = Path(__file__).parent


class Stopwatch:

    def __init__(self) -> None:
        self.start_timestamp_ns = time.time_ns()
        self.diff = 0
        self.stopwatch_model = Model()

        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()

        self.engine.rootContext().setContextProperty("stopwatch_model", self.stopwatch_model)
        self.engine.load(FILE_PATH / "frontend/qml/main.qml")

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_callback)
        self.timer.start()

    def run(self) -> None:
        if not self.engine.rootObjects():
            sys.exit(-1)
        sys.exit(self.app.exec())

    def timer_callback(self) -> None:
        self.stopwatch_model.update_timers()


