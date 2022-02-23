class Tree(object):
    x = 0
    l = None
    r = None

def solution(T: Tree):
    return find_visible(T)


def find_visible(root, S = 0):
    count = 0
    if root.x > S:
        count += 1

    if (root.left):
        count += find_visible(root.l, S + root.x)

    if (root.right):
        count += find_visible(root.r, S + root.x)
    return count