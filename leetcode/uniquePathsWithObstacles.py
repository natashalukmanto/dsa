from typing import List


def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return 0
    dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
    print(dp)
    dp[0][0] = 1

    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[0])):
            if i == 0 and j == 0:
                continue
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
                continue
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            if j - 1 >= 0:
                dp[i][j] += dp[i][j - 1]
    return dp[-1][-1]

    # def dfs(x: int, y: int):
    #     if x >= rows or y >= cols:
    #         return
    #     if obstacleGrid[x][y] == 1:
    #         dp[x][y] == 0

    #     if x > 0 and y > 0:
    #         dp[x][y] = dp[x][y -1] + dp[i - 1][j]
    #     dp[x][y] += 1

    #     dfs(x+1, y)
    #     dfs(x, y+1)

    # dfs(0, 0)
    # return dp[rows-1][cols-1]

    # BRUTE FORCE
    # def dfs(x:int, y:int):
    #     if x > rows or y > cols or obstacleGrid[x][y] == 1:
    #         return 0
    #     if x == rows and y == cols:
    #         return 1

    #     #going down             right
    #     return dfs(x+1, y) + dfs(x, y+1)class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        print(dp)
        dp[0][0] = 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]

        # def dfs(x: int, y: int):
        #     if x >= rows or y >= cols:
        #         return
        #     if obstacleGrid[x][y] == 1:
        #         dp[x][y] == 0

        #     if x > 0 and y > 0:
        #         dp[x][y] = dp[x][y -1] + dp[i - 1][j]
        #     dp[x][y] += 1

        #     dfs(x+1, y)
        #     dfs(x, y+1)

        # dfs(0, 0)
        # return dp[rows-1][cols-1]

        # BRUTE FORCE
        # def dfs(x:int, y:int):
        #     if x > rows or y > cols or obstacleGrid[x][y] == 1:
        #         return 0
        #     if x == rows and y == cols:
        #         return 1

        #     #going down             right
        #     return dfs(x+1, y) + dfs(x, y+1)
