from typing import List
import heapq


def num_buses_to_destination(routes: List[List[int]], source: int, target: int) -> int:
    if target == source:
        return 0

    adj_matrix = [[0] * len(routes) for _ in range(len(routes))]
    routes = [set(x) for x in routes]

    for idx1 in range(len(routes)):
        for idx2 in range(idx1 + 1, len(routes)):
            intersects = int(bool(routes[idx1].intersection(routes[idx2])))
            adj_matrix[idx1][idx2] = intersects
            adj_matrix[idx2][idx1] = intersects

    open_set = [(1, route_idx) for route_idx, route in enumerate(routes) if source in route]
    visited_set = set()
    target_set = set([route_idx for route_idx, route in enumerate(routes) if target in route])

    while open_set:
        cost, route_idx = heapq.heappop(open_set)

        if route_idx in target_set:
            return cost

        for neighbor_idx, present in enumerate(adj_matrix[route_idx]):
            if present and neighbor_idx not in visited_set:
                heapq.heappush(open_set, (cost + 1, neighbor_idx))
        
        if route_idx not in visited_set:
            visited_set.add(route_idx)
    
    return -1


def main():
    routes = [[1, 2, 3], [3, 5, 6]]
    print(num_buses_to_destination(routes, 1, 6))


if __name__ == '__main__':
    main()
        