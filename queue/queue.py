class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []
        # super naive first pass implementation!

    def enqueue(self, item):
        self.storage.append(item)
        return

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            return None

    def len(self):
        return len(self.storage)

     # * Should have the methods: `enqueue`, `dequeue`, and `len`.
     # * enqueue should add an item to the back of the queue.
     # * dequeue should remove and return an item from the front of the queue.
     # * len returns the number of items in the queue.
