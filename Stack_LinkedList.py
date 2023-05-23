class Node:  # Node 클래스
    def __init__(self, item, link):  # Node 생성자
        self.item = item
        self.next = link


def push(item):  # push 연산
    global top
    global size
    top = Node(item, top)
    size += 1


def peek():  # peek 연산
    if size != 0:
        return top.item


def pop():  # pop 연산
    global top
    global size
    if size != 0:
        top_item = top.item

        # 실습
        new_top = top.next
        top = new_top

        size -= 1
        return top_item


def print_stack():  # 스택 출력
    print('top ->\t', end='')
    p = top
    while p:
        if p.next != None:
            print(p.item, '-> ', end='')
        else:
            print(p.item, end='')
        # 실습
        p = p.next
    print()


top = None
size = 0

# push('apple')
# push('orange')
# push('cherry')

# print('사과, 오렌지, 체리  push 후:\t', end='')
# print_stack()
# print('top 항목: ', end='')
# print(peek())

# push('pear')
# print('배 push 후:\t\t', end='')
# print_stack()

# pop()
# push('grape')
# print('pop(), 포도 push 후:\t', end='')
# print_stack()
