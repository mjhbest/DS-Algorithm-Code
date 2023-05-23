class Stack:
    def __init__(self):
        """스택 데이터 구조의 생성자"""
        self.arr = []

    def is_empty(self):
        """스택이 비어있는지 확인 : True(비어있는 경우), False(비어있지 않은 경우)"""
        if len(self.arr) == 0:
            return True
        else:
            return False

    def print_stack(self):
        print()
        print("현재 스택은 다음과 같습니다:")
        print(self.arr)
        print()

    def push(self, data):
        """스택의 top에 데이터를 추가"""
        self.arr.append(data)
        # print("스택에 데이터가 추가되었음 : ", data)

    def npush(self, data, n):
        """data를 입력받아서 n번 push하는 함수"""
        for i in range(n):
            self.push(data)

    def pop(self, index=-1):
        """스택의 top에서 데이터를 삭제 및 반환"""
        if self.is_empty():
            print("Pop 실패 : 스택이 비어있음.")
            return -1

        return self.arr.pop(index)

    def npop(self, n):
        """스택에서 n번 pop하는 함수"""
        if n > len(self.arr):
            return -1

        for i in range(n):
            self.pop()

    def top(self):
        """Stack의 Top에 있는 값을 반환"""
        if self.is_empty():
            print("Top 실패 : 스택이 비어있음.")
            return -1

        return self.arr[-1]


new_stack = Stack()
new_stack.npush('a', 3)
new_stack.npush('b', 4)
new_stack.pop()
new_stack.npush('c', 2)
new_stack.print_stack()
