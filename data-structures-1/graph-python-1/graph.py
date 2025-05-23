from functools import wraps
import time

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time - start_time:.10f} seconds")
        return result
    return wrapper

class Graph:
    @time_it
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict: ", self.graph_dict)

    def get_paths(self, start, end, path =[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    path.append(p)
        return paths
    
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        shortest_paths = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_paths(node, end, path)  
                if sp:
                    if not shortest_paths or len(sp) < len(shortest_paths):
                        shortest_paths = [sp]
        return shortest_paths

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    Graph = Graph(routes)

    start = "Mumbai"
    end = "New York"
    print(f"Shortest Path between {start} and {end} : ", Graph.get_shortest_path(start, end))