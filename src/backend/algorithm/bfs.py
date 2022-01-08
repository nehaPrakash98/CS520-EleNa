from src.backend.algorithm.algorithm import Algorithm
import logging

"""
To get the shortest path using the BFS Algorithm
"""

class BFS(Algorithm):
    def get_shortest_path(self, graph, start_node, dest_node, edge_weight='length'):
        """
        Get the vanilla shortest path
        :param graph: Graph obj
        :param start_node: node id of source
        :param dest_node: node id of dest
        :param edge_weight: weight measure
        :return: Vanilla shortest path
        """
        explored = []

        # start the BFS queue
        queue = [[start_node]]

        # return if start node is the end node
        if start_node == dest_node:
            return [dest_node]

        # keeps looping until all possible paths have been checked
        while queue:
            path = queue.pop(0)
            node = path[-1]
            # add neighboring nodes if they haven't been explored
            if node not in graph:
                logging.error("Start node is not in the map. Please restart with the correct start node")
                raise Exception("Start node is not in the map. Please restart with the correct start node")

            if node not in explored:
                neighbors = graph.neighbors(node)
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if neighbor == dest_node:
                        return new_path
                explored.append(node)
        # Return empty list if path doesn't exist
        return []

    def bfs(self, graph, start_node, dest_node, limit, mode):
        """
        BFS entry point
        :param graph: Graph obj
        :param start_node: node id of source
        :param dest_node: node id of dest
        :param limit: Deviance allowed
        :param mode: Max/Min
        :return: Optimized shortest path
        """
        logging.info("Finding shortest path using BFS Algorithm")
        try:
            return self.get_shortest_path(graph, start_node, dest_node)
        except:
            raise Exception("Start node not in graph")
