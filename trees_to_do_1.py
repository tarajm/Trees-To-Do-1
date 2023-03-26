class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    

class BST:
    def __init__(self):
        self.root = None


#ADD
# Create an add(val) method on the BST object to add new value to the tree. This entails creating a 
# BTNode with this value and connecting it at the appropriate place in the tree. Unless specified otherwise, BSTs can contain duplicate values. 

def add(self,value):
    if(self.root):
        runner = self.root
        while(runner):
            if(value>runner.value):
                if(runner.right):
                    runner = runner.right
                else:
                    runner.right = Node(value)
                    return self
            else:
                if(runner.left):
                    runner = runner.left
                else:
                    runner.left = Node(value)
                    return self
    self.root = Node(value)
    return self

#Contains
# Create a contains(val) method on BST that returns whether the tree contains a given value. 
# Take advantage of the BST structure to make this a much more rapid operation than SList.contains() would be. 

def contains(self, value):
    runner = self.root
    while runner:
        if value == runner.value:
            return True
        
        if value < runner.value:
            if (not runner.left):
                return False
            runner = runner.left
        else:
            if (not runner.right):
                return False
            runner = runner.right
    return False


#Min
# Create a min() method on the BST class that returns the smallest value found in the BST. 

def min(self):
        runner = self.root
        min = self.root.value
        while runner.left:
            if runner.left.value < min:
                min = runner.left.value
            runner = runner.left
        
        return min

#Max
# Create a max() BST method that returns the largest value contained in the binary search tree. 
 def max(self):
        runner = self.root
        max = self.root.value
        while(runner.right):
            if(runner.right.value > max):
                max = runner.right.value
            
            runner = runner.right
        
        return max