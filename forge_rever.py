class Tree(object):
    x = 0
    l = None
    r = None


def traverse(sub_tree, height):
    left_height = 0
    right_height = 0

    if sub_tree.l:
        left_height = traverse(sub_tree.l, height + 1)
    if sub_tree.r:
        right_height = traverse(sub_tree.r, height + 1)

    if sub_tree.l or sub_tree.r:
        return max(left_height, right_height)
    else:
        return height

def solution(T):
    # write your code in Python 3.6
    return traverse(T, 0)
