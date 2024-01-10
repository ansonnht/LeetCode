class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {}
        for i in range(n):
            if manager[i] in graph:
                graph[manager[i]].append(i)
            else:
                graph[manager[i]] = [i]
        def dfs(node):
            manager_time = informTime[node]
            employee_time = 0
            if node in graph:
                for employee in graph[node]:
                    employee_time = max(employee_time, dfs(employee))
            return manager_time + employee_time
        return dfs(headID)
