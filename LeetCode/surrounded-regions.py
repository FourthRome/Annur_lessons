# https://leetcode.com/problems/surrounded-regions/

from collections import deque

def secure_area(board, protected_zeros, start):
    m = len(board)
    n = len(board[0])
    cells_to_process = deque()

    if board[start[0]][start[1]] == 'O' and start not in protected_zeros:
        protected_zeros.add(start)
        cells_to_process.append(start)
    
    while cells_to_process:
        i, j = cells_to_process.popleft()

        # Top
        if i > 0:
            neighbour_idx = (i - 1, j)
            near_i, near_j = neighbour_idx
            if (board[near_i][near_j] == 'O'
                    and neighbour_idx not in protected_zeros):
                protected_zeros.add(neighbour_idx)
                cells_to_process.append(neighbour_idx)
        # Bottom
        if i < m - 1:
            neighbour_idx = (i + 1, j)
            near_i, near_j = neighbour_idx
            if (board[near_i][near_j] == 'O'
                    and neighbour_idx not in protected_zeros):
                protected_zeros.add(neighbour_idx)
                cells_to_process.append(neighbour_idx)
        # Left
        if j > 0:
            neighbour_idx = (i, j - 1)
            near_i, near_j = neighbour_idx
            if (board[near_i][near_j] == 'O'
                    and neighbour_idx not in protected_zeros):
                protected_zeros.add(neighbour_idx)
                cells_to_process.append(neighbour_idx)
        # Right
        if j < n - 1:
            neighbour_idx = (i, j + 1)
            near_i, near_j = neighbour_idx
            if (board[near_i][near_j] == 'O'
                    and neighbour_idx not in protected_zeros):
                protected_zeros.add(neighbour_idx)
                cells_to_process.append(neighbour_idx)


def secure_area_refactored(board, protected_zeros, start):
    m = len(board)
    n = len(board[0])
    cells_to_process = deque()

    if board[start[0]][start[1]] == 'O' and start not in protected_zeros:
        protected_zeros.add(start)
        cells_to_process.append(start)
    
    while cells_to_process:
        i, j = cells_to_process.popleft()

        neighbours = (
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1)
        )

        for neighbour in neighbours:
            check_neighbour(board, protected_zeros, neighbour, cells_to_process)


def check_neighbour(board, protected_zeros, index, cells_to_process):
    m = len(board)
    n = len(board[0])
    near_i, near_j = index
    if near_i >= 0 and near_i < m and near_j >= 0 and near_j < n: 
        if (board[near_i][near_j] == 'O'
                and index not in protected_zeros):
            protected_zeros.add(index)
            cells_to_process.append(index)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        protected_zeros = set()

        # Securing the values adjacent to the border
        # Top and bottom traverse
        for i in 0, m - 1:  # Note this is not a range
            row = board[i]
            for j, value in enumerate(row):
                if value == 'O':
                    # secure_area(board, protected_zeros, (i, j))
                    secure_area_refactored(board, protected_zeros, (i, j))
        # Left and right traverse
        for j in 0, n - 1:  # Again not a range
            for i in range(1, m - 1):
                if board[i][j] == 'O':
                    # secure_area(board, protected_zeros, (i, j))
                    secure_area_refactored(board, protected_zeros, (i, j))
        
        # Overwrite zeroes that are not protected
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == 'O' and (i, j) not in protected_zeros:
                    board[i][j] = 'X'
