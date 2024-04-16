class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def save_to_memento(self):
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def backup(self):
        self._mementos.append(self._originator.save_to_memento())

    def undo(self):
        if not self._mementos:
            return
        memento = self._mementos.pop()
        self._originator.restore_from_memento(memento)

    def clear(self):
        self._mementos.clear()
