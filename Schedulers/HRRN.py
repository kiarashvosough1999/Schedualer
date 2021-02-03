from DataStructures.TaskState import State
from DataStructures.Timer import Timer
from Schedulers.Base import BaseScheduler


class HRRN(BaseScheduler):

    def __init__(self, core1, core2, core3, core4):
        super().__init__(core1, core2, core3, core4)
        self.timer = Timer()
        self.timer.start()
        self.elapsed = 0

    def add_to_ready(self):
        self.sort_by_ratio(self.ready_queue)
        for task in self.ready_queue:
            task.acquire_lock_for_resourses()
            self.check_and_add_task_to_cpus(task)
            task.release_lock_for_resourses()
        self.ready_queue = []

    def add_from_waiting(self):
        match_arriavl_time = []
        self.elapsed += self.timer.stop()
        self.timer.start()

        for task in self.waiting_queue:
            task.acquire_lock_for_resourses()
            if task.arriaval_time <= self.elapsed and task.is_resources_available():
                task.state = State.ready
                self.ready_queue.append(task)
                match_arriavl_time.append(task)
            task.release_lock_for_resourses()
        # if self.ready_queue:
        #     print('ready', [x.response_ratio for x in self.ready_queue])
        for task in match_arriavl_time:
            self.waiting_queue.remove(task)

    def start(self):
        self.print_task()
        while self.ready_queue or self.waiting_queue:
            self.sort_by_arraival(self.waiting_queue)
            self.add_from_waiting()
            self.add_to_ready()

    def sort_by_ratio(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j].get_response_ratio(self.elapsed) > arr[j + 1].get_response_ratio(self.elapsed):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def sort_by_arraival(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j].arriaval_time >= arr[j + 1].arriaval_time:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
