class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: Tree) -> None:
    stack = []
    temp = root
    while temp or stack:
        if temp:
            stack.append(temp)
            temp = temp.left
        else:
            temp = stack.pop()
            print(f"{temp.val} ", end="")
            temp = temp.right
    print()


def prorder(root: Tree) -> None:
    stack = []
    temp = root
    while temp or stack:
        if not temp:
            temp = stack.pop()
            temp = temp.right
        else:
            print(f"{temp.val} ", end="")
            stack.append(temp)
            temp = temp.left
    print()


def postorder(root: Tree) -> None:
    stack = []
    temp = root
    last_visited = None

    while temp or stack:
        if not temp:
            peek_node = stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                temp = peek_node.right
            else:
                last_visited = stack.pop()
                print(f"{last_visited.val} ", end="")
        else:
            stack.append(temp)
            temp = temp.left
    print()


if __name__ == "__main__":
    node7 = Tree(7)
    node6 = Tree(6)
    node5 = Tree(5)
    node4 = Tree(4)
    node3 = Tree(3, node6, node7)
    node2 = Tree(2, node4, node5)
    node1 = Tree(1, node2, node3)

    prorder(node1)
    inorder(node1)
    postorder(node1)
