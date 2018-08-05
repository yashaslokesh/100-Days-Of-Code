
import sys

"""
    path[X][Y] = Z tells us that going from room number X to room number Y, 
    Z bunnies will fit in the corridor
""" 

# Read http://www.ifp.illinois.edu/~angelia/ge330fall09_maxflowl20.pdf for info

def answer(entrances, exits, path):
    
    residual_network = path[:]
    bunnies = 0
    updated = True
    
    while updated:
        
        updated = False
        for entrance in entrances:
    
            visited = set()
            flow_path = []
            current_room = entrance               
            while True:
                visited.add(current_room)      

                costs = residual_network[current_room]
                maximum = max([
                    costs[next_room]
                    for next_room in range(len(costs))
                    if next_room not in visited
                ])

                for next_room,cost in enumerate(costs):
                    if next_room not in visited and cost == maximum:
                        index = next_room
                        break

                if maximum > 0:
                    flow_path.append(current_room)
                    current_room = index
                elif flow_path:
                    current_room = flow_path.pop()
                else:
                    break

                if current_room in exits:
                    flow_path.append(current_room)

                    minimum = min([
                        residual_network [flow_path[room]] [flow_path[room + 1]]
                        for room in range(len(flow_path) - 1)
                    ])

                    if minimum != 0:

                        updated = True
                        bunnies += minimum

                        for room in range(len(flow_path) - 2):

                            residual_network [flow_path[room]] [flow_path[room + 1]] -= minimum

                            residual_network [flow_path[room + 1]] [flow_path[room]] += minimum

                        residual_network [flow_path[len(flow_path) - 2]] [flow_path[len(flow_path) - 1]] -= minimum

                    break
 
    return bunnies

print("Num bunnies",answer(
    [0,1],
    [4,5],
    [
        [0, 0, 4, 6, 0, 0], 
        [0, 0, 5, 2, 0, 0], 
        [0, 0, 0, 0, 4, 4], 
        [0, 0, 0, 0, 6, 6], 
        [0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0]
    ]))