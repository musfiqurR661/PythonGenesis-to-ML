import math


def listIns():
    list = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]

   #  list = [2, 1, 5, 0]
    return list


# counting inversion

def cost_calculation(state):
    countiongInversation = 0

    for i in range(len(state) - 1):
        for j in range(i + 1, len(state)):
            if state[i] > state[j]:
                countiongInversation += 1

    return countiongInversation


# generate neighbopur

def generate_neighbors(current_state):
    neighbors = []

    for i in range(len(current_state) - 1):
        new_list = current_state.copy()
        for j in range(i, len(current_state) - 1):
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
            neighbors.append(new_list.copy())
    return neighbors

#extra function for my visualization

# Define the current_state
# current_state = [2, 1, 5, 0]
current_state = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]

# Generate neighbors
neighbors = generate_neighbors(current_state)

# Print the neighbors
for neighbor in neighbors:
    print(neighbor)
# stat generation
##
    
def State_generation(current_state):
    while True:
        current_state_cost = cost_calculation(current_state)
        print("Current State :" , current_state, "Cost :", current_state_cost)
        min_next_cost = math.inf
        min_next_state = None
        for neighbor in generate_neighbors(current_state):
            next_state_cost = cost_calculation(neighbor)
            if next_state_cost < current_state_cost: #difference between
                min_next_cost = next_state_cost
                min_next_state = neighbor
                break
        if min_next_cost < current_state_cost:
            current_state = min_next_state
        else:
            print("Final State:", current_state, "Cost :", current_state_cost)
            break


def main():
    initial_state = listIns()

    State_generation(initial_state)

    print("FINISH")


if __name__ == "__main__":
    main()
