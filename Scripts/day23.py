import networkx as nx
import numpy as np

def get_distances(depth):
    locations = {0: (0, 0), 1: (1, 0), 2: (3, 0), 3: (5, 0), 4: (7, 0), 5: (9, 0), 6: (10, 0)}
    for c in range(4):
        for h in range(depth):
            locations[7 + c * depth + h] = (2 * c + 2, h + 1)
            
    distances = {}
    for pos_0, loc_0 in locations.items():
        for pos_1, loc_1 in locations.items():
            distances[(pos_0, pos_1)] = abs(loc_0[0] - loc_1[0]) + abs(loc_0[1] - loc_1[1])
            distances[(pos_1, pos_0)] = abs(loc_0[0] - loc_1[0]) + abs(loc_0[1] - loc_1[1])
            
    return distances

def transitions(state, position, depth, distances):
    new_states = []
    
    if state[position] == -1:
        return new_states

    elif position >= 7:
        h = (position - 7)%depth
        for pos in range(position - h, position):
            if state[pos] != -1:
                return new_states
        
        c = (position - 7)//depth
        left = np.linspace(c + 1, 0, c + 2, dtype = int)
        right = np.linspace(c + 2, 6, 5 - c, dtype = int)
        
        for pos in left:
            if state[pos] != -1:
                break
            new_state = list(state)
            new_state[pos] = state[position]
            new_state[position] = -1
            new_states.append((tuple(new_state), distances[(position, pos)] * (10 ** new_state[pos])))
            
        for pos in right:
            if state[pos] != -1:
                break
            new_state = list(state)
            new_state[pos] = state[position]
            new_state[position] = -1
            new_states.append((tuple(new_state), distances[(position, pos)] * (10 ** new_state[pos])))
            
        return new_states
    
    elif position <= 6:
        if position - state[position] in (1, 2):
            between = []
            
        elif position - state[position] > 2:
            between = range(state[position] + 2, position)
            
        elif position - state[position] <= 0:
            between = range(position + 1, state[position] + 2)
            
        for pos in between:
            if state[pos] != -1:
                return new_states
            
        col = range(7 + state[position] * depth, 7 + (state[position] + 1) * depth)
        for pos in col:
            if state[pos] not in (-1, state[position]):
                return new_states
            
        for pos in np.linspace(6 + (state[position] + 1) * depth, 7 + state[position] * depth, depth, dtype = int):
            if state[pos] == -1:
                new_state = list(state)
                new_state[pos] = state[position]
                new_state[position] = -1
                new_states.append((tuple(new_state), distances[(position, pos)] * (10 ** new_state[pos])))
                return new_states
    
def find_shortest_path(start, end, depth):
    G = nx.Graph()
    distances = get_distances(depth)
    
    processed = {start}
    to_process = {start}
    
    while to_process:
        state = to_process.pop()
        
        for position in range(7 + 4 * depth):
            new_states = transitions(state, position, depth, distances)
            
            for new_state, distance in new_states:
                G.add_node(new_state)
                G.add_edge(state, new_state, weight = distance)
                
                if new_state not in processed:
                    to_process.add(new_state)
                    processed.add(new_state)

    return nx.shortest_path_length(G, source = start, target = end, weight = "weight")
    
if __name__ == "__main__":
    start = (-1, -1, -1, -1, -1, -1, -1, 0, 1, 3, 2, 1, 0, 3, 2)
    end = (-1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3)
    print(f"Part one: {find_shortest_path(start, end, 2)}")
    
    start = (-1, -1, -1, -1, -1, -1, -1, 0, 3, 3, 1, 3, 2, 1, 2, 1, 1, 0, 0, 3, 0, 2, 2)
    end = (-1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3)
    print(f"Part one: {find_shortest_path(start, end, 4)}")
    