"""
This is an implementation of Dijkstra's algorithm in Python 3.

Usage:
$ python3 dijkstra.py < graph.txt
Distances: {'A': (0, 'A'), 'B': (2, 'A'), 'C': (3, 'B'), 'D': (5, 'C'), 'E': (7, 'D')}
Shortest paths: {'A': (0, 1), 'B': (2, 1), 'C': (3, 1), 'D': (5, 1), 'E': (7, 1)}

graph.txt
A B 2
A C 3
B C 1
B D 4
C D 2
C E 5
D E 1
"""

import sys


def dijkstra(graph, start, end):
    """
    Find the shortest path from start to end in graph.
    """
    # A dictionary of the form {node: (distance, previous node)}
    distances = {}
    # A dictionary of the form {node: (distance, count)}
    # where count is the number of shortest paths to the node.
    paths = {start: (0, 1)}
    # A list of the form [(distance, count, node), ...]
    queue = [(0, 1, start)]
    while queue:
        print("----")
        print("Queue:", queue)
        print("Distances:", distances)
        print("Paths:", paths)
        queue.sort()
        (dist, _, v1) = queue.pop(0)
        if v1 in distances:
            continue
        print("Visiting:", v1)
        print("Distance:", dist)
        print("Distances:", distances)
        distances[v1] = (dist, v1)
        if v1 == end:
            break
        # Update the distances to the neighbors of v1.
        for v2 in graph[v1]:
            print("--")
            print("Checking:", v2)
            if v2 in distances:
                continue
            # The distance to v2 is the distance to v1 plus the distance
            new_dist = dist + graph[v1][v2]
            new_paths = paths[v1][1]
            print("New distance:", new_dist)
            print("New paths:", new_paths)
            queue.append((new_dist, new_paths, v2))
            if v2 not in paths:
                paths[v2] = (new_dist, new_paths)
            elif new_dist < paths[v2][0]:
                paths[v2] = (new_dist, new_paths)
            elif new_dist == paths[v2][0]:
                # There are multiple shortest paths to v2.
                # Add the number of shortest paths to v1 to the number
                # of shortest paths to v2.
                # Note that the number of shortest paths to v1 is
                # paths[v1][1].
                # The number of shortest paths to v2 is paths[v2][1].
                paths[v2] = (new_dist, paths[v2][1] + new_paths)
            print("Queue:", queue)
            print("Distances:", distances)
            print("Paths:", paths)
    return distances, paths


def main():
    """
    Read a graph from stdin and print the shortest paths.
    """
    graph = {}
    for line in sys.stdin:
        (v1, v2, dist) = line.split()
        dist = int(dist)
        if v1 not in graph:
            graph[v1] = {}
        graph[v1][v2] = dist
        if v2 not in graph:
            graph[v2] = {}
        graph[v2][v1] = dist
    print("Graph: {}".format(graph))
    (distances, paths) = dijkstra(graph, "A", "E")
    print("Distances:", distances)
    print("Shortest paths:", paths)


if __name__ == "__main__":
    main()

# -------

# This is an implementation of Dijkstra's algorithm in Python 3 heapq.
# It is a single-source shortest path algorithm that finds the shortest
# path from a source node to all other nodes in a weighted graph.
# The algorithm is based on the idea of greedily choosing the next
# closest node at each step. It is a weighted graph, so each edge
# has a weight associated with it. The algorithm works by maintaining
# two sets: a set of nodes already visited and a set of nodes not yet
# visited. At each step, the algorithm finds the unvisited node that
# is closest to the source node, and marks it as visited. It then
# updates the distances to all of its neighbors. The algorithm stops
# when all nodes have been visited.
# The time complexity of the algorithm is O(V^2), where V is the
# number of vertices. The space complexity is O(V), since we need
# to store the distances to all the vertices.
# The algorithm can be improved by using a priority queue instead
# of a set to store the unvisited nodes. The priority queue will
# always return the node with the smallest distance. The time
# complexity of the algorithm is then O(E log V), where E is the
# number of edges. The space complexity is still O(V).
# The algorithm can also be improved by using a min heap instead
# of a priority queue. The time complexity of the algorithm is then
# O(E + V log V), where E is the number of edges. The space
# complexity is still O(V).

# code to demonstrate working of Dijkstra's Algorithm using O(v^2) approach for finding minimum distance
# between two vertices


def dijkstra(graph, src, dest):
    # This function returns the shortest distance between src and dest in O(v^2)
    # time complexity
    # graph is a dictionary of the form {node: {neighbour: distance}}
    # src is the source node
    # dest is the destination node
    # The function returns the shortest distance between src and dest
    # and the shortest path between src and dest

    # If src and dest are the same node
    if src == dest:
        return 0, [src]

    # If src and dest are not connected
    if src not in graph or dest not in graph:
        return None, None

    # If src and dest are connected
    # Initialize the distance to infinity
    distance = {}
    for node in graph:
        distance[node] = float("inf")
    # The distance to the source node is 0
    distance[src] = 0

    # Initialize the previous node to None
    previous = {}
    for node in graph:
        previous[node] = None

    # Initialize the unvisited nodes to all the nodes
    unvisited = set(graph)

    # While there are unvisited nodes
    while unvisited:

        # Find the unvisited node with the smallest distance
        min_distance = float("inf")
        for node in unvisited:
            if distance[node] < min_distance:
                min_distance = distance[node]
                current = node

        # If the smallest distance is infinity, then the nodes are not connected
        if min_distance == float("inf"):
            return None, None

        # Remove the current node from the unvisited nodes
        unvisited.remove(current)

        # For each neighbour of the current node
        for neighbour in graph[current]:

            # If the neighbour is unvisited
            if neighbour in unvisited:

                # Calculate the distance to the neighbour
                new_distance = distance[current] + graph[current][neighbour]

                # If the distance to the neighbour is smaller than the current
                # distance to the neighbour
                if new_distance < distance[neighbour]:

                    # Update the distance to the neighbour
                    distance[neighbour] = new_distance

                    # Update the previous node of the neighbour
                    previous[neighbour] = current


# Driver code
if __name__ == "__main__":
    graph = {
        "A": {"B": 10, "C": 3},
        "B": {"C": 1, "D": 2},
        "C": {"B": 4, "D": 8, "E": 2},
        "D": {"E": 7},
        "E": {"D": 9},
    }
    print(dijkstra(graph, "A", "E"))

# code to demonstrate working of Dijkstra's Algorithm using O(E log V) approach for finding minimum distance
# between two vertices


def dijkstra(graph, src, dest):
    # This function calculates the shortest path from src to dest in O(E log V)
    dist = [float("Inf")] * len(graph)
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist[dest]


# code to demonstrate working of Dijkstra's Algorithm using O(E + V log V) approach for finding minimum distance
# between two vertices

import heapq
import sys


def dijkstra(graph, start, end):
    """
    Find the shortest path from the start node to all nodes
    in the graph.
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return distances[end]


def main():
    """
    Read a graph from stdin and print the shortest paths.
    """
    graph = {}
    for line in sys.stdin:
        (v1, v2, dist) = line.split()
        dist = int(dist)
        if v1 not in graph:
            graph[v1] = {}
        graph[v1][v2] = dist
        if v2 not in graph:
            graph[v2] = {}
        graph[v2][v1] = dist
    print("Graph: {}".format(graph))
    distances = dijkstra(graph, "A", "E")
    print("Distances:", distances)


if __name__ == "__main__":
    main()
