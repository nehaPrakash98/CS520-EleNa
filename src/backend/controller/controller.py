from src.backend.algorithm.astar import AStar
from src.backend.algorithm.dijkstra import Dijkstra
from src.backend.algorithm.bfs import BFS
from src.backend.utils.map_utils import convert_path, get_node_from_address
import osmnx as ox
import logging

"""
Controller class
 - Handles the requests received by the server
 - Has-a model object
"""


class Controller(object):

    def _init_(self):
        self.model = None

    def set_model(self, model):
        self.model = model

    def get_route(self, graph, source_node, dest_node, algorithm='AStar', limit=0, mode='min', plot_local=0):
        """
        Calls the appropriate methods (based on algorithm) to get the route
        :param graph: graph object
        :param source_node: node id of source
        :param dest_node: node id of dest
        :param algorithm: preferred algorithm
        :param limit: limit
        :param mode: mode
        :param plot_local: whether to plot locally
        :return: final route information
        """
        path = ""
        if algorithm == 'AStar':
            astar = AStar()
            path = astar.astar(graph, source_node, dest_node, limit, mode)

        elif algorithm == 'Dijkstra':
            dijkstra = Dijkstra()
            path = dijkstra.dijkstra(graph, source_node, dest_node, limit, mode)

        elif algorithm == 'BFS':
            bfs = BFS()
            path = bfs.bfs(graph, source_node, dest_node, limit, mode)

        final_path, path_data = convert_path(graph, path)

        # Plot the local graph - for local debugging
        if plot_local == 1:
            logging.info("Plotting Graph")
            ox.plot_graph_route(graph, path)

        return {'path': final_path, 'path_data': path_data}

    def handle_request(self, graph, plot_local=0):
        """
        Handle requests received from the server
        :param graph: graph object
        :param plot_local: whether to plot the map locally
        :return: final route information
        """
        # Get nodes from graph that are nearest to the given source and destination
        source_node = get_node_from_address(graph, self.model.get_source())
        dest_node = get_node_from_address(graph, self.model.get_destination())

        # Get route
        return self.get_route(graph, source_node, dest_node,
                              self.model.get_algorithm(),
                              self.model.get_limit(),
                              self.model.get_mode(), plot_local)
