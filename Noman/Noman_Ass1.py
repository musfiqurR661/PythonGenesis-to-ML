# Graph Data Structure
adjacency_list = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('D', 2), ('G', 3)],
    'D': [('G', 2), ('A', 2)],
    'G': [('C', 4)],
}

H = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 1,
    'G': 0,
}


# Node Chass
class Node:
    def _init_(self, nodename, parent, g, h):
        self.nodename = nodename
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h


priority_queue_list = []


def push_in_priority_queue(node):
    priority_queue_list.append(node)
    priority_queue_list.sort(key=lambda node: node.f)
    return


def pop_from_priority_queue():
    return priority_queue_list.pop(0)


def pathGeneration(GNode):
    print("Cost = ", GNode.g)

    path = []
    while GNode.parent is not None:
        path.insert(0, GNode)
        GNode = GNode.parent
    path.insert(0, GNode)

    firstNode = True
    for node in path:
        if firstNode:
            print("Path: ", node.nodename, end='')
            firstNode = False
        else:
            print(" -> ", node.nodename, end='')


# A* Search & Solution Finding
def AStarSearch(source, goal):
    push_in_priority_queue(Node(source, None, 0, H[source]))
    while priority_queue_list is not None:
        NOb = pop_from_priority_queue()
        if NOb.nodename == goal:
            pathGeneration(NOb)
            return

        i = 0
        while i < len(adjacency_list[NOb.nodename]):
            nodename, edge_cost = adjacency_list[NOb.nodename][i]
            push_in_priority_queue(Node(nodename, NOb, NOb.g + edge_cost, H[nodename]))
            i += 1


AStarSearch(input("Enter source node: ").upper(), input("Enter goal node: ").upper())
