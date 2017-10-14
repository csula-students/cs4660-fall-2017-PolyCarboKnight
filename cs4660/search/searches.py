"""
Searches module defines all different search algorithms
"""
import queue
import sys
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
    parents = {}
    visited = {}

    dfs_tracepath(graph, initial_node, visited, parents)

    path = []
    temp_node = dest_node

    while temp_node != initial_node:
        path.append(g.Edge(parents[temp_node], temp_node, graph.distance(parents[temp_node], temp_node)))
        temp_node = parents[temp_node]

    path.reverse()
    return path

def dfs_tracepath(graph, node, visited, parents):
    for neighbor in graph.neighbors(node):
        if neighbor not in visited:
            visited[neighbor] = True
            parents[neighbor] = node
            dfs_tracepath(graph, neighbor, visited, parents)

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
    distances = {initial_node: 0}
    adj_distances = {initial_node: heuristic(initial_node, dest_node)}

    parents = {}
    visited = {}

    q = queue.PriorityQueue()
    q.put((0, initial_node))

    while q:
        heap_element = q.get()
        current_node = heap_element[1]

        if current_node not in visited:
            if current_node == dest_node:
                path = []
                temp_node = dest_node
                while temp_node != initial_node:
                    path = [g.Edge(parents[temp_node], temp_node, graph.distance(parents[temp_node], temp_node))] + path
                    temp_node = parents[temp_node]
                return path
            visited[current_node] = True
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    if current_node in distances:
                        true_distance = 1 + distances[current_node]
                    else:
                        true_distance = sys.maxsize
                    parents[neighbor] = current_node
                    distances[neighbor] = true_distance
                    adj_distances[neighbor] = distances[neighbor] + heuristic(neighbor, dest_node)
                    q.put((adj_distances[neighbor], neighbor))
    return []

def heuristic(current_node, dest_node):
    dx = abs(current_node.data.x - dest_node.data.x)
    dy = abs(current_node.data.y - dest_node.data.y)

    return ((dx * dx) + (dy * dy)) ** 0.5