import numpy as np


class CSP:
    def __init__(self, n):
        """
        Here we initialize all the required variables for the CSP computation,
        according to the n.
        """
        # Your code here
        self.n = n
        self.grid = np.array(np.zeros(shape=(n, n), dtype=int))
        self.domain = np.array(np.ones(shape=(n, n), dtype=int))
        self.number_of_iteration = 0

    def check_constraints(self,row,col) -> bool:
        """
        Here we check the grid horizontally, vertically and diagonally
        """
        for i in range(col):
            if self.grid[row,i] == 1:
                return False
 
        for i, j in zip(range(row, -1, -1),
                        range(col, -1, -1)):
            if self.grid[i,j] == 1:
                return False
    
        for i, j in zip(range(row, self.n, 1),
                        range(col, -1, -1)):
            if self.grid[i,j] == 1:
                return False
    
        return True
                    
    

    def forward_check(self, i):
        """
        After assigning a queen to ith column, we can make a forward check
        to boost up the computing speed and prune our search tree.
        """
        rows = []
        for row in range(self.n):
            if self.check_constraints(row, i):
                rows.append(row)
        domain = list(rows)
        for row in rows:
            if not self.check_constraints(row, i):
                domain.remove(row)
        return len(domain) == 0

    def assign(self, row, column):
        """
        assign 1 to self.grid[row,colmn]
        """
        self.grid[row,column] = 1 

    def _solve_problem_with_backtrack(self, i):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem.
        """
        if i >= self.n :
            return True 
        for row in range(self.n) :
            self.number_of_iteration += 1
            if self.check_constraints(row,i):
                self.assign(row,i)
                if self._solve_problem_with_backtrack(i+1):
                      return True
                self.grid[row,i] = 0

    def solve_problem_with_backtrack(self):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem
         and return solution's grid
        """
        return self._solve_problem_with_backtrack(0)

    def _solve_problem_with_forward_check(self, i):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem.
        """
        # Your code here
        
        if i >= self.n :
            return True 

        rows = []
        for row in range(self.n):
            if self.check_constraints(row, i):
                rows.append(row)
        for row in rows:
            self.grid[row, i] = 1
            domainWipeOut = False
            for point in self.getUnassignedFromConstraint(i):
                if self.forward_check(point):
                    domainWipeOut = True
                    break
            if not domainWipeOut:
                if self._solve_problem_with_forward_check(i + 1):
                    return True
            self.grid[row, i] = 0
        
        
    
    def getUnassignedFromConstraint(self,i):
        result = []
        for row in range(self.n):
            for col in range(i+1, self.n):
                if self.grid[row,col] == 0 and self.check_constraints(row, col):
                    result.append(col)
        return result
    

    def solve_problem_with_forward_check(self):
        """
         In this function we should set the ith queen in ith column and call itself recursively to solve the problem
         and return solution's grid
        """
        return self._solve_problem_with_forward_check(0)

