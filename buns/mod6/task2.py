class DoubleElement:
    def __init__(self, *lst):
        self.list = [*lst, None]
        self.count = 0

    def __next__(self):
        self.length = len(self.list)
        if self.current_index + 1 < self.length:
            x = (self.list[self.current_index], self.list[self.current_index + 1])
            self.current_index += 2
            return x
        raise StopIteration

    def __iter__(self):
        self.current_index = 0
        return self

dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5, 6, 7)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3)
for pair in dL:
    print(pair)
