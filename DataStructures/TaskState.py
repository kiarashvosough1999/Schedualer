import enum


class State(enum.Enum):
    ready = 1
    waiting = 2
    running = 3


class Priority(enum.Enum):
    low = 3
    med = 2
    high = 1
    none = -1


def get_state_text(state):
    if state == State.low:
        return 'ready'
    elif state == State.med:
        return 'waiting'
    elif state == State.high:
        return 'running'


def get_priority_text(priority):
    if priority == Priority.low:
        return 'X'
    elif priority == Priority.med:
        return 'Y'
    elif priority == Priority.high:
        return 'Z'
