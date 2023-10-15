class BST:
    class Node:
        def __init__(self,ele):
            self.data=ele
            self.left=None
            self.right=None
    def __init__(self):
        self.root=None
        self.count=0
    def isEmpty(self):
        self.root==None

    def geteleCount(self):
        return self.count

    def addNode(self,ele):
        cur=parent=self.root
        if not self.isEmpty():
            while cur!=None and cur.data!=ele:
                parent=cur
                if ele<cur.data:
                    cur=cur.left
                else:
                    cur = cur.right
            if cur==None:
                new_node=self.Node(ele)
                if parent==None:
                    self.root=new_node

                elif ele<parent.data:
                    parent.left=new_node
                elif ele>parent.data:
                    parent.right=new_node

        self.count+=1
        return self.count

    def isMember(self,key):
        if not self.isEmpty():
            cur=self.root
            while cur!=None:
                if key==cur.data:
                    break
                elif key<cur.data:
                    cur=cur.left
                else:
                    cur=cur.right
            return cur!=None
        return False
    def inorder(self):
        if not self.isEmpty():
            self.__inorder__(self.root)
    def __inorder__(self,node):
        if node!=None:
            self.__inorder__(node.left)
            print(node.data)
            self.__inorder__(node.right)
    def preorder(self):
        if not self.isEmpty():
            self.__preorder__(self.root)
    def __preorder__(self,node):
        if node!=None:
            print(node.data)
            self.__preorder__(node.left)
            self.__preorder__(node.right)
    def postorder(self):
        if not self.isEmpty():
            self.__postorder__(self.root)
    def __postorder__(self,node):
        if node!=None:
            self.__postorder__(node.left)
            self.__postorder__(node.right)
            print(node.data)

    def level_order(self):
        data=[]
        data.append(self.root)
        count=0
        while data:
            cur=data.pop(0)
            print(cur.data)
            if cur.left!=None:
                data.append(cur.left)
                count+=1
            if cur.right!=None:
                data.append(cur.right)
                count+=1
            count-=1
    def height_tree(self):
        return self.__height_tree__(self.root)
    def __height_tree__(self,node):
        if node==None:
            return 0
        left_height=self.__height_tree__(node.left)
        right_height=self.__height_tree__(node.right)
        return max(left_height,right_height)+1
    def count_terminal(self):
        return self.__count_terminal__(self.root)
    def __count_terminal__(self,node):
        if node is None:
             return 0
        if node.left is None and node.right is None:
            return 1
        left_terminal=self.__count_terminal__(node.left)
        right_terminal=self.__count_terminal__(node.right)
        return left_terminal+right_terminal
    def deleteNode(self,key):
        return self.__deleteNode__(self.root,key)
    def __deleteNode__(self,node,key):
        if node==None:
            return None
        elif key<node.data:
            node.left=self.__deleteNode__(node.left,key)
        elif key>node.data:
            node.right=self.__deleteNode__(node.right,key)
        elif node.left and node.right:
            temp=self.__findMin__(node.right)
            node.data=temp.data
            node.right=self.__deleteNode__(node.right,temp.data)
        else:
            if node.left==None:
                node=node.right
            elif node.right==None:
                node=node.left
            self.count-=1
            return node
    def __findMin__(self,node):
        if node.left==None:
            return node
        else:
            return(self.__findMin__(node.left))
    def traverse_increasing(self):
        return self.__traverse_increasing__(self.root)
    def __traverse_increasing__(self,node):
        if node!=None:
            self.__traverse_increasing__(node.right)
            print(node.data)
            self.__traverse_increasing__(node.left)