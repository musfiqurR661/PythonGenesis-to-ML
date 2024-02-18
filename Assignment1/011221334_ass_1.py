adjacency_list = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('D', 2), ('G', 3)],
    'D': [('G', 2), ('A', 2)],
    'G': [('C', 4)]
}

H = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 1,
    'G': 0
}


class Node:
    def __init__(self, nodename, parent, g, h):
        self.nodename = nodename
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h


start_node = input("Enter the start node: ").upper()
end_node = input("Enter the end node: ").upper()  # .strip()

# pq
priority_queue = []


def push(node):
    priority_queue.append(node)
    priority_queue.sort(key=lambda x: x.f)


def pop():
    return priority_queue.pop(0)


def is_empty():
    return len(priority_queue) == 0


NOb = Node(nodename=start_node, parent=None, g=0, h=H[start_node])
push(NOb)

# A*
while not is_empty():
    NOb = pop()

    if NOb.nodename == end_node:
        break

    for neighbour, cost in adjacency_list[NOb.nodename]:
        new_node = Node(nodename=neighbour, parent=NOb, g=NOb.g + cost, h=H[neighbour])
        push(new_node)
    NOb = None

path = []
cost = NOb.g

while NOb.parent is not None:
    path.insert(0, NOb.nodename)
    NOb = NOb.parent
path.insert(0, start_node)

# Printing the path
print("Path:", " -> ".join(path))
print("Cost =", cost)
