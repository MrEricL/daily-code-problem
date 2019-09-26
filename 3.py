'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''
import collections

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def serialize(root):
	def encode(x):
		if x:
			vals.append(str(x.val))
			encode(x.left)
			encode(x.right)
		else:
			vals.append("#")
	vals = []
	encode(root)
	return " ".join(vals)

def deserialize(data):
	'''# Using iterator
	def decode():
	val = next(vals)
	if val == "#":
	return None
	else:
	node = TreeNode(int(val))

	node.left = decode()
	node.right = decode()
	return node
	vals = iter(data.split())'''

    # Using deque
	def decode(nodes):
		val = nodes.popleft()
		if val == "#":
			return None
		else:
			node = Node(val)
			node.left = decode(nodes)
			node.right = decode(nodes)
			return node

	vals = collections.deque(data.split())
	return decode(vals)

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(deserialize(serialize(node)).left.left.val == 'left.left')
