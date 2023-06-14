# grafos com usando lista de adjacencias
# Autor: Pedro Henrique da Cruz Santos

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.node_count = 0
        self.edge_count= 0

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []
            self.node_count += 1
        else:
            print(f"Node {node} already exist")

    def add_edge(self, node1, node2):
        try:
            self.adj_list[node1].append(node2)
            self.edge_count += 1
        except KeyError as e:
            print(f"WARNING: Node {e} not found.")

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_two_way_edge(self, node1, node2):
        self.add_edge(node1, node2)
        self.add_edge(node2, node1)

    def remove_node(self, node):
        try:
            if node in self.adj_list:
                del self.adj_list[node]
                self.node_count -= 1
                for key in self.adj_list:
                    try:
                        self.adj_list[key].remove(node)
                        self.edge_count -= 1
                    except ValueError:
                        pass
            else:
                print(f"WARNING: Node {node} not found.")
        except KeyError as e:
            print(f"WARNING: Node {e} not found.")

    # def remove_node_Prof(self, node):
    #     for node2 in self.adj_list:
    #         if node in self.adj_list[node2]:
    #             self.adj_list[node2].remove(node)
    #     self.adj_list.pop(node)        
    #     self.edge_count -= 1

    def remove_edge(self, node1, node2):
        try:
            self.adj_list[node1].remove(node2)
            self.edge_count -= 1
        except KeyError as e:
            print(f"WARNING: Node {e} not found.")
        except ValueError as e:
            print(f"WARNING: Edge {node1} -> {node2} not found.")



    # degree_in deve retornar o numero de arestas que chegam no nó, ou seja quantos nós apontam para ele
    def degree_in(self, node):
        count = 0
        for node2 in self.adj_list:
            if node in self.adj_list[node2]:
                count += 1
        return count


    def degree_out(self, node):
        try:
            return len(self.adj_list[node])
        except KeyError as e:
            print(f"WARNING: Node {e} not found.")

    def highest_degree_in(self):
        highest = float("-inf")
        for node in self.adj_list:
            if self.degree_in(node) > highest:
                highest = self.degree_in(node)
        return highest
        
    def highest_degree_out(self):
        highest = float("-inf")
        for node in self.adj_list:
            if self.degree_out(node) > highest:
                highest = self.degree_out(node)
        return highest
    
    def density(self):
        return self.edge_count / (self.node_count * (self.node_count - 1))
    
    def is_complete(self):
        if self.density() == 1:
            return True
        elif self.density() < 1:
            return False

     
    def there_is_edge(self, node1, node2):
        return node2 in self.adj_list[node1]
    
    def neighbors(self, node):
        return self.adj_list[node]
    
    def is_oriented(self):
        for node in self.adj_list:
            for node2 in self.adj_list[node]:
                if node not in self.adj_list[node2]:
                    return True
        return False
    
    def is_regular(self):
        degree_frist_node = self.degree_out(list(self.adj_list)[0])
        for node in self.adj_list:
            if self.degree_out(node) != degree_frist_node:
                return False
        return True
    
    def complement(self):
        g2 = Graph()
        for node in self.adj_list:
            g2.add_node(node)
            for node2 in self.adj_list:
                if node != node2 and not self.there_is_edge(node, node2):
                    g2.add_edge(node, node2)
        return g2
    
    def is_subgraph_of(self, g2):
        for node in self.adj_list:
            if node not in g2.adj_list:
                return False
            for node2 in self.adj_list:
                if node2 not in g2.adj_list[node]:
                    return False
        return True        
    
    def is_connected(self):
        pass



    def is_valid_walk(self, walk):
        for i in range(len(walk) - 1):
            if not self.there_is_edge(walk[i], walk[i + 1]):
                return False
        return True

    def is_valid_path(self, path):
        if not self.is_valid_walk(path):
            return False
        for node in self.adj_list:
            if path.count(node) > 1:
                return False
        return True
        

    def is_valid_circuit(self, circuit):
        if not self.is_valid_walk(circuit):
            return False
        if circuit[0] != circuit[-1]:
            return False
        for node in self.adj_list:
            if circuit.count(node) > 2:
                return False
        return True
    

    def bfs (self, s): #s is the starting node
        visited = [False] * self.node_count
        queue = []
        R = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            R.append(s)
            for i in self.adj_list[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True                
        return R
    

    def dfs (self, s): #s is the starting node
        visited = [False] * self.node_count
        stack = []
        R = []
        stack.append(s)
        visited[s] = True
        while stack:
            s = stack.pop()
            R.append(s)
            for i in self.adj_list[s]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True
        return R
    
    def dfs_recursive_aux(self, s, visited, R):
        visited[s] = True
        R.append(s)
        for i in self.adj_list[s]:
            if visited[i] == False:
                self.dfs_recursive_aux(i, visited, R)


    def dfs_recursive(self, s):
        visited = [False] * self.node_count
        R = []
        self.dfs_recursive_aux(s, visited, R)
        return R


    def __str__(self) -> str:
        output = "Nodes: " + str(self.node_count) + "\n"
        output += "Edges: " + str(self.edge_count) + "\n"
        output += str(self.adj_list)
        return output
    
       


    


    

        
