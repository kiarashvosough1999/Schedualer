from DataStructures.Timer import Timer


class Task:

    def __init__(self, id, name, priority, state, executing_time, needed_resources):
        self.id = id
        self.name = name
        self.priority = priority
        self.state = state
        self.executing_time = executing_time
        self.needed_resources = needed_resources  # list
        self.waiting_timer = Timer()
        self.time_left_to_finish = 0

    def is_resources_available(self):
        for res in self.needed_resources:
            if not res.get_available() > 0:
                return False
        return True

    def __str__(self):
        return  self.name