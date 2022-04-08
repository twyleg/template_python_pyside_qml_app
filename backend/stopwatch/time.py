from PySide6.QtCore import QObject, Signal, Property


class Time(QObject):
    def __init__(self, millis):
        QObject.__init__(self)
        self._millis = millis

    def get_millis(self):
        return self._millis

    def set_millis(self, millis):
        self._millis = millis
        self.millis_changed.emit()

    @Signal
    def millis_changed(self):
        pass

    millis = Property(int, get_millis, set_millis, notify=millis_changed)
