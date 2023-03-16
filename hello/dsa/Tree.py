class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(root):
        stack = []
        temp = root

        while temp or stack:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(f"{temp.val} ",end="")
                temp = temp.right
        print()


    def prorder(root):
        stack = []
        temp = root

        while temp or stack:
            if temp:
                print(f"{temp.val} ",end = "")
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                temp = temp.right
        print()
#TODO: postorder
    def postorder(root):
        stack = []
        temp = root

        while temp or stack:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                temp = temp.right
                print(f"{temp.val} ", end="")

        print()


if __name__ == "__main__":
    node7 = Tree(7)
    node6 = Tree(6)
    node5 = Tree(5)
    node4 = Tree(4)
    node3 = Tree(3, node6, node7)
    node2 = Tree(2, node4, node5)
    root = Tree(1, node2, node3)

    Solution.prorder(root)
    Solution.inorder(root)
    Solution.postorder(root)
