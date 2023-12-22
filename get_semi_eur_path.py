import networkx as nx
import matplotlib.pyplot as plt

# Using DFS for finding semi-Eulerian path traversal
def dfs(u, graph, visited_edge, path=[]):
    path = path + [u]
    for v in graph[u]:
        if visited_edge[u][v] == False:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    return path

# For checking if the graph has a semi-Eulerian path
def check_semi_euler(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for node in graph.nodes():  
        if graph.degree(node) % 2 == 1:
            odd_degree_nodes += 1
            odd_node = node
    if odd_degree_nodes == 0:
        print("Graph has a semi-Eulerian circuit")
    elif odd_degree_nodes == 2:
        print("Graph has a semi-Eulerian path")
        start_node = odd_node
        visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
        path = dfs(start_node, graph, visited_edge)
        print("Semi-Eulerian path:", path)
    else:
        print("Graph is not semi-Eulerian")

def main():
    from convert_shp_to_graph import create_graph_from_shapefile

    shapefile_path = '/Users/max/Downloads/Major_Road_Network_2018_Open_Roads/Major_Road_Network_2018_Open_Roads.shp'

    G = create_graph_from_shapefile(shapefile_path)

if __name__ == "__main__":
    main()
