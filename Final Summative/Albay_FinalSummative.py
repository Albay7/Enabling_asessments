class Node:
    def __init__(self, num):
        self.left = None
        self.right = None
        self.data = num

def ordr_Traversal(Root):
    if not Root:
        return []
    sequence = {}
    queue = [(Root, 0)]

    while queue:
        node, arrange = queue.pop(0)

        if arrange in sequence:
            sequence[arrange].append(node.data)
        else:
            sequence[arrange] = [node.data]

        if node.left:
            queue.append((node.left, arrange - 1))

        if node.right:
            queue.append((node.right, arrange + 1))

    sorted_arrangement = sorted(sequence.keys())

    result = []
    for range in sorted_arrangement:
        result.extend(sequence[range])

    return result

def reverse(input_list):
    front, end = 0, len(input_list) - 1

    while front < end:
        input_list[front], input_list[end] = input_list[end], input_list[front]
        front += 1
        end -= 1

    return input_list

Root = Node(1)
Root.left = Node(2)
Root.right = Node(3)
Root.left.left = Node(4)
Root.left.right = Node(5)
Root.right.left = Node(6)
Root.right.right = Node(7)
Root.right.left.right = Node(8)
Root.right.right.right = Node(9)

result = ordr_Traversal(Root)
reversed_result = reverse(result)
print("Output:", reversed_result)