from collections import deque

def solution(bridge_length, weight, truck_weights):
    time_lapse = 1
    truck_weights = deque(truck_weights)
    load = truck_weights.popleft()
    bridge = deque([0]*(bridge_length-1) + [load])
    
    while load:
        load -= bridge.popleft()
        time_lapse += 1
        x = 0
        if truck_weights and load + truck_weights[0] <= weight:
            x = truck_weights.popleft()
        bridge.append(x)
        load += x
            
    return time_lapse