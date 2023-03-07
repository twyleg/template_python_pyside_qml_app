""""
Copyright (C) 2022 twyleg
"""
import os
import sys
import time
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QTimer

from stopwatch_model import Model, State


class Stopwatch:

    def __init__(self) -> None:
        self.start_timestamp_ns = time.time_ns()
        self.diff = 0
        self.stopwatch_model = Model(0, 0, 0, 0)

        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()

        self.engine.rootContext().setContextProperty("stopwatch_model", self.stopwatch_model)
        self.engine.load(os.fspath(Path(__file__).resolve().parent / "../frontend/qml/main.qml"))

        self.stopwatch_model.start_stop_button_clicked.connect(self.start_stop_button_clicked)
        self.stopwatch_model.reset_button_clicked.connect(self.reset_button_clicked)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_callback)

    def run(self) -> None:
        if not self.engine.rootObjects():
            sys.exit(-1)
        sys.exit(self.app.exec())

    def timer_callback(self) -> None:
        current_timestamp_ns = time.time_ns()
        self.diff = current_timestamp_ns - self.start_timestamp_ns
        self.stopwatch_model.set_timestamp(self.diff)

    def start(self) -> None:
        self.start_timestamp_ns = time.time_ns() - self.diff
        self.timer.start()
        self.stopwatch_model.set_state(State.RUNNING)

    def pause(self) -> None:
        self.timer.stop()
        self.stopwatch_model.set_state(State.PAUSED)

    def reset(self) -> None:
        self.diff = 0
        self.stopwatch_model.set_timestamp(0)
        self.stopwatch_model.set_state(State.RESET)

    def start_stop_button_clicked(self) -> None:
        state = self.stopwatch_model.get_state()
        if state == State.RESET:
            self.start()
        elif state == State.PAUSED:
            self.start()
        elif state == State.RUNNING:
            self.pause()

    def reset_button_clicked(self) -> None:
        self.reset()

