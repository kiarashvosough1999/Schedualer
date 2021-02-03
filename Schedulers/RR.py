from DataStructures.TaskState import State
from Schedulers.Base import BaseScheduler


class RR(BaseScheduler):

    def __init__(self, core1, core2, core3, core4):
        super().__init__(core1, core2, core3, core4)

    def add_to_ready(self):
        new_tasks = []
        for task in self.ready_queue:
            task.acquire_lock_for_resourses()
            res = self.check_and_add_task_to_cpus(task)
            if res and not task.is_finished_now():
                new_tasks.append(res)
            task.release_lock_for_resourses()
        self.ready_queue = []
        self.waiting_queue += new_tasks

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
        self.print_task()
        while self.ready_queue or self.waiting_queue:
            if self.core1.executing_task_id == -1 and \
                    self.core2.executing_task_id == -1 and \
                    self.core3.executing_task_id == -1:
                self.add_from_waiting()
                self.add_to_ready()

    def check_and_add_task_to_cpus(self, task):
        if task.is_resources_available():
            if self.core1.executing_task_id == -1:
                task.set_executing_time(self.quantum)
                task.modify_executed_time()
                self.core1.add_task(task)
                self.order.append(task.executing_time)
                return task.get_next_task()
            elif self.core2.executing_task_id == -1:
                task.set_executing_time(self.quantum)
                task.modify_executed_time()
                self.core2.add_task(task)
                self.order.append(task.executing_time)
                return task.get_next_task()
            elif self.core3.executing_task_id == -1:
                task.set_executing_time(self.quantum)
                task.modify_executed_time()
                self.core3.add_task(task)
                self.order.append(task.executing_time)
                return task.get_next_task()
        else:
            self.waiting_queue.append(task)

        return None
