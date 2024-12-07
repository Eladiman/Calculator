class Stack:

    def __init__(self):
        self._top_element = -1
        self._list = []

    def push(self, value):
        self._top_element += 1
        self._list.insert(0, value)

    def top(self):
        if not self.is_empty():
            return self._list[0]
        else:
            return None

    def pop(self):
        if not self.is_empty():
            self._top_element -= 1
            temp = self._list[0]
            self._list.pop(0)
            return temp
        else:
            return None

    def is_empty(self):
        return self._top_element == -1

    def to_string(self):
        return self._list
