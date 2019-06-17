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

    def seek(self, value, cb=equal_to(None)):
        branch = self
        if value >= self.value:
            if cb(self.right):
                return branch
            else:
                branch = self.right
                return branch.seek(value)
        elif value < self.value:
            if cb(self.left):
                return self
            else:
                branch = self.left
                return branch.seek(value)

    def insert(self, value):
        branch = self.seek(value)
        # print(branch.value, branch.right, branch.left)
        if value >= branch.value:
            branch.right = BinarySearchTree(value)
        else:
            branch.left = BinarySearchTree(value)

    def contains(self, target):
        maybe_this = equal_to(target)
        branch = self.seek(target, maybe_this)
        return maybe_this(branch.value)

    def get_max(self):
        infinity = inf
        branch = self.seek(infinity)
        return branch.value

    def for_each(self, cb):
      cb(self.value)
      if self.left != None:
          self.left.for_each(cb)
      if self.right != None:
          self.right.for_each(cb)

