class ArrayStack :
    def __init__(self,capacity):
        self.capacity = capacity #생성자 정의
        self.array = [None]*self.capacity #용량(고정)
        self.top = -1#요소를 저장할 배열
    def isEmpty(self) :# 스택 상단의 인덱스
        return self.top == -1
    def isFull(self) :
        return self.top == self.capacity-1
    def push(self,item):
        if not self.isFull():
            self.top+=1
            self.array[self.top]=item
        else:
            print("stack overflow")
    def pop(self):
        if not self.isEmpty():
            item= self.array[self.top]
            self.top -= 1
            return item
        else:
            print("stack underflow")
            return None
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("stack underflow")
    def __str__(self):
        return str(self.array[0:self.top+1])
    
if __name__ == "__main__":
    s = ArrayStack(10)
    for i in range(1,6):
        s.push(i)
    print(" push 5회: ", s)
    # print(" push 5회: ", s.array)
    # print(" push 5회: ", s.array)
    s.pop()
    print('pop 1회',s)
    print(s.peek())