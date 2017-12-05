# coding:utf-8
import time


class Node(object):

    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):

    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)

            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            elif cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.lchild)
                queue.append(cur_node.rchild)

    def aa_travel(self, node):
        if node is None:
            return
        print node.elem
        self.aa_travel(node.lchild)
        self.aa_travel(node.rchild)

    # 前序遍历
    def a_travel(self):
        if self.root is None:
            print("error")
            return

        stack = []
        cur_node = self.root

        while True:
            if cur_node is not None:
                print (cur_node.elem)

                if cur_node.rchild is not None:
                    stack.append(cur_node.rchild)

                cur_node = cur_node.lchild

            else:
                try:
                    cur_node = stack.pop()
                except:
                    print("end")

                    return

    # 中序遍历
    def b_travel(self):
        if self.root is None:
            print("error")
            return

        stack = []
        cur_node = self.root

        while True:
            if cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.lchild

            else:
                try:
                    lnode = stack.pop()
                    print(lnode.elem)
                    cur_node = lnode.rchild
                except:
                    print("end")
                    return
    #后序遍历
def c_travel(root):
    if root is None:
        return
    c_travel(root.lchild)
    c_travel(root.rchild)
    print(root.elem)



def main():
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    #  tree.aa_travel(tree.root)
    c_travel(tree.root)


if __name__ == '__main__':
    main()
