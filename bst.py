# node structure of binary search tree node
class Node(object):
    left = None              # a member for representing left child of the node
    right = None            # a member for representing right child of the node
    val = -1                # the data stored in the node (representing main information attached to a node in a tree)

    # for creating each node we need to assign a data value (val) to it
    # without a data value (val) the node is invalid
    def __init__(self,val):
        self.val = val

    # 'insert' function will insert a new value at appropriate position in the tree
    # insertion is based on the binary search tree insertion rules
    def insert(self,value):
        if self is None:
            self = Node(value)
            return
        if(self.val >= value):
            if self.left is None:
                self.left = Node(value)
                return
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
                return
            else:
                self.right.insert(value)

    # deletion of a node in binary search tree
    def delete(self,value):
        #this block of method is for search the node by matching data value (val)
        if self is None:
            return
        print self.val,
        if self.val == value:
            #node found
            print "node found" ,self.val,
            if(self.left == self.right == None):
                return True
            else:
                # now the node has at least one child
                if self.left is not None:
                    #node has its left child
                    # trying to copy the right most node of this left child to current child
                    left_node = self.left
                    while (left_node.right is not None):
                        left_node = left_node.right
                    # found the node
                    self.val = left_node.val
                    # now trying to delete the right most node of left_node (recursion !!!!)
                    var = self.left.delete(self.val)
                    if var is True:
                        self.left = None
                    return False
                else:
                    # node has only right child
                    # copying the left most value of right child to the current node
                    right_node = self.right
                    while(right_node.left is not None):
                        right_node = right_node.left
                    #found the left most node
                    self.val = right_node.val
                    #now trying to delete the left most node of right_node (recursion !!!)
                    var = self.right.delete(self.val)
                    if var is True:
                        self.right = None
                    return False

        else:
            #print self.val,
            if (self.val > value):
                if self.left is not None:
                    var = self.left.delete(value)
                    if var is True:
                        self.left = None
                        return False
            else:
                if self.right is not None:
                    var = self.right.delete(value)
                    if var is True:
                        self.right = None
                        return False

        return False

    # printing tree node data values (val) in 'inorder' traversal style to check if tree is properly constructed or not
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print self.val,
        if self.right is not None:
            self.right.inorder()

    # pre order traversal of tree
    def preorder(self):
        print self.val,
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()


# Node class is for a single node
# all methods in Node class are designed in view that we can perform these operation on any node (not only root node)
# but we in general we start every operation from the root of the tree
# so defining a new class where 'root' of the tree will we kept and each operation will start from the 'root' is guarenteed

# class for handling root of the tree
class BST(object):
    root = None;    #root of the tree

    # function to operate insert operation on the tree
    def insert(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.root.insert(val)

    # function to operate inorder printing operation on the tree
    def inorder(self):
        if self.root is None:
            print ("tree is empty")
        else:
            self.root.inorder()

    # pre order traversal of binary search tree
    def preorder(self):
        if self.root is None:
            print "tree is emtpy"
        else:
            self.root.preorder()

    # deleting a value from tree
    def delete(self,value):
        if self.root is not None:
            var = self.root.delete(value)
            if var is True:
                self.root = None
        else:
            print "root is null"





x = BST()

while(True):
    var = input("enter a variable to insert into the tree else enter -1 : ")
    if(var == -1):
        break
    x.insert(var)

print "in order traversal of binary tree is\n"
x.inorder()
print "\n preorder traversal of binary tree is \n"
x.preorder()
print "\n"

# now trying to delete the nodes in tree

while(True):
    var = input("enter a value to delete from the tree : ")
    if(var == -1):
        break
    x.delete(var)
    print "\nafter deleting ",var,"\n"
    x.inorder()
    print "\n"
    x.preorder()
    print "\n"
