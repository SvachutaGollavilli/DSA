class TreeNode():
    def __init__(self, value, left = None, right = None):
        self.value  = value
        self.left   = left
        self.right  = right

    def __str__(self):
        return str(self.value)
    



A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F



def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)



def In_order(node):
    if not node:
        return
    
    In_order(node.left)
    print(node)
    In_order(node.right)


def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)


#iterative pre order traversal DFS
def pre_order_iterative(node):
    stack = [node]

    while stack:
        node    =   stack.pop()
        print(node)

        if node.right : stack.append(node.right)
        if node.left  : stack.append(node.left)
        print(node)



#BFS using deque
from collections import deque
def bfs(node):
    q = deque()
    q = q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left:   q.append(node.left)
        if node.right:  q.append(node.right)


#check if element exists
def search(node, target):
    if not node:
        return False
    
    if target == node:
        return True
    
    return search(node.left, target) or search(node.right, target)


#Binary Search Tree

def bst(node, target):
    if not node:
        return False
    
    if node.value == target:
        return True
    
    if target < node.value: return bst(node.left, target)
    else: return bst(node.right, target)



