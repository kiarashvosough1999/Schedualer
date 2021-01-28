from Schedulers.Base import BaseScheduler


class FCFS(BaseScheduler):

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

        while self.ready_queue or self.waiting_queue:
            self.add_from_waiting()

            self.add_to_ready()



