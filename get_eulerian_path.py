# Eulerian Path is a path in graph that visits every edge exactly once.
# Eulerian Circuit is an Eulerian Path which starts and ends on the same
# vertex.
import networkx as nx
import matplotlib.pyplot as plt

# using dfs for finding eulerian path traversal
def dfs(u, graph, visited_edge, path=[]):
    path = path + [u]
    for v in graph[u]:
        if visited_edge[u][v] == False:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    return path


# for checking if graph has euler path or circuit
def check_circuit_or_path(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for node in graph.nodes():  
        if graph.degree(node) % 2 == 1:
            odd_degree_nodes += 1
            odd_node = node
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    return 3, odd_node



def check_euler(graph, max_node):
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
    check, odd_node = check_circuit_or_path(graph, max_node)
    if check == 3:
        print("graph is not Eulerian")
        print("no path")
        return
    start_node = 1
    if check == 2:
        start_node = odd_node
        print("graph has an Euler path")
    if check == 1:
        print("graph has an Euler cycle")
    path = dfs(start_node, graph, visited_edge)
    print(path)
    return False  



def main():
    from convert_shp_to_graph import create_graph_from_shapefile

    shapefile_path = '/Users/max/Downloads/Def_Paths/Def_Paths.shp'

    G = create_graph_from_shapefile(shapefile_path)

    max_node = G.number_of_nodes()
    check_euler(G, max_node)

   


if __name__ == "__main__":
    main()