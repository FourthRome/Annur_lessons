#--------------------
# Approach One: naive
#--------------------
# def findBestPath(grid, i, j):
#     m = len(grid)
#     n = len(grid[0])

#     down_score = findBestPath(grid, i + 1, j) if i < m - 1 else None
#     right_score = findBestPath(grid, i, j + 1) if j < n - 1 else None

#     return grid[i][j] + min(
#             (x for x in (down_score, right_score) if x is not None),
#             default=0)


# def minPathSum(grid):
#     return findBestPath(grid, 0, 0)


# if __name__ == "__main__":
#     n = int(input())
#     matrix = []
#     for i in range(n):
#         matrix.append([int(token) for token in input().split()])
#     print(minPathSum(matrix))




#--------------------------
# Approach Two: DIY caching
#--------------------------
# cache = {}  # Dangerous global object, there are better ways

# def findBestPath(grid, i, j):
#     if (i, j) in cache:
#         return cache[(i, j)]
#     m = len(grid)
#     n = len(grid[0])

#     down_score = findBestPath(grid, i + 1, j) if i < m - 1 else None
#     right_score = findBestPath(grid, i, j + 1) if j < n - 1 else None

#     result = grid[i][j] + min(
#             (x for x in (down_score, right_score) if x is not None),
#             default=0)
#     cache[(i, j)] = result
#     return result


# def minPathSum(grid):
#     return findBestPath(grid, 0, 0)


# if __name__ == "__main__":
#     n = int(input())
#     matrix = []
#     for i in range(n):
#         matrix.append([int(token) for token in input().split()])
#     print(minPathSum(matrix))




#---------------------------------
# Approach Three: The Pythonic Way
#---------------------------------
from functools import cache


@cache
def findBestPath(i, j):
    m = len(grid)
    n = len(grid[0])

    down_score = findBestPath(i + 1, j) if i < m - 1 else None
    right_score = findBestPath(i, j + 1) if j < n - 1 else None

    return grid[i][j] + min(
           (x for x in (down_score, right_score) if x is not None),
           default=0)


def minPathSum():
    return findBestPath(0, 0)


if __name__ == "__main__":
    n = int(input())
    grid = []
    for i in range(n):
        grid.append([int(token) for token in input().split()])
    print(minPathSum())
    # f"one: {i}, two: {n}"
    # "one: " + str(i) + ", two: " + str(n)
    # ",".join(2, 3, 4)
