class AANode:
    def __init__(self, value: float, level: int = 1, parent: 'AANode' = None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.level = level
    
    @property
    def is_root(self):
        return self.parent is None
    
    def skew(self) -> 'AANode':
        r"""Check the right-horizontal-only invariant. Perform the skew operation if the
        invariant is violated.

        Examples:
            .. code-block:: none

                      \                 \
                  1 <- 2                 1 -> 2
                 / \    \    becomes    /    / \
                3   4    5             3    4   5
        """
        if self.left is None or self.left.level != self.level:
            return self
        
        self.left.parent = self.parent
        
        if not self.is_root:
            if self == self.parent.right:
                self.parent.right = self.left
            else:
                self.parent.left = self.left
            
        self.parent = self.left
        self.left = self.left.right

        return self.parent


    def split(self) -> 'AANode':
        r"""Check the grandchild level invariant. Perform the split operation if the
        invariant is violated. Increment the level of the right child.

        Examples:
            .. code-block:: none
            
                 \                                \
                  1 -> 2 -> 3                      2 -> 3
                 /    /    / \     becomes        /    / \
                4    5    6   7                  1    6   7
                                                / \
                                               4   5
        """
        if self.right and self.right.right:
            if self.level != self.right.level or self.level != self.right.right.level:
                return self
        else:
            return self

        self.right.parent = self.parent
        old_right_left = self.right.left
        self.right.left = self

        if not self.is_root:
            if self == self.parent.right:
                self.parent.right = self.right
            else:
                self.parent.left = self.right
        
        self.parent = self.right
        self.right = old_right_left
        self.parent.level += 1

        return self.parent
    
    def compute_level(self) -> int:
        left_level = 0
        right_level = 0

        if self.left:
            left_level = self.left.compute_level()
        if self.right:
            right_level = self.right.compute_level()
        
        return 1 + max(left_level, right_level)

    def insert(self, value: float) -> 'AANode':
        if value <= self.value:
            if self.left is None:
                self.left = AANode(value, parent=self)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = AANode(value, parent=self)
            else:
                self.right.insert(value)
        
        self.skew()

        return self.split()
    
    def __str__(self) -> str:
        self_str = f'{self.left.value if self.left else ""} <- {self.value} -> {self.right.value if self.right else ""}'
        
        if self.left:
            self_str += '\n' + str(self.left)
        if self.right:
            self_str += '\n' + str(self.right)
        
        return self_str


class AATree:
    """The simplest self-balancing binary search tree. It reduces to a red-black
    tree where only the right nodes can be red, while maintaining some other invariants.
    """

    def __init__(self):
        self.root = None

    def insert(self, value: float):
        if self.root is None:
            self.root = AANode(value)
        else:
            new_node = self.root.insert(value)

            if new_node.is_root:
                self.root = new_node
    
    def compute_level(self) -> int:
        if self.root:
            return self.root.compute_level()

        return 0
    
    def __str__(self):
        return str(self.root)
        

def main():
    tree = AATree()

    for num in list(range(100)):
        tree.insert(num)
    
    print(tree.compute_level())


if __name__ == '__main__':
    main()
