from collections import deque
from abc import ABC
from threading import Thread
from time import sleep
from DataStructures.TaskState import Priority, State


class BaseScheduler(ABC):

    def __init__(self, core1, core2, core3, core4):
        self.order = []
        self.order_first = []
        self.waiting_queue = deque([])
        self.ready_queue = deque([])
        self.core1 = core1
        self.core2 = core2
        self.core3 = core3
        self.core4 = core4
        self.priority = Priority.none
        self.quantum = 3

    def print_task(self):
        single_thread = Thread(target=self.printInfo)
        single_thread.start()

    def printInfo(self):
        while self.waiting_queue or \
                self.ready_queue or \
                self.core1.executing_task_id != -1 or \
                self.core2.executing_task_id != -1 or \
                self.core3.executing_task_id != -1:
            sleep(1)
            print('waiting: ', ', '.join([task.name for task in self.waiting_queue]))
            print(self.core1)
            print(self.core2)
            print(self.core3, end='\n\n')

        if self.core1.executing_task_id == -1 and \
                self.core2.executing_task_id == -1 and \
                self.core3.executing_task_id == -1:
            # x = int(round(self.core1.idle_timer.stop()))
            # y = int(round(self.core2.idle_timer.stop()))
            # c = int(round(self.core3.idle_timer.stop()))
            print('waiting: ', [task.name for task in self.waiting_queue])
            print(self.core1.get_idle_time())
            print(self.core2.get_idle_time())
            print(self.core3.get_idle_time())
            # print(self.order_first)
            # print(self.order)

    @classmethod
    def add_to_ready(cls):
        raise NotImplementedError

    @classmethod
    def add_from_waiting(cls):
        raise NotImplementedError

    @classmethod
    def start(cls):
        raise NotImplementedError

    def check_and_add_task_to_cpus(self, task):
        if task.is_resources_available():
            if self.core1.executing_task_id == -1:
                task.state = State.ready
                self.core1.add_task(task)
                self.order.append(task.executing_time)
            elif self.core2.executing_task_id == -1:
                self.core2.add_task(task)
                self.order.append(task.executing_time)
            elif self.core3.executing_task_id == -1:
                self.core3.add_task(task)
                self.order.append(task.executing_time)
        else:
            self.waiting_queue.append(task)
