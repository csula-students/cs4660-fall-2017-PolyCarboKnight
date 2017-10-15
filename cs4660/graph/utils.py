"""
utils package is for some quick utility methods

such as parsing
"""

class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.symbol)

from .graph import Node
from .graph import Edge

def parse_grid_file(graph, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph

    Returns graph object
    """
    with open(file_path) as file:
        lines = file.readlines()
        maze = []
        for line in lines:
            if len(line) > 0:
                maze.append([line[i:i + 2] for i in range(1, len(line[1:-1]), 2)])
        maze = maze[1:-1]

    nodes = {}

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            node = Tile(x, y, maze[y][x])
            graph.add_node(Node(node))
            nodes[(x, y)] = node

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            current_node = Tile(x, y, maze[y][x])

            if current_node.symbol != "##":
                if (x + 1, y) in nodes:
                    graph.add_edge(Edge(Node(current_node), Node(nodes[(x + 1, y)]), 1))
                if (x - 1, y) in nodes:
                    graph.add_edge(Edge(Node(current_node), Node(nodes[(x - 1, y)]), 1))
                if (x, y + 1) in nodes:
                    graph.add_edge(Edge(Node(current_node), Node(nodes[(x, y + 1)]), 1))
                if (x, y - 1) in nodes:
                    graph.add_edge(Edge(Node(current_node), Node(nodes[(x, y - 1)]), 1))

    return graph


def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile

    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """
    route = ''

    if not edges:
        return ''

    for edge in edges:
        if edge.from_node.data.x > edge.to_node.data.x:
            route += 'W'
        elif edge.from_node.data.x < edge.to_node.data.x:
            route += 'E'
        elif edge.from_node.data.y > edge.to_node.data.y:
            route += 'N'
        elif edge.from_node.data.y < edge.to_node.data.y:
            route += 'S'

    return route
