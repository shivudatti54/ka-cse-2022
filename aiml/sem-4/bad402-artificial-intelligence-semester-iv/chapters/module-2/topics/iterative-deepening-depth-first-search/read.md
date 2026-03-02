function IDDFS(root):
    for depth from 0 to infinity:
        result = DLS(root, depth)
        if result != cutoff, return result

function DLS(node, depth): // Depth-Limited Search
    if node is goal:
        return node
    else if depth == 0:
        return cutoff  // Signifies that deeper search is needed
    else:
        cutoff_occurred = false
        for each child in expand(node):
            result = DLS(child, depth-1)
            if result == cutoff:
                cutoff_occurred = true
            else if result != failure:
                return result
        return cutoff if cutoff_occurred, else failure