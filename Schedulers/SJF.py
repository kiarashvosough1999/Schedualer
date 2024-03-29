from DataStructures.TaskState import State
from Schedulers.Base import BaseScheduler


class SJF(BaseScheduler):

    def __init__(self, core1, core2, core3, core4):
        super().__init__(core1, core2, core3, core4)

    def add_to_ready(self):
        for task in self.ready_queue:
            task.acquire_lock_for_resourses()
            self.check_and_add_task_to_cpus(task)
            task.release_lock_for_resourses()
        self.ready_queue = []

    def add_from_waiting(self):
        temp_list = []

        for task in self.waiting_queue:
            task.acquire_lock_for_resourses()
            if task.is_resources_available():
                task.state = State.ready
                self.ready_queue.append(task)
                temp_list.append(task)
            task.release_lock_for_resourses()
        for item in temp_list:
            self.waiting_queue.remove(item)

    def start(self):
        self.sort_by_burstTime()
        self.order_first = [x.executing_time for x in self.ready_queue]
        self.print_task()
        while self.ready_queue or self.waiting_queue:
            if self.core1.executing_task_id == -1 and \
                    self.core2.executing_task_id == -1 and \
                    self.core3.executing_task_id == -1:
                self.sort_by_burstTime()
                self.add_from_waiting()

                self.add_to_ready()

    def sort_by_burstTime(self):
        low = 0
        high = len(self.ready_queue) - 1
        self.quickSort(low, high)

    def quickSort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quickSort(low, pi - 1)
            self.quickSort(pi + 1, high)

    def partition(self, low, high):
        i = (low - 1)
        pivot = self.ready_queue[high].executing_time

        for j in range(low, high):
            if self.ready_queue[j].executing_time < pivot:
                i = i + 1
                self.ready_queue[i], self.ready_queue[j] = self.ready_queue[j], self.ready_queue[i]

        self.ready_queue[i + 1], self.ready_queue[high] = self.ready_queue[high], self.ready_queue[i + 1]
        return i + 1
