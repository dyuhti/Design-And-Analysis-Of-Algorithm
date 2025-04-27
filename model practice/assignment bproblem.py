class AssignmentProblem:
    def __init__(self, cost_matrix):
        self.n = len(cost_matrix)
        self.cost_matrix = cost_matrix
        self.min_cost = float('inf')
        self.min_assignment = [-1] * self.n
        self.visited = [False] * self.n
        self.path = []

    def branch_and_bound(self):
        current_cost = 0
        current_assignment = [-1] * self.n
        self._branch_and_bound_util(current_assignment, current_cost, 0)
        return self.min_cost, self.min_assignment

    def _branch_and_bound_util(self, current_assignment, current_cost, level):
        if level == self.n:
            if current_cost < self.min_cost:
                self.min_cost = current_cost
                self.min_assignment = current_assignment[:]
            return

        for i in range(self.n):
            if not self.visited[i]:
                self.visited[i] = True
                current_assignment[level] = i
                reduced_cost = self._reduce_matrix(current_assignment, level, i)
                self.path.append((level, i))

                if current_cost + reduced_cost < self.min_cost:
                    self._branch_and_bound_util(current_assignment, current_cost + self.cost_matrix[level][i],
                                                level + 1)

                self.path.pop()
                self.visited[i] = False
                current_assignment[level] = -1

    def _reduce_matrix(self, current_assignment, level, col):
        reduction_cost = 0

        # Row reduction
        for i in range(level + 1, self.n):
            min_val = float('inf')
            for j in range(self.n):
                if j != col and not self.visited[j]:
                    min_val = min(min_val, self.cost_matrix[i][j])
            reduction_cost += min_val
            for j in range(self.n):
                if j != col and not self.visited[j]:
                    self.cost_matrix[i][j] -= min_val

        # Column reduction
        min_val = float('inf')
        for i in range(self.n):
            if not self.visited[i]:
                min_val = min(min_val, self.cost_matrix[i][col])
        reduction_cost += min_val
        for i in range(self.n):
            if not self.visited[i]:
                self.cost_matrix[i][col] -= min_val

        return reduction_cost


# Example usage:
cost_matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

problem = AssignmentProblem(cost_matrix)
min_cost, min_assignment = problem.branch_and_bound()

print("Minimum Cost:", min_cost)
print("Assignment:", min_assignment)
