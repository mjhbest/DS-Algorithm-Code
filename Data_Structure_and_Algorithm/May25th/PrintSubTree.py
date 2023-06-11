class Node:
    def __init__(self, key, value, left=None, right=None): # 노드 생성자
        self.key   = key
        self.value = value 
        self.left  = left 
        self.right = right 
        
class BST:           
    def __init__(self): # 트리 생성자
        self.root = None

    def put(self, key, value): # 삽입 연산
        ## [실습] ##
        self.root = self.put_item(self.root, key, value)
        
    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value) 
        if n.key > key: # 왼쪽 서브트리에 삽입
            ## [실습] ##
            n.left = self.put_item(n.left, key, value)
        elif n.key < key: # 오른쪽 서브트리에 삽입
            ## [실습] ##
            n.right = self.put_item(n.right, key, value) 
        else: # 노드 n의 value 갱신
            n.vlaue = value
        ## [실습] ##
        return n

    def get(self, k): # 탐색 연산
        item = self.get_item(self.root, k)
        return item
    
    def get_item(self, n, k):
        if n == None:
            return None # key를 발견 못함
        if n.key > k: # 왼쪽 서브트리 탐색
            return self.get_item(n.left, k)
        elif n.key < k: # 오른쪽 서브트리 탐색 
            return self.get_item(n.right, k) 
        else:
            return n # key를 가진 노드 발견
          
    def min(self): # 최솟값 가진 노드 찾기
        if self.root == None:
            return None
        return self.minimum(self.root)
    
    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def min_v2(self):
        if self.root is None:
            return None

        n = self.root
        while n.left is not None:
            n = n.left
        return n

    def preorder(self, n): # 전위순회
        if n != None:
            print(str(n.key),' ', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n): # 중위순회
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key),' ', end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n): # 후위순회
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.key),' ', end='')
              
    def levelorder(self, root): # 레벨순회
        q = []
        q.append(root)
        while len(q) != 0:  
            t = q.pop(0) 
            print(str(t.key), ' ', end='')
            if t.left != None: 
                q.append(t.left)  
            if t.right != None: 
                q.append(t.right)
                

    def print_subtree(self,k):
        k_node = self.get(k)
        self.inorder(k_node)

t = BST() # 이진탐색트리 객체 t 생성

#                                 500
#                 200                                       600
#         100             400
#     50      150    250                                              800
# 10                      350                                       700



t.put(500, 'apple') 
t.put(600, 'banana')
t.put(200, 'melon') 
t.put(100, 'orange')
t.put(400, 'lime') 
t.put(250, 'kiwi')
t.put(150, 'grape')
t.put(800, 'peach') 
t.put(700, 'cherry') 
t.put(50,  'pear')
t.put(350, 'lemon')
t.put(10,  'plum')

t.print_subtree(200)


# print('\n250: ',t.get(250).value)

# print('\nMin: ',t.min().key, t.min().value)

# print('전위순회:\t', end='')
# t.preorder(t.root)

# print('\n중위순회:\t', end='')
# t.inorder(t.root)
