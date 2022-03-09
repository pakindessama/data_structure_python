class Stack(object):
    def __init__(self):
        self.items = []

    def add(self, item):
        return self.items.append(item)

    def remove(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
