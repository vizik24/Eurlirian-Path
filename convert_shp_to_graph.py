# import geopandas as gpd
# import networkx as nx
# import matplotlib.pyplot as plt

# def create_graph_from_shapefile(shapefile_path):
#     streets_gdf = gpd.read_file(shapefile_path)
#     exploded = streets_gdf.explode()

#     G = nx.Graph()

#     for index, row in exploded.iterrows():
#         start_node = (row['geometry'].coords[0][0], row['geometry'].coords[0][1])
#         end_node = (row['geometry'].coords[-1][0], row['geometry'].coords[-1][1])

#         # Convert coordinates to strings
#         start_node_str = str(start_node)
#         end_node_str = str(end_node)

#         G.add_edge(start_node_str, end_node_str)
    

#     # -------
#     #in order to make sure the outputted graph can have a eulirian path or circuit,
#     # therefore we may need to remove x nodes with odd number of edges connecting them, n. x = n-2
#     # -----
#     # get number of nodes with odd degrees    
#     odd_degree_nodes = [node for node, degree in graph.degree() if degree % 2 != 0]
#     removal_number = odd_degree_nodes - 2

#     if not odd_degree_nodes:
#         print("No nodes with odd degrees found.")


#     def remove_nodes_with_odd_degrees(graph, num_nodes_to_remove):
#         # Find nodes with odd degrees
#         odd_degree_nodes = [node for node, degree in graph.degree() if degree % 2 != 0]

#         if not odd_degree_nodes:
#             print("No nodes with odd degrees found.")
#             return

#         # Remove user-defined number of nodes with odd degrees
#         nodes_to_remove = odd_degree_nodes[:num_nodes_to_remove]
#         graph.remove_nodes_from(nodes_to_remove)

#         print(f"Removed {num_nodes_to_remove} nodes with odd degrees.")
#         print(f"Remaining nodes: {graph.nodes()}")

#     # Example usage:
#     # Create a sample graph (you can replace this with your own graph)
#     G = nx.Graph()
#     G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (3, 5)])

#     # Get user input for the number of nodes to remove
#     num_nodes_to_remove = int(input("Enter the number of nodes to remove with odd degrees: "))

#     # Call the function to remove nodes with odd degrees
#     remove_nodes_with_odd_degrees(G, removal_number)


#     return G

import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt

def remove_nodes_with_odd_degrees(graph, num_nodes_to_remove):
    # Find nodes with odd degrees
    odd_degree_nodes = [node for node, degree in graph.degree() if degree % 2 != 0]

    if not odd_degree_nodes:
        print("No nodes with odd degrees found.")
        return

    # Remove a specific number of nodes with odd degrees
    nodes_to_remove = odd_degree_nodes[:num_nodes_to_remove]
    graph.remove_nodes_from(nodes_to_remove)

    print(f"Removed {num_nodes_to_remove} nodes with odd degrees.")

def remove_nodes_with_zero_degrees(graph):
    # Find nodes with odd degrees
    zero_degree_nodes = [node for node, degree in graph.degree() if degree == 0]

    if not zero_degree_nodes:
        print("No nodes with zero degrees found.")
        return

    # Remove a specific number of nodes with zero degrees
    graph.remove_nodes_from(zero_degree_nodes)

    nodes_to_remove = len(zero_degree_nodes)
    print(f"Removed {nodes_to_remove} nodes with zero degrees.")

def create_graph_from_shapefile(shapefile_path):
    streets_gdf = gpd.read_file(shapefile_path)
    exploded = streets_gdf.explode(index_parts=True)

    G = nx.Graph()

    for index, row in exploded.iterrows():
        start_node = (row['geometry'].coords[0][0], row['geometry'].coords[0][1])
        end_node = (row['geometry'].coords[-1][0], row['geometry'].coords[-1][1])

        # Convert coordinates to strings
        start_node_str = str(start_node)
        end_node_str = str(end_node)

        G.add_edge(start_node_str, end_node_str)

    # Get number of nodes with odd degrees
    odd_degree_nodes = [node for node, degree in G.degree() if degree % 2 != 0]

    if not odd_degree_nodes:
        print("No nodes with odd degrees found.")
    else:
        # Calculate the number of nodes to remove
        num_nodes_to_remove = len(odd_degree_nodes) - 2

        # Remove nodes with odd degrees
        remove_nodes_with_odd_degrees(G, num_nodes_to_remove)
        # Remove nodes with zero degrees
        remove_nodes_with_zero_degrees(G)

    nx.draw(G, with_labels=False)
    plt.show()

    return G


    



