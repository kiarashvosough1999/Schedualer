
class Resource:

    def __init__(self, name, count):
        self.name = name
        self.count = count
        self.in_use = 0

    def set_count(self, count):
        self.count = count

    def get_available(self):
        return self.count - self.in_use