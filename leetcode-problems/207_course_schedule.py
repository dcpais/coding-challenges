class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {i: [] for i in range(numCourses)}
        # Initialize Adjacency list
        for crs, pre in prerequisites:
            adjList[pre].append(crs)

        print(adjList)

        # Visited set
        visited = set()

        # Run DFS on each node to check for loops
        # optimized by removing checked nodes
        def dfs(crs):
            if crs in visited:
                return False
            if not adjList[crs]:
                return True 
            
            visited.add(crs)
            for next in adjList[crs]:
                if not dfs(next):
                    return False

            adjList[crs] = []
            visited.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



            