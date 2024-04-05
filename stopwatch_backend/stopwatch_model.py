# Copyright (C) 2024 twyleg
import time
from enum import IntEnum
from PySide6.QtCore import QObject, Signal, Slot

from stopwatch_backend.properties import PropertyMeta, Property


class State(IntEnum):
    RESET = 0
    RUNNING = 1
    PAUSED = 2


class Timer(QObject, metaclass=PropertyMeta):
    state = Property(int)
    millis = Property(int)
    seconds = Property(int)
    minutes = Property(int)
    hours = Property(int)

    def __init__(self, millis: int, seconds: int, minutes: int, hours: int) -> None:
        QObject.__init__(self)
        self.state = State.RESET
        self.millis = millis
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

        self.count_ns = 0
        self.last_timestamp_ns = 0

    @Slot()
    def start(self) -> None:
        self.last_timestamp_ns = time.time_ns()
        self.state = State.RUNNING

    @Slot()
    def pause(self) -> None:
        self.state = State.PAUSED

    @Slot()
    def reset(self) -> None:
        self.count_ns = 0
        self.state = State.RESET
        self.update()

    @Slot()
    def start_stop(self) -> None:
        state = self.state
        if state == State.RESET:
            self.start()
        elif state == State.PAUSED:
            self.start()
        elif state == State.RUNNING:
            self.pause()

    def update(self):
        if self.state == State.RUNNING:
            current_timestamp_ns = time.time_ns()
            diff = current_timestamp_ns - self.last_timestamp_ns
            self.count_ns += diff
            self.last_timestamp_ns = current_timestamp_ns

        count_ms = self.count_ns // (1000 * 1000)

        self.millis = count_ms % 1000
        self.seconds = (count_ms // 1000) % 60
        self.minutes = (count_ms // (1000 * 60)) % 60
        self.hours = (count_ms // (1000 * 60 * 60))


class Model(QObject, metaclass=PropertyMeta):

    active_timer = Property(Timer)
    timers = Property(list)

    def __init__(self) -> None:
        QObject.__init__(self)
        self.active_timer = Timer(0, 0, 0, 0)
        self.timers = []
        self.timers.append(self.active_timer)

    @Slot()
    def add_timer(self):
        self.timers.append(Timer(0, 0, 0, 0))

    @Slot(Timer)
    def activate_timer(self, timer: Timer):
        self.active_timer = timer

    def update_timers(self) -> None:
        for timer in self.timers:
            timer.update()
