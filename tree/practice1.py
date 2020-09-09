import sys


def preorder(node):
    if node != 0:
        print(node, end=" ")
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print(node, end=" ")
        inorder(tree[node][1])


def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=" ")


def printTree():
    for i in range(1, V + 1):
        print("%2d | %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2]))


# -------------------------------------------------------------------------
sys.stdin = open('input.txt', 'r')
V, E = map(int,input().split())
tree = [[0 for _ in range(3)] for _ in range(V + 1)]  # left, right, parent
temp = list(map(int, input().split()))

for i in range(E):
    n1 = temp[i * 2]
    n2 = temp[i * 2 + 1]
    if not tree[n1][0]:
        tree[n1][0] = n2  # left
    else:
        tree[n1][1] = n2  # right
    tree[n2][2] = n1  # parent

printTree()

print("preorder : ", end="")
preorder(1)
print()

print("inorder : ", end="")
inorder(1)
print()

print("postorder : ", end="")
postorder(1)
print()
