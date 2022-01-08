import logging
import os

import osmnx as ox
import pickle as pkl

"""
Map related utils 
Used all through the project
"""


def get_coordinates(address):
    """
    Get lat, long of address supplied
    :param address: Addrress of location
    :return: Geocodes (lat, lng)
    """
    return ox.geocode(address)


def get_map(city, state, country, api_key, file_name):
    """
    Saves the map of a particular city
    :param city: City for the map
    :param state: State
    :param country: Country
    :param api_key:  Google API Key
    :param file_name: Path to save the pickle file
    """

    # Change to correct directory
    print(os.getcwd())
    os.chdir("backend")

    # Downloading local map
    query = {'city': city, 'state': state, 'country': country}
    graph_orig = ox.graph_from_place(query, network_type='drive')

    # adding elevation data from GoogleMaps
    graph_orig = ox.add_node_elevations_google(graph_orig, api_key=api_key)
    graph_orig = ox.add_edge_grades(graph_orig)

    # saving the pickle file
    pkl.dump(graph_orig, open(file_name, "wb"))


def load_map(filepath, changeDir=0):
    """
    Loads the map at the supplied filepath
    :param filepath: path to pickle map file
    :param changeDir: boolean to decide whether we change directory
    :return: graph object
    """
    print(os.getcwd())
    # if changeDir == 1:
    #     os.chdir("src/backend")

    with open(filepath, 'rb') as infile:
        graph_orig = pkl.load(infile)
        return graph_orig


def get_node_from_address(graph, address):
    """
    Gets the node nearest to the supplied address
    :param graph: graph object
    :param address: address
    :return: nearest node id
    """
    try:
        lat, lng = get_coordinates(address)
        node, dist = ox.nearest_nodes(graph, lng, lat, return_dist=True)
        if dist / 10000 > 10000:
            logging.error("The given address is out of bounds")
            raise Exception("{} is not currently included in Routing Capabilities".format(address))
        return node
    except:
        logging.error("The given location cannot be found")
        raise Exception("Could not find location '{}'".format(address))


def convert_path(graph, path):
    """
    Converts path to final output
    :param graph: graph object
    :param path: final route path
    :return: final path with node ids of all nodes in the along with other info
    """
    final_path = []
    lengths_and_elevations = []

    next_node = None
    for i in range(len(path) - 1):
        node_id = path[i]
        next_node = path[i + 1]
        x = graph.nodes[node_id]['x']
        y = graph.nodes[node_id]['y']
        elevation = graph.nodes[node_id]['elevation']
        edge = graph[node_id][next_node][0]
        length = 0

        if 'length' in edge:
            length = edge['length']
        grade = 0
        if 'grade' in edge:
            grade = max(0, edge['grade'])
        final_path.append((x, y))
        lengths_and_elevations.append({'length': length, 'elevation': elevation, 'grade': grade})

    # Add Last Node
    if next_node is None:
        logging.error("Route cannot be found for the given source and destination")
        raise Exception("Unable to find a route")

    last_node = graph.nodes[next_node]
    final_path.append((last_node['x'], last_node['y']))
    lengths_and_elevations.append({'length': 0, 'elevation': last_node['elevation']})
    return final_path, lengths_and_elevations
