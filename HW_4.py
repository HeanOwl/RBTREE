import RB_Tree

def PrintTree(node, height):
	if node.right != None:
		PrintTree(node.right, height + 1)
	print("  " * height + str(node.val))
	if node.left != None:
		PrintTree(node.left, height + 1)

tree = RB_Tree.RB_Tree()
f = open("input.txt", 'r')
lines = f.readlines()
for line in lines:
	value = int(line)
	if value > 0 :
		tree.Insert_Value(value)
	elif value < 0 :
		print("Not implemented")
		#tree.DeleteVal(-value)
	else: 
		tree.GetResult()
		break;
f.close()

PrintTree(tree.root,0)