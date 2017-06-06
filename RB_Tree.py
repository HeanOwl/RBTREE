class Node():
	def __init__(self, inputValue):
		self.val = inputValue
		self.p = None
		self.left = None
		self.right = None
		self.color = "Red"
	def InvertColor(self):
		if self.color == "Red":
			self.color = "Black"
		else :
			self.color = "Red"

class RB_Tree():
	def __init__(self):
		self.root = None
	def Transplant(self, oldNode, newNode):
		if newNode != None:
			newNode.p = oldNode.p
		if oldNode.p == None:
			self.root = newNode
		elif oldNode.p.left is oldNode:
			oldNode.p.left = newNode
		elif oldNode.p.right is oldNode:
			oldNode.p.right = newNode
		#newNode.left = oldNode.left
		#newNode.right = oldNode.right
		
	def Insert_Value(self, value):
		newNode = Node(value)
		self.Insert(newNode)
	def Insert(self, inputNode):
		currentNode = self.root
		parentNode = None
		while currentNode != None:
			parentNode = currentNode
			if inputNode.val < currentNode.val:
				currentNode = currentNode.left
			else :
				currentNode = currentNode.right
		inputNode.p = parentNode
		# To check "inputNode" position
		if parentNode == None:
			self.root = inputNode
		elif inputNode.val < parentNode.val:
			parentNode.left = inputNode
		else :
			parentNode.right = inputNode
		self.Insert_Fixup(inputNode)

	def Insert_Fixup(self, currentNode):
		while currentNode.p != None and currentNode.p.color == "Red":
			if currentNode.p.p != None and currentNode.p == currentNode.p.p.left:
				uncleNode = currentNode.p.p.right
				if uncleNode != None and uncleNode.color == "Red":	# Case1
					currentNode.p.InvertColor() # "Red" => "Black"
					uncleNode.color = "Black"
					currentNode.p.p.color = "Red"
					currentNode = currentNode.p.p
				else :	# 
					if currentNode == currentNode.p.right:
						self.Left_Rotate(currentNode.p)
						currentNode = currentNode.left
					currentNode.p.color = "Black"
					currentNode.p.p.color = "Red"
					self.Right_Rotate(currentNode.p.p)
			else :
				uncleNode = currentNode.p.p.left
				if uncleNode != None and uncleNode.color == "Red":	# Case1
					currentNode.p.InvertColor() # "Red" => "Black"
					uncleNode.color = "Black"
					currentNode.p.p.color = "Red"
					currentNode = currentNode.p.p
				else :	# 
					if currentNode == currentNode.p.left:
						self.Right_Rotate(currentNode.p)
						currentNode = currentNode.right
					currentNode.p.color = "Black"
					currentNode.p.p.color = "Red"
					self.Right_Rotate(currentNode.p.p)
		self.root.color = "Black"

	def Left_Rotate(self, currentNode):
		rightNode = currentNode.right
		currentNode.right = rightNode.left
		if rightNode.left != None:
			rightNode.left.p = currentNode
		rightNode.p = currentNode.p
		if currentNode.p == None:
			self.root = rightNode
		elif currentNode == currentNode.p.left:
			currentNode.p.left = rightNode
		else :
			currentNode.p.right = rightNode
		rightNode.left = currentNode
		currentNode.p = rightNode

	def Right_Rotate(self, currentNode):
		leftNode = currentNode.left
		if leftNode == None:
			return
		currentNode.left = leftNode.right
		if leftNode.right != None:
			leftNode.right.p = currentNode
		leftNode.p = currentNode.p
		if currentNode.p == None:
			self.root = leftNode
		elif currentNode == currentNode.p.left:
			currentNode.p.left = leftNode
		else :
			currentNode.p.right = leftNode
		leftNode.right = currentNode
		currentNode.p = leftNode

	def Minimum(self, node):
		result = node
		while True:
			if result.left == None:
				return result
			result = result.left

	def FindNode(self, val):
		node = self.root
		while True:
			if node == None:
				return False
			elif node.val == val:
				return node
			elif val > node.val:
				node = node.right
			elif val < node.val:
				node = node.left
			else:
				print("ERROR")

	def DeleteVal(self, val):
		node = self.FindNode(val)
		if node:
			self.DeleteNode(node)
		else :
			print("Invalid value : " + str(val))

	def DeleteNode(self, node):
		y = node
		y_original_color = y.color
		if node.left == None:
			x = node.right
			self.Transplant(node,node.right)
		elif node.right == None:
			x = node.left
			self.Transplant(node,node.left)
		else :
			y = self.Minimum(node.right)
			y_original_color = y.color
			x = y.right
			if x != None and y.p == node :
				x.p = y
			else :
				self.Transplant(y,y.right)
				y.right = node.right
				if y.right != None:
					y.right.p = y
			self.Transplant(node,y)
			y.left = node.left
			y.left.p = y
			y.color = node.color
		if y_original_color == "Black":
			self.Delete_Fixup(x)

	def Delete_Fixup(self, node):
		if node is None:
			return
		while node is not self.root and node.color == "Black":
			if node == node.p.left:
				sibling = node.p.right
				if sibling.color == "Red":
					sibling.color = "Black"
					node.p.color = "Red"
					Left_Rotate(node.p)
					sibling = node.p.right
				if sibling.left.color == "Black" and sibling.right.color == "Black":
					sibling.color = "Red"
					node = node.p
				else :
					if sibling.right.color == "Black":
						sibling.left.color = "Black"
						sibling.color = "Red"
						Right_Rotate(sibling)
						sibling = node.p.right
					sibling.color = node.p.color
					node.p.color = "Black"
					sibling.right.color = "Black"
					Left_Rotate(node.p)
					node = self.root
			else:
				sibling = node.p.left
				if sibling.color == "Red":
					sibling.color = "Black"
					node.p.color = "Red"
					Right_Rotate(node.p)
					sibling = node.p.left
				if sibling.right.color == "Black" and sibling.left.color == "Black":
					sibling.color = "Red"
					node = node.p
				else :
					if sibling.left.color == "Black":
						sibling.right.color = "Black"
						sibling.color = "Red"
						Left_Rotate(sibling)
						sibling = node.p.left
					sibling.color = node.p.color
					node.p.color = "Black"
					sibling.left.color = "Black"
					Right_Rotate(node.p)
					node = self.root
			node.color = "Black"
	def calculate_BH():			


	def PrintInorderTraverse(self, node):
		if node.left != None:
			self.PrintInorderTraverse(node.left)
		print(node.val)
		if node.right != None:
			self.PrintInorderTraverse(node.right)

	def GetResult(self):
		total = 0
		blackNode = 0
		blackHeight = 0
		inorderList = []
		traverseStack = []
		
		# Inorder Traverse
		traverseStack.append(self.root)
		while len(traverseStack) != 0:
			# Traverse
			node = traverseStack.pop()
			if node.right != None:
				traverseStack.append(node.right)
			if node.left != None:
				traverseStack.append(node.left)
			# Add total count	
			total += 1
			# Add black node count
			if node.color == "Black":
				blackNode += 1
			# Add black height count
			## Dunno
			# Add inorder traverse
			inorderList.append(node.val)

		# Print Total
		print("total = " + str(total))
		# Print Black Node count
		print("nb = " + str(blackNode))
		# Print Black Height
		print("bh = " + str(blackHeight))
		# Print Inorder Traverse
		self.PrintInorderTraverse(self.root)
