"""
Searches module defines all different search algorithms
"""
import queue
from graph import graph as g

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    distances = {initial_node: 0}
    parents = {}
    q = queue.deque()
    q.append(initial_node)

    while q:
        current_node = q.popleft()

        if current_node == dest_node:
            temp_node = dest_node
            path = []
            while temp_node in parents:
                value = distances[temp_node]
                path.append(g.Edge(parents[temp_node], temp_node, value))
                temp_node = parents[temp_node]
            path.reverse()
            return path

        for neighbor in graph.neighbors(current_node):
            if neighbor not in distances:
                distances[neighbor] = graph.distance(current_node, neighbor)
                parents[neighbor] = current_node
                q.append(neighbor)

def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    distances = {initial_node: 0}
    parents = {}
    q = queue.PriorityQueue()
    q.put((0, initial_node))

    while q:
        heap_element = q.get()
        current_node = heap_element[1]

        if current_node == dest_node:
            temp_node = dest_node
            path = []
            while temp_node in parents:
                value = distances[temp_node]
                path.append(g.Edge(parents[temp_node], temp_node, value))
                temp_node = parents[temp_node]
            path.reverse()
            return path

        for neighbor in graph.neighbors(current_node):
            adj_distance = distances[current_node] + graph.distance(current_node, neighbor)
            if neighbor not in distances or adj_distance < distances[neighbor]:
                distances[neighbor] = graph.distance(current_node, neighbor)
                parents[neighbor] = current_node
                q.put((distances[neighbor],neighbor))

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass
