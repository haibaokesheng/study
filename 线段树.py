
max_len = 1000
arr = [1, 3, 5, 7, 9, 11]
size = len(arr)
tree = [0]*size

def build_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = start+(end-start)//2
        left_node = 2*node+1
        right_node = 2*node+2
        build_tree(arr, tree, left_node, start, mid)
        build_tree(arr, tree, right_node, mid+1, end)
        tree[node] = tree[left_node]+tree[right_node]

build_tree(arr,tree,0,0,size-1)