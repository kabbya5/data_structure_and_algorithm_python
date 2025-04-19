import heapq 

class WeightedGraph:
    def __init__(self):
        self.graph = {} 

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
        
    def add_edge(self, from_node, to_node, weight):
        self.add_node(from_node)
        self.add_node(to_node)

        self.graph[from_node].append((to_node, weight))

    def dijkstra(self, start):
        distances = {node:float('inf') for node in self.graph}
        distances[start] = 0 

        pq = [(0, start)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)
            if current_distance > distances[current_node]:
                continue 

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight 
                if distance < distances[neighbor]:
                    distances[neighbor] = distance 
                    heapq.heappush(pq,(distance, neighbor))

        return distances 
    
g = WeightedGraph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)

start_node = 'A'
shortest_paths = g.dijkstra(start_node)

print(f"Shortest paths from node {start_node}:")
for node, distance in shortest_paths.items():
    print(f" - to {node}: {distance}")
