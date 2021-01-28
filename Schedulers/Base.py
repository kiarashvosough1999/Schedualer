from collections import deque
from abc import abstractclassmethod, ABC

from CPU.CPUCore import CPUCore


class BaseScheduler(ABC):
    def __init__(self):
        self.waiting_queue = deque([])
        self.ready_queue = deque([])
        self.core1 = CPUCore("core 1")
        self.core2 = CPUCore("core 2")
        self.core3 = CPUCore("core 3")
        self.core4 = CPUCore("core 4")

    @abstractclassmethod
    def add_to_ready(cls, new_task):
        raise NotImplementedError

    # @abstractclassmethod
    # def get_next_process(cls):
    #     raise NotImplementedError

    @abstractclassmethod
    def start(cls):
        raise NotImplementedError
