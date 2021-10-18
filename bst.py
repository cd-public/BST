# provided, could be named "BST", feel free to edit
class node:

	# provided, feel free to edit
	def __repr__(self):
		lstr = ""
		mstr = ""
		if self.less != None:
			lstr = "(" + self.less.__repr__() + ") <- "
		if self.more != None:
			mstr = " -> (" + self.more.__repr__() + ")"
		return lstr + str(self.data) + mstr
	
	# provided, feel free to edit
	def __str__(self):
		return self.__repr__()

	# provided, feel free to edit
	def __init__(self, d, l=None, m=None):
		self.data = d # piece of data (not None)
		self.less = l # None or another node
		self.more = m # None or another node
		
	# calculate size of the BST - the number of elements it contains
	# * always greater than zero
	def size(self):
		pass
		
	# calculate size of the BST - the number of elements in the longest single path
	# * always greater than zero	
	def depth(self):
		pass
	
	# given d, return the BST containing all elements in the BST and also d
	# * may ignore the case of duplicates, like adding "2" twice
	# * may assume added elements are of comparable types
	def insert(self, d):
		pass

	# given d, return true if d is in the BST
	# * may assume added elements are of comparable types		
	def contains(self, d):
		pass
		
	# return the minimum value in the bst
	def getMin(self):
		pass
	
	# return the maximum value in the bst
	def getMax(self):
		pass
			
	# given d, return the BST containing all elements in the BST except d
	# * may ignore the case of duplicates
	# * may assume elements are of comparable types
	def remove(self, d):
		pass
		
# provided as a curiousity, an outer class to wrap node and allow BSTs to be of size zero
# feel free to edit
class BST:
	
	def __repr__(self):
		return "BST: " + self.node.__repr__()
	
	def __str__(self):
		return "BST: " + self.node.__str__()

	def __init__(self, d=None):
		if d == None:
			self.node = None # always a node or None
		else:
			self.node = node(d) # always a node or None
		
	def size(self):
		if self.node == None:
			return 0
		return self.node.size()
	
	def depth(self):
		if self.node == None:
			return 0
		return self.node.depth()
	
	# this returns self for the autograder as a convenience
	def insert(self, d):
		if self.node == None:
			self.node = node(d)
		else:
			self.node.insert(d)
		return self
		
	def contains(self, d):
		if self.node == None:
			return False
		return self.node.contains(d)
	
	# returns None if the BST contains no min
	def getMin(self):
		if self.node == None:
			return
		return self.node.getMin()
	
	# returns None if the BST contains no max
	def getMax(self):
		if self.node == None:
			return
		return self.node.getMax()
	
	# this returns self for the autograder as a convenience
	def remove(self, d):
		if self.node == None:
			return
		self.node = self.node.remove(d)
		return self
	