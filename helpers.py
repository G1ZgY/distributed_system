class Queue:
    def __init__(self):
        self.queue: list[Task] = []

    def push(self, item):
        self.queue.insert(0, item)

    def pop(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def get_all(self):
        return [task.duration for task in self.queue]


class Task:
    def __init__(self, duration):
        self.duration = duration
