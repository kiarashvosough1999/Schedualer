from DataStructures.Queue import MyQueue
from DataStructures.TaskState import Priority
from Schedulers.Base import BaseScheduler
from Schedulers.FCFS import FCFS
from Schedulers.RR import RR
from Schedulers.SJF import SJF


class MFQ(BaseScheduler):

    def __init__(self, core1, core2, core3, core4):
        super().__init__(core1, core2, core3, core4)
        self.queue_1 = RR(core1, core2, core3, core4)
        self.queue_2 = RR(core1, core2, core3, core4)
        self.queue_3 = FCFS(core1, core2, core3, core4)

    def start(self):
        pass

    def add_to_ready(self):
        level = 0
        while self.ready_queue:
            self.queue_1.ready_queue = self.ready_queue
            level = 2
            self.queue_2.start()

        pass

    def get_task_ready(self, level, queue):
        to_delete = []
        for task in self.ready_queue:
            if not task.is_finished:
                task.executing_time = 3 + 3 * level
                queue.ready_queue.append(task)
            else:
                to_delete.append(task)
        for item in to_delete:
            self.ready_queue.remove(item)
