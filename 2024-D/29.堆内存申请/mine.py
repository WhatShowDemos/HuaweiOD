
mem = [0]*100;
free = [];

class free_mem:
    start = -1;
    end = -1;
    space = 0;
    def __init__(self, start, end):
        self.start = start;
        self.end = end;
        self.space = self.end - self.start + 1;
    def overlap(self, start, end):
        if start >= self.start or start <= self.end:
            return True;
        if end >= self.start or end <= self.end:
            return True;
    
    
f = open("in1");
mem_req = int(f.readline());

while True:
    