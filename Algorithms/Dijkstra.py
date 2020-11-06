'''
• Breadth-first search is used to calculate the shortest path for
an unweighted graph.
• Dijkstra’s algorithm is used to calculate the shortest path for
a weighted graph.
• Dijkstra’s algorithm works when all the weights are positive.
• If you have negative weights, use the Bellman-Ford algorithm

'''


graph = {}
costs = {}
parents = {}
processed = []

def print_shortest_path(start, fin):
    path = []
    path.append(fin)
    n = fin
    while parents[n] != start and parents[n] != None:
        path.append(parents[n])
        n = parents[n]
    path.append(start)
    path = path[::-1]
    return "-".join(path)

def find_lowest_cost_nodes():
    lowest_cost = float("inf")
    lowest_cost_node = None
    for n in costs.keys():
        if costs[n] < lowest_cost and n not in processed:
            lowest_cost = costs[n]
            lowest_cost_node = n
    return lowest_cost_node

def dijkstras():
    node = find_lowest_cost_nodes()
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if new_cost < costs[n]:
                costs[n]   = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_nodes()

def setup():
    graph["start"] = {}
    graph["start"]["A"] = 6
    graph["start"]["B"] = 2
    graph["A"] = {}
    graph["A"]["Fin"] = 1
    graph["B"] = {}
    graph["B"]["A"] = 3
    graph["B"]["Fin"] = 5
    graph["Fin"] = {}

    costs["A"] = 6
    costs["B"] = 2
    costs["Fin"] = float("inf")

    parents["A"] = "start"
    parents["B"] = "start"
    parents["Fin"] = None

def setup2():
    graph["start"] = {}
    graph["start"]["A"] = 5
    graph["start"]["B"] = 2
    graph["A"] = {}
    graph["A"]["C"] = 4
    graph["A"]["D"] = 2
    graph["B"] = {}
    graph["B"]["A"] = 8
    graph["B"]["D"] = 7
    graph["C"] = {}
    graph["C"]["D"] = 6
    graph["C"]["Fin"] = 3
    graph["D"] = {}
    graph["D"]["Fin"] = 1
    graph["Fin"] = {}

    costs["start"] = 0
    costs["A"] = 5
    costs["B"] = 2
    costs["C"] = float("inf")
    costs["D"] = float("inf")
    costs["Fin"] = float("inf")

    parents["A"] = "start"
    parents["B"] = "start"
    parents["C"] = None
    parents["D"] = None
    parents["Fin"] = None

def setup3():
    graph["start"] = {}
    graph["start"]["A"] = 10
    graph["A"] = {}
    graph["A"]["C"] = 20
    graph["B"] = {}
    graph["B"]["A"] = 1
    graph["C"] = {}
    graph["C"]["B"] = 1
    graph["C"]["Fin"] = 30
    graph["Fin"] = {}

    costs["start"] = 0
    costs["A"] = 10
    costs["B"] = float("inf")
    costs["C"] = float("inf")
    costs["Fin"] = float("inf")

    parents["A"] = "start"
    parents["B"] = None
    parents["C"] = None
    parents["Fin"] = None

def setup4():
    graph["start"] = {}
    graph["start"]["A"] = 2
    graph["start"]["B"] = 2
    graph["A"] = {}
    graph["A"]["C"] = 2
    graph["A"]["Fin"] = 2
    graph["B"] = {}
    graph["B"]["A"] = 2
    graph["C"] = {}
    graph["C"]["B"] = -1
    graph["C"]["Fin"] = 2
    graph["Fin"] = {}

    costs["start"] = 0
    costs["A"] = 2
    costs["B"] = 2
    costs["C"] = float("inf")
    costs["Fin"] = float("inf")

    parents["A"] = "start"
    parents["B"] = "start"
    parents["C"] = None
    parents["Fin"] = None

if __name__ == '__main__':
    setup()
    dijkstras()
    print("Weights of the shortest path is: ", costs["Fin"])
    print("Shortest path is: ", print_shortest_path("start", "Fin"))

    processed = []
    graph = {}
    costs = {}
    parents = {}
    setup2()
    dijkstras()
    print("Weights of the shortest path is: ", costs["Fin"])
    print("Shortest path is: ", print_shortest_path("start", "Fin"))

    processed = []
    graph = {}
    costs = {}
    parents = {}
    setup3()
    dijkstras()
    print("Weights of the shortest path is: ", costs["Fin"])
    print("Shortest path is: ", print_shortest_path("start", "Fin"))

    processed = []
    graph = {}
    costs = {}
    parents = {}
    setup4()
    dijkstras()
    print("Weights of the shortest path is: ", costs["Fin"])
    print("Shortest path is: ", print_shortest_path("start", "Fin"))

