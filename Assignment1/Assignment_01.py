class Node:
    def __init__(self, nodename, parent, g, h):
        self.nodename = nodename
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h


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

# Take input for start and end nodes
start_node = input("Enter the start node: ").strip().upper()
end_node = input("Enter the end node: ").strip().upper()

# Initialize the priority queue with the start node
priority_queue = []
NOb = Node(nodename=start_node, parent=None, g=0, h=H[start_node])
priority_queue.append(NOb)


def get_priority(obj):
    return obj.f


# A* search algorithm
while priority_queue:

    NOb = min(priority_queue, key=get_priority)
    priority_queue.remove(NOb)

    if NOb.nodename == end_node:
        break

    for neighbor, cost in adjacency_list[NOb.nodename]:
        new_node = Node(nodename=neighbor, parent=NOb, g=NOb.g + cost, h=H[neighbor], f=NOb.g + cost + H[neighbor])
        priority_queue.append(new_node)

# Path generation
path = []
cost = NOb.g
while NOb.parent is not None:
    path.insert(0, NOb.nodename)
    NOb = NOb.parent
path.insert(0, start_node)

# Print the path and cost
print("Path:", path)
print("Cost:", cost)
