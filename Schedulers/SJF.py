from Schedulers.Base import BaseScheduler


class SJF(BaseScheduler):

    def __init__(self):
        super().__init__()

    def add_to_ready(self):

        for item in self.ready_queue:
            if item.is_resources_available():
                if self.core1.executing_task_id == -1:
                    self.core1.add_task(item)
                elif self.core2.executing_task_id == -1:
                    self.core2.add_task(item)
                elif self.core3.executing_task_id == -1:
                    self.core3.add_task(item)
            else:
                self.waiting_queue.append(item)
        self.ready_queue = []

    def add_from_waiting(self):
        list = []
        for i in range(len(self.waiting_queue)):
            if self.waiting_queue[i].is_resources_available():
                self.ready_queue.append(self.waiting_queue[i])
                list.append(self.waiting_queue[i])

        for item in list:
            self.waiting_queue.remove(item)


    def start(self):
        self.sort_by_burstTime()
        while self.ready_queue or self.waiting_queue:
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
