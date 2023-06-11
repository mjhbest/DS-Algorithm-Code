# Definition: Binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def delete_Node(root, key):
    # if root doesn't exist, just return it
	if not root: 
        return root

	# Find the node in the left subtree	if key value is less than root value
	if root.val > key: 
		root.left = delete_Node(root.left, key)
	# Find the node in right subtree if key value is greater than root value, 
	elif root.val < key: 
		root.right= delete_Node(root.right, key)
	# Delete the node if root.value == key
	else: 
	# If there is no right children delete the node and new root would be root.left
		if not root.right:
			return root.left

	# If there is no left children delete the node and new root would be root.right	
		if not root.left:
			return root.right
            
    # 만약 왼쪽과 오른쪽 자식이 모두 존재하면 오른쪽 서브트리에서 최소값을 찾아서 해당 노드의 값을 루트 값으로 대체한다.
    # 그리고 오른쪽 서브트리에서 해당 최소값을 가지는 노드를 삭제한다.
    temp_val = root.right # 17
    mini_val = temp_val.val # 17
    while temp_val.left:
        temp_val = temp_val.left
        mini_val = temp_val.val
    # 오른쪽 서브트리에서 최소 노드를 삭제한다.
    root.right = delete_Node(root.right, root.val)
	return root
