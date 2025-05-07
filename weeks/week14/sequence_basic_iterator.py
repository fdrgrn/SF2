class SequenceIterable:
    def __init__(self, start, end):
        self.start_num = start
        self.end_num = end

    def __iter__(self):
        return Sequence(self.start_num, self.end_num)

    def __len__(self):
        return self.end - self.start + 1
        


class Sequence:
    def __init__(self, start, end):
        self.start_num = start
        self.end_num = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start_num > self.end_num:
            raise StopIteration
        else:
            self.start_num += 1
            return self.start_num - 1
    def __len__(self):
        return self.end_num - self.start_num + 1


if __name__ == "__main__":
    start, end = 3, 10
    seq = Sequence(3, 10)

    for elem in seq:
        print(elem)
        
    print()

    print(len(seq))
    for elem in Sequence(start, end):
        print(elem)