# Breadth First Search

from collections import deque

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        children = f'\nLeft child: {self.left}\nRight child: {self.right}\n' \
            if (self.left or self.right) else '\nNo children'
        return f'''Node value = {self.val} {children}'''

def level_order_traversal(root:Node) -> list[list[int]]:
    result = []
    queue = deque([root]) # intialize the queue
    while queue: # or while len(queue)>0
        n = len(queue) # snapshot of the level
        new_level = []
        for _ in range(n):
            node = queue.popleft() # classic FIFO
            new_level.append(node.val)
            for child in [node.left, node.right]: # left to right
                if child:
                    queue.append(child)
        result.append(new_level)
    return result

ceo=Node(100)
cto=Node(200)
cfo=Node(300)
ceo.left=cto
ceo.right=cfo

cto.left=Node(400)
cto.right=Node(500)
cfo.left=Node(600)
cfo.right=Node(700)

print(level_order_traversal(ceo))