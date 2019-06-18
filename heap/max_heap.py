from math import inf


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        heap = self.storage
        heap.append(value)
        position = len(heap) - 1
        self._bubble_up(position)

    def delete(self):
        heap = self.storage
        head = heap.pop(0)
        self._sift_down(0)

        return head

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return index

        heap = self.storage
        parent = (index-1) // 2

        if heap[parent] > heap[index]:
            return index
        else:
            heap[index], heap[parent] = heap[parent], heap[index]
            return self._bubble_up(parent)

    def _sift_down(self, index):
        heap = self.storage
        if index*2+2 >= len(heap):
            return index

        branches = (index*2)+1, (index*2)+2
        b_values = [0, 0]
        for k, v in enumerate(branches):
            try:
                b_values[k] = heap[v]
            except IndexError:
                b_values[k] = -inf

        if heap[index] >= max(b_values):
            self._sift_down(branches[0])
            self._sift_down(branches[1])
            return index

        if b_values[0] >= b_values[1]:
            swap = branches[0]
        else:
            swap = branches[1]

        heap[index], heap[swap] = heap[swap], heap[index]
        return self._sift_down(swap)
