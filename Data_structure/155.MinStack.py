class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.helper = []
        

    def push(self, x: int) -> None:
        self.s.append(x)
        if self.helper != []:
            a = self.helper.pop()
            self.helper.append(a)
            if x > a:
                self.helper.append(a)
            else:
                self.helper.append(x)
        else:
            self.helper.append(x)

    def pop(self) -> None:
        if self.s:
            a = self.s.pop()
            self.helper.pop()
            return a 

    def top(self) -> int:
        if self.s:
            a = self.s.pop()
            self.s.append(a)
            return a

    def getMin(self) -> int:
        if self.helper:
            a = self.helper.pop()
            self.helper.append(a)
            return a
        