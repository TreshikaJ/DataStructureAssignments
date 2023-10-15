from BST import *
def testBST(bst):
    bst.addNode(10)
    bst.addNode(20)
    bst.addNode(40)
    bst.addNode(15)
    bst.addNode(90)
    bst.addNode(70)
    bst.addNode(5)
    assert(bst.geteleCount()==7)
bst=BST()
testBST(bst)
bst.deleteNode(5)
print("Inorder")
bst.inorder()
print("Preorder")
bst.preorder()
print("Postorder")
bst.postorder()
print("Levelorder")
bst.level_order()
print("Height of tree:")
print(bst.height_tree())
print("Number of terminal nodes:")
print(bst.count_terminal())
print("Traverse_increasing:")
bst.traverse_increasing()





