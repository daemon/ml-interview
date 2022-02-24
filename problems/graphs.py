from collections import defaultdict
from typing import List
import heapq


class Node:
    def __init__(self, value: str):
        self.value = value
        self.parents = set()
        self.children = dict()
    
    def add_child(self, node: 'Node'):
        self.children[node.value] = node
        node.parents.add(self.value)
    
    def remove(self):
        for v in self.children.values():
            v.parents.remove(self.value)


def alien_order(words: List[str]) -> str:
    def construct(new_words: List[str]):
        char_map = defaultdict(list)
        chars = []
        
        for x in new_words:
            if len(x) > 1:
                char_map[x[0]].append(x[1:])
            
            chars.append(x[0])            
        
        for idx in range(len(chars) - 1):
            c1 = chars[idx]
            c2 = chars[idx + 1]
            
            if c1 not in nodes:
                nodes[c1] = Node(c1)
            
            if c2 not in nodes:
                nodes[c2] = Node(c2)
            
            if c1 != c2:
                nodes[c1].add_child(nodes[c2])
        
        for v in char_map.values():
            construct(v)
        
    nodes = dict()  
    all_chars = set(''.join(words))
    construct(words)
    
    orig_node_len = len(nodes)
    sorted_list = []
    added_chars = set()
    values = iter(nodes.values())
    
    for idx1 in range(len(words)):
        for w in words[:idx1]:
            if w.startswith(words[idx1]) and len(w) > len(words[idx1]):
                return ''
    
    while True:
        try:
            node = next(values)
            
            if not node.parents:
                sorted_list.append(node.value)
                
                if node.value in added_chars:
                    return ''
                
                node.remove()
                del nodes[node.value]
                values = iter(nodes.values())
                added_chars.add(node.value)
        except StopIteration:
            break
    
    if len(sorted_list) < orig_node_len:
        return ''
    
    unused_chars = ''.join(all_chars - added_chars)
    
    return ''.join(sorted_list) + unused_chars


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

    print(alien_order(['abc', 'abd', 'tx', 'xt']))


if __name__ == '__main__':
    main()
        