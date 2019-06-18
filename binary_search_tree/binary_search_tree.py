from math import inf


def equal_to(value):
    def is_equal(something):
        if something == value:
            return True
        else:
            return False

    enclosure = is_equal
    return enclosure


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def _seek(self, value, passing=equal_to(None)):
        if value >= self.value:
            if passing(self.right):
                return self
            else:
                return self.right._seek(value)
        elif value < self.value:
            if passing(self.left):
                return self
            else:
                return self.left._seek(value)

    def insert(self, value):
        branch = self._seek(value)

        if value >= branch.value:
            branch.right = BinarySearchTree(value)
        else:
            branch.left = BinarySearchTree(value)

    def contains(self, target):
        maybe_this_ = equal_to(target)
        branch = self._seek(target, maybe_this_)
        return maybe_this_(branch.value)

    def get_max(self):
        infinity = inf
        branch = self._seek(infinity)
        return branch.value

    def for_each(self, cb):
        cb(self.value)

        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
