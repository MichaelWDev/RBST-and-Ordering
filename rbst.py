import random

class Node:
	'''
	This is the Node class for the RBST.
	Each node holds some data. This is one element in the dynamic sequence.
	It is also augmented with the size of its subtree.
	'''

	def __init__(self, d, left = None, right = None):
		self.data = d
		self.left, self.right = left, right
		self.update_size()

	def increment_size(self):
		'''
		This function can be used to increment the size field when needed. This is mostly called when inserting.
		'''
		self.size += 1

	def update_size(self):
		'''
		This function can be used to safely update the size field of a node. After splits, the node's size needs to reflect the true size of the elements in its subtree.
		'''
		self.size = (self.left.size if self.left else 0) + (self.right.size if self.right else 0) + 1

	def __str__(self):
		''' This can be used to print nodes when testing.
		'''
		return f"data = {self.data}, value = {self.value}, size = {self.size}"

'''
This is a Randomly balanced binary search tree that encodes a dynamic sequence.
Note that this is a dynamic sequence, and not a dictionary data structure. The inorder traversal prints out the sequence.
The first element in the sequence is indexed from 1, and the the last element in the sequence is indexed n (or size).
'''
class RBST:

	def __init__(self, root = None):
		self.root = root

	def __len__(self):
		'''
		Returns the number of elements stored in the data structure.
		This is called using the in-built len function.
		'''
		return self.root.size if self.root else 0

	def insert_normal(self, data, rank):
		'''
		Insert an item (data) in position rank. No balancing is done.
		This is a wrapper function that calls our own recursive_insert_normal function.
		'''
		self.root = self.recursive_insert_normal(self.root, data, rank)

	def recursive_insert_normal(self, T, data , rank):
		'''
		Actual recursive function that performs the insert.

		'''

		# if the tree is empty, create a new node
		if T is None:
			return Node(data)

		# get the root rank in the subtree
		left_size = T.left.size if T.left != None else 0
		root_rank = left_size + 1

		# if the rank is less than or equal to the root_rank, go left
		if rank <= root_rank:
			T.left = self.recursive_insert_normal(T.left, data, rank)
		# otherwise go right
		else:
			T.right = self.recursive_insert_normal(T.right, data, rank - root_rank)

		# then update the subtree size
		T.update_size()

		# return the updated node
		return T

	# ------


	def inorder(self):
		'''
		This performs an inorder traversal of the tree.
		Instead of printing the nodes, this returns a generator object, which can be used to step through each node in the inorder traversal, one at a time.
		This is wrapper function that calls our own recursive_inorder function.
		'''

		yield from self.recursive_inorder(self.root)

	# -------


	def recursive_inorder(self, T):

		# check if the subtree is empty, if it is then stop
		if T is None:
			return

		# get all items from left subtree
		yield from self.recursive_inorder(T.left)

		# get current node data
		yield T.data

		# get all items from right subtree
		yield from self.recursive_inorder(T.right)



	# -------
		


	def split(self, rank):
		'''
		This function splits the tree based on rank, so that the sequence containing items in indices 1, through rank (inclusive) are on one tree, while the seuqnce containing items in indices rank+1 through n (size) are on the other tree.
		This is a wrapper function that calls our own recursive_split function.
		'''
		ret = self.recursive_split(self.root, rank)
		return [RBST(ret[0]), RBST(ret[1])]

	def recursive_split(self, T, rank):
		'''
		The recursive function that actually perfroms the split.
		Should split the input tree T based on rank. Should return the root nodes of two trees L, and R, where L encodes the sequence of elements [1, ..., rank], and R encodes the sequence of elements [rank+1, ..., size].
		'''

		# check if the tree is empty, return none for the split
		if T is None:
			return [None, None]

		# get the root rank in the subtree
		left_size = T.left.size if T.left != None else 0
		root_rank = left_size + 1

		# if the rank is less than or equal to the root_rank, split is in the left sub
		if (rank < root_rank):
			[L_L, R_L] = self.recursive_split(T.left, rank)
			T.left = R_L

			T.update_size()

			return [L_L, T]

		# otherwise split is in the right
		else:
			[L_R, R_R] = self.recursive_split(T.right, rank - root_rank)
			T.right = L_R

			T.update_size()

			return [T, R_R]
		
	# ------


	def insert(self, data, rank):
		'''
		This function inserts data at position rank. This performs balancing based on the rules of a randomly built binary search tree.
		This is a wrapper function which calls our own recursive_insert function.
		'''
		self.root = self.recursive_insert(self.root, data, rank)

	def recursive_insert(self, T, data, rank):
		'''
		This function performs the actual insert. 
		With probability 1 / (T.size + 1), the new element is inserted at the root (using split).
		Else it is recursively inserted in the subtree.
		'''

		# check if the tree is empty, return node with data
		if T is None:
			return Node(data)

		# check if the random int of (0, T.size) is equal to 0 (true)
		if random.randint(0, T.size) == 0:
			[L, R] = self.recursive_split(T, rank - 1)
			return Node(data, L, R)

		# get the root rank in the subtree
		left_size = T.left.size if T.left != None else 0
		root_rank = left_size + 1

		if rank <= root_rank:
			T.left = self.recursive_insert(T.left, data, rank)

		else:
			T.right = self.recursive_insert(T.right, data, rank - root_rank)

		# update the tree and return it
		T.update_size()
		return T

		# -------


	def select(self, rank):
		'''
		Selects and returns a pointer (reference) to the Node object of the sequence in position rank.
		This is a wrapper function that calls recursive_select function.
		'''
		return self.recursive_select(self.root, rank)

	def recursive_select(self, T, rank):

		# if the tree is empty, return none
		if T is None:
			return None

		
		# get the root rank in the subtree
		left_size = T.left.size if T.left != None else 0
		root_rank = left_size + 1


		# node found at the given rank, return T
		if rank == root_rank:
			return T

		# target rank is smaller, so go left
		elif rank < root_rank:
			return self.recursive_select(T.left, rank)

		# target rank is larger, so go right and adjust the rank
		else:
			return self.recursive_select(T.right, rank - root_rank)

	# -------
