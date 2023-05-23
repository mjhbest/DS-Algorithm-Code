class Node:
    def __init__(self, item, n):  # Node 생성자
        self.item = item
        self.next = n


def add(item):  # 삽입 연산
    global size
    global front
    global rear
    new_node = Node(item, None)
    if size == 0:
        front = new_node
    else:
        ### 실습 ###
        rear.next = new_node

    ### 실습 ###
    rear = new_node

    size += 1


def remove():  # 삭제 연산
    global size
    global front
    global rear
    if size != 0:
        fitem = front.item
        front = front.next
        size -= 1
        if size == 0:
            rear = None
        return fitem


def print_q():  # 큐 출력
    p = front
    print('front: ', end='')
    while p:
        if p.next != None:
            print(p.item, '->   ', end='')
        else:
            print(p.item, end='')
        p = p.next
    print('  : rear')


front = None
rear = None
size = 0

add('apple')
add('orange')
add('cherry')
add('pear')

# print('사과, 오렌지, 체리, 배 삽입 후: \t', end='')
print_q()

# remove()
# print('remove한 후:\t\t', end='')
# print_q()

# remove()
# print('remove한 후:\t\t', end='')
# print_q()

# add('grape')
# print('포도 삽입 후:\t\t', end='')
# print_q()
