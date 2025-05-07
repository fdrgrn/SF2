class Progression:
    '''
    Iterator producing a generic progression

    Default iterator gives the whole numbers
    '''

    def __init__(self, start = 0):
        self._current = start
    
    def _advance(self):
        self.current += 1

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer
        
    def __iter__(self):
        return self
    
    def printProgression(self, n):
        print(' '.join(str(next(self)) for _ in range(n)))

    def lstProgression(self, n):
        return [int(next(self)) for _ in range(n)]
    
if __name__ == "__main__":
    Progression().printProgression(10)
    Progression(12).printProgression(10)