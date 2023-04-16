class Superstack:
    def __init__(self):
        self.stack = []
    
    def push(self, v):
        self.stack.append(v)
    
    def pop(self):
        if self.stack:
            self.stack.pop()
    
    def inc(self, i, v):
        for j in range(min(i, len(self.stack))):
            self.stack[j] += v
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return 'Empty'
    
    def process_operations(self, operations):
        for operation in operations:
            parts = operation.split()
            if parts[0] == 'push':
                self.push(int(parts[1]))
                print(self.top())
            elif parts[0] == 'pop':
                self.pop()
                print(self.top())
            elif parts[0] == 'inc':
                self.inc(int(parts[1]), int(parts[2]))
                print(self.top())
