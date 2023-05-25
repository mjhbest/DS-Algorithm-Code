class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

# 재귀함수 
def height(node, depth):
    if node is None:
        return depth-1

    left_h = height(node.left, depth+1)
    right_h = height(node.right, depth+1)
    return max(left_h, right_h)

def num_node(node):
    if node is None:
        return 0

    left_num = num_node(node.left)
    right_num = num_node(node.right)
    return left_num + right_num + 1

def preorder(node):  # NLR
    print(node.key, end=' ') #N
    if node.left is not None: #L
        preorder(node.left)
    if node.right is not None:#R
        preorder(node.right)

def inorder(node): # LNR
    if node.left is not None: #L
        inorder(node.left)
    print(node.key, end=' ') #N
    if node.right is not None:#R
        inorder(node.right)

def postorder(node): #LRN
    if node.left is not None: #L
        postorder(node.left)
    if node.right is not None:#R
        postorder(node.right)
    print(node.key, end=' ') #N

def levelorder(node):
    queue = [node]
    while queue:
        top = queue.pop(0)
        print(top.key, end=' ')
        if top.left:
            queue.append(top.left)
        if top.right:
            queue.append(top.right)



root = Node('8',\
    Node('3',\
        Node('1'),\
        Node('6',\
            Node('4'),\
            Node('7'))),\
    Node('10',\
        None,\
        Node('14',\
            Node('13'),\
            None)))

print(height(root, 1))
print(num_node(root))
print("Pre : ",end='')
preorder(root)
print()

print("In : ",end='')
inorder(root)
print()

print("Post : ",end='')
postorder(root)
print()

print("Level : ",end='')
levelorder(root)
print()

