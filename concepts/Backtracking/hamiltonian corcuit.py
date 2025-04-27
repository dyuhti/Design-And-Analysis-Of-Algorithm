class HamiltonianCircuit:
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = len(graph)
        self.hamiltonian_path = [-1] * self.num_vertices

    def is_valid(self, v, pos):
        # Check if this vertex can be added to the Hamiltonian path
        if self.graph[self.hamiltonian_path[pos - 1]][v] == 0:
            return False

        # Check if the vertex has already been visited
        for vertex in self.hamiltonian_path:
            if vertex == v:
                return False

        return True

    def solve_hamiltonian(self):
        # Start with vertex 0 as the first vertex in the Hamiltonian path
        self.hamiltonian_path[0] = 0

        if not self._solve_hamiltonian_util(1):
            print("No Hamiltonian circuit exists.")
        else:
            print("Hamiltonian circuit found:")
            print(self.hamiltonian_path)

    def _solve_hamiltonian_util(self, pos):
        # Base case: if all vertices are included in the Hamiltonian path
        if pos == self.num_vertices:
            # Check if there is an edge from the last vertex to the first vertex
            if self.graph[self.hamiltonian_path[pos - 1]][self.hamiltonian_path[0]] == 1:
                return True
            else:
                return False

        # Try different vertices as the next candidate in the Hamiltonian path
        for v in range(1, self.num_vertices):
            if self.is_valid(v, pos):
                self.hamiltonian_path[pos] = v
                if self._solve_hamiltonian_util(pos + 1):
                    return True
                # Backtrack
                self.hamiltonian_path[pos] = -1

        return False


# Example usage:
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hamiltonian_solver = HamiltonianCircuit(graph)
hamiltonian_solver.solve_hamiltonian()
