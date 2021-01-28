from time import sleep
from DataStructures.Timer import Timer
from threading import Thread


class CPUCore:

    def __init__(self, core_name):
        self.core_name = core_name
        self.task = None
        self.executing_task_id = -1
        self.idle_time = 0
        self.idle_timer = Timer()
        self.idle_timer.start()

    def get_task_count(self):
        return len(self.task)

    def add_task(self, task):
        self.idle_time += self.idle_timer.stop()
        self.task = task
        self.executing_task_id = task.id
        single_thread = Thread(target=self.runnable_task, args=(task,))
        single_thread.start()
        # print("finished")

    def runnable_task(self, task):
        task.needed_resources[0].in_use += 1
        task.needed_resources[1].in_use += 1
        print("executing")
        sleep(task.executing_time)
        self.idle_timer.start()
        self.executing_task_id = -1
        print("finished task with name",task.name)
        task.needed_resources[0].in_use -= 1
        task.needed_resources[1].in_use -= 1
