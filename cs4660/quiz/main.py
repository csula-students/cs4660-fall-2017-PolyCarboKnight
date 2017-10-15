"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!

Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9

TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import codecs

# import queue for Python 2 and 3
try:
    import Queue as queue
except ImportError:
    import queue

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.

    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response

def bfs(initial_node, dest_node):
    distances = {initial_node: 0}
    parents = {}
    route ={}
    q = queue.deque()
    q.append(initial_node)

    while q:
        current_node = q.popleft()
        neighbors = get_state(current_node)['neighbors']

        if current_node == dest_node:
            temp_node = current_node
            path = []
            while temp_node in parents:
                path.append(route[temp_node])
                temp_node = parents[temp_node]
            path.reverse()
            print_path(path, initial_node)

        for index in range(len(neighbors)):
            neighbor = neighbors[index]['id']
            if neighbor not in distances:
                distances[neighbor] = distances[current_node] + 1
                parents[neighbor] = current_node
                route[neighbor] = (transition_state(current_node, neighbor))
                q.append(neighbor)

def dijkstra_search(initial_node, dest_node):
    distances = {initial_node: 0}
    parents = {}
    route = {}
    visited = []
    q = queue.PriorityQueue()
    q.put((0, initial_node))

    while q:
        heap_element = q.get()
        current_node = heap_element[1]
        visited.append(current_node)
        neighbors = get_state(current_node)['neighbors']

        if current_node == dest_node:
            temp_node = dest_node
            path = []
            while temp_node in parents:
                value = distances[temp_node]
                path.append(route[temp_node])
                temp_node = parents[temp_node]
            path.reverse()
            print_path(path, initial_node)
            break

        for index in range(len(neighbors)):
            neighbor = neighbors[index]['id']
            edge = transition_state(current_node, neighbor)
            adj_distance = distances[current_node] - edge['event']['effect']
            if (neighbor not in distances or adj_distance < distances[neighbor]) and neighbor not in visited:
                if neighbor in distances:
                    q.get(neighbor)
                distances[neighbor] = adj_distance
                parents[neighbor] = current_node
                route[neighbor] = edge
                q.put((distances[neighbor],neighbor))

def print_path(path, current_node):
    hp = 50
    print('Starting HP: ' + str(hp))
    for index in range(len(path)):
        node = get_state(current_node)
        next_node = path[index]['id']
        hp += path[index]['event']['effect']
        print(node['location']['name'] + ": " + current_node + " to " + path[index]['action'] + ": " + path[index]['id'] + " -> " + path[index]['event']['name'] + ": " + path[index]['event']['description'], path[index]['event']['effect'])
        current_node = next_node
    print('Remaining HP: ' + str(hp))

if __name__ == "__main__":
    # Your code starts here
    empty_room = '7f3dc077574c013d98b2de8f735058b4'
    hall_way = 'f1f131f647621a4be7c71292e79613f9'

bfs(empty_room, hall_way)
print()
dijkstra_search(empty_room, hall_way)
