"""
Graph related utils methods
Used throughout the project
"""


def shortest_path_optimizer(graph, weight='length'):
    """
    Returns the right shortest path optimizer
    :param graph: Graph object
    :param weight: Weight used to decide optimizer
    :return: optimizer function
    """
    if weight == 'length':
        def weight_(source, dest, edge_data):
            return min(attr.get(weight, 1) for attr in edge_data.values())

    elif weight == 'grade':
        def weight_(source, dest, edge_data):
            try:
                return max(0, edge_data['grade'])
            except:
                return 0
    elif weight == 'elevation_change':
        def weight_(source, dest, edge_data):
            try:
                elevation_diff = graph.nodes[dest]['elevation'] - graph.nodes[source]['elevation']
                return max(elevation_diff, 0)
            except:
                print("elevation not found: ", source, dest)
                return 0
    else:
        def weight_(source, dest, edge_data):
            return min(attr.get(weight, 1) for attr in edge_data.values())

    return weight_


def get_path_length(graph, path):
    """
    Returns path length
    :param graph: Graph obj
    :param path: Path
    :return: Length of path
    """
    length = 0
    for i in range(len(path) - 1):
        length += graph[path[i]][path[i + 1]][0]['length']
    return length


def get_path_elevation(graph, path):
    """
    Returns path elevation
    :param graph: Graph obj
    :param path: Path
    :return: Elevation of path
    """
    elevation = 0
    for i in range(len(path) - 1):
        elevation += max(0, graph.nodes[path[i + 1]]['elevation'] - graph.nodes[path[i]]['elevation'])
    return elevation


def get_l1_distance(graph, start, goal):
    """
    Return the Manhattan distance
    :param graph: Graph obj
    :param start: Start
    :param goal: Goal
    :return: L1 or Manhattan distance
    """
    amherst_graph = graph
    start_x, start_y = amherst_graph.nodes[start]['x'], amherst_graph.nodes[start]['y']
    end_x, end_y = amherst_graph.nodes[goal]['x'], amherst_graph.nodes[goal]['y']

    return ((end_x - start_x) ** 2 + (end_y - start_y) ** 2) ** 0.5
