graph = {}
costs = {}
parents = {}
processed = []

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

if __name__ == '__main__':
    setup()
