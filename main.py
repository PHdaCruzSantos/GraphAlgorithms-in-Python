from graph import Graph

grafo = Graph()

grafo.add_node("Bia")
grafo.add_node("Caio")
grafo.add_node("Liz")
grafo.add_node("Alex")

grafo.add_edge("Caio", "Liz")
grafo.add_edge("Liz", "Caio")
grafo.add_edge("Caio", "Alex")
grafo.add_edge("Alex", "Liz")

print(grafo)

grafo.add_nodes(["Pedro", "Joao", "Maria", "Jose"])
grafo.add_two_way_edge("Pedro", "Joao")
grafo.add_node("Bia")
print("------------------------")
print(grafo)
# print("------------------------")
# grafo.remove_node("Caio")
# grafo.remove_edge("Pedro", "Joao")
# grafo.remove_node_Prof("Caio")
# grafo.remove_edge_Prof("Pedro", "Joao")
# print(grafo)
print("------------------------")
print("degree in:", grafo.degree_in("Liz"))
print("degree out:", grafo.degree_out("Caio"))
print("------------------------")

print("Highest degree in:", grafo.highest_degree_in())
print("Highest degree out:", grafo.highest_degree_out())

print("------------------------")
print("Density:", grafo.density())
print("------------------------")
print("is complete:", grafo.is_complete())

g2 = Graph()

g2.add_node(0)
g2.add_node(1)
g2.add_node(2)
g2.add_node(3)
g2.add_node(4)
g2.add_node(5)
g2.add_node(6)

g2.add_edge(0, 1)
g2.add_edge(0, 3)
g2.add_edge(0, 5)

g2.add_edge(1, 0)
g2.add_edge(1, 2)
g2.add_edge(1, 3)

g2.add_edge(2, 1)
g2.add_edge(2, 3)
g2.add_edge(2, 4)

g2.add_edge(3, 0)
g2.add_edge(3, 1)
g2.add_edge(3, 2)
g2.add_edge(3, 4)
g2.add_edge(3, 5)
g2.add_edge(3, 6)

g2.add_edge(4, 2)
g2.add_edge(4, 3)
g2.add_edge(4, 6)

g2.add_edge(5, 0)
g2.add_edge(5, 3)
g2.add_edge(5, 6)

g2.add_edge(6, 3)
g2.add_edge(6, 4)
g2.add_edge(6, 5)

walk = [0, 3, 0, 5, 3, 4]
path = [0, 3, 4, 6]
circuit = [0, 3, 0, 5, 6, 3, 4, 2, 1, 0]

print("is valid walk?? ", g2.is_valid_walk(walk))
print("is valid path?? ", g2.is_valid_path(path))
print("is valid circuit?? ", g2.is_valid_circuit(circuit))

print("------------------------")

g3 = Graph()

g3.add_node(0)
g3.add_node(1)
g3.add_node(2)
g3.add_node(3)
g3.add_node(4)

g3.add_edge(0, 1)
g3.add_edge(0, 3)
g3.add_edge(0, 4)
g3.add_edge(1, 2)

print("bfs:", g3.bfs(0))

print("------------------------")

g4 = Graph()

g4.add_node(0)
g4.add_node(1)
g4.add_node(2)
g4.add_node(3)
g4.add_node(4)
g4.add_node(5)

g4.add_edge(0, 2)
g4.add_edge(0, 5)
g4.add_edge(2, 4)
g4.add_edge(4, 3)
g4.add_edge(4, 5)
g4.add_edge(5, 0)

print("dfs:", g4.dfs_recursive(0))

