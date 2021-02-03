from DataStructures.Timer import Timer
from DataStructures.TaskState import get_priority_text, get_state_text

class Task:

    def __init__(self, id, name, priority, state, executing_time, needed_resources, arrival_time):
        self.id = id
        self.name = name
        self.priority = priority
        self.state = state
        self.executing_time = executing_time
        self.executed_time_since_created = 0
        self.should_execute_time = executing_time
        self.needed_resources = needed_resources  # list
        self.waiting_timer = Timer()
        self.is_finished = False
        self.arriaval_time = arrival_time
        self.response_ratio = 0
        self.suspended_due_to_long_burst = False

    def get_response_ratio(self, now_time):
        waiting = now_time - self.arriaval_time
        self.response_ratio = (waiting + self.executing_time) / self.executing_time
        return self.response_ratio

    def is_finished_now(self):
        if self.should_execute_time - self.executed_time_since_created <= 0 or \
                self.should_execute_time - self.executing_time <= 0:
            return True
        return False

    def get_next_task(self):
        task = Task(self.id,
                    self.name,
                    self.priority,
                    self.state,
                    self.should_execute_time - self.executed_time_since_created,
                    self.needed_resources,
                    self.arriaval_time)
        task.should_execute_time = self.should_execute_time
        task.executed_time_since_created = self.executed_time_since_created
        return task

    def set_executing_time(self, quantum):
        if quantum <= self.should_execute_time - self.executed_time_since_created:
            self.executing_time = quantum

    def modify_executed_time(self):
        if self.executing_time >= self.should_execute_time:
            self.is_finished = True
        else:
            self.executed_time_since_created += self.executing_time

    def get_executing_time(self):
        return self.should_execute_time - self.executed_time_since_created

    def is_resources_available(self):
        for res in self.needed_resources:
            if not res.get_available() > 0:
                return False
        return True

    def acquire_lock_for_resourses(self):
        self.needed_resources[0].lock.acquire()
        self.needed_resources[1].lock.acquire()

    def release_lock_for_resourses(self):
        self.needed_resources[1].lock.release()
        self.needed_resources[0].lock.release()

    def __str__(self):
        return self.name + ' ' + get_priority_text(self.priority) +\
               ' burst time: ' +\
               str(self.should_execute_time) +\
               ' arrival time:  ' +\
               str(self.arriaval_time) + ' state: ' + str(self.state)
