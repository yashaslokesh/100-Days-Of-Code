
""" The entry in the n-th row and m-th column will be the cost to travel
    from the vertex at n to the vertex at m """
class AdjacencyMatrixGraph(object):

    def __init__(self):
        self.adj_matrix = []
        self.vertices = {}
        self.datamap = {}
        self.count = 0
    
    def add_vertex(self, name : str, data):
        self.vertices[name] = self.count
        self.datamap[name] = data
        self.count += 1

        self.adj_matrix.append([0 for _ in range(self.count)])

        for row_num, row in enumerate(self.adj_matrix):
            if row_num != len(self.adj_matrix) - 1:
                row.extend([0 for _ in range(self.count - len(row))])

    def add_edge(self, source_name : str, dest_name : str, cost):
        if source_name not in self.vertices or dest_name not in self.vertices:
            raise ValueError('Edge can only be added between vertices already '
                             'added to the graph')

        source_index = self.vertices[source_name]
        dest_index = self.vertices[dest_name]

        self.adj_matrix[source_index][dest_index] = cost
    
    def __str__(self):
        """ 
        Utility function for printing out a matrix without extra commas or
        brackets anywhere (avoids the standard list printing representation) 
        """
        return '\nGraph:\n' + '\n'.join(' '.join(str(num) for num in row) 
                                        for row in self.adj_matrix) + '\n'
    

def main():
    graph = AdjacencyMatrixGraph()
    graph.add_vertex('1', 1)
    graph.add_vertex('2', 2)
    print(graph)

    graph.add_edge('1', '2', 5)
    graph.add_vertex('3', 3)
    graph.add_edge('3', '1', 4)
    graph.add_edge('2', '3', 2)
    graph.add_edge('1','3', 5)

    print(graph)

if __name__ == '__main__':
    main()