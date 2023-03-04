class NumArray:

    def __init__(self, nums):
        self.original_len = len(nums)
        self.len = 1
        while self.len < self.original_len:
            self.len *= 2
        self.tree = [None] * self.len
        self.tree.extend(nums)
        self.tree.extend([0] * (self.len - self.original_len))
        self.ranges = [None] * self.len
        self.ranges.extend([(i, i) for i in range(self.original_len)])
        self.ranges.extend([None] * (self.len - self.original_len))
        for idx in range(self.len - 1, 0, -1):
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]
            if self.ranges[2 * idx]:
                if self.ranges[2 * idx + 1]:
                    self.ranges[idx] = (
                        self.ranges[2 * idx][0],
                        self.ranges[2 * idx + 1][1]
                    )
                else:
                    self.ranges[idx] = self.ranges[2 * idx]


    def update(self, index: int, val: int) -> None:
        self.tree[self.len + index] = val
        idx = (self.len + index) // 2
        while idx:
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]
            idx //= 2


    def sumRange(self, left: int, right: int) -> int:
        return self.sumIntersectingRange(left, right, 1)


    def sumIntersectingRange(self, left, right, node_idx):
        node_range = self.ranges[node_idx]
        if node_range is None or node_range[0] > right or node_range[1] < left:
            return 0
        if node_range[0] >= left and node_range[1] <= right:
            return self.tree[node_idx]
        return (self.sumIntersectingRange(left, right, node_idx * 2)
               + self.sumIntersectingRange(left, right, node_idx * 2 + 1))



if __name__ == "__main__":
    obj = NumArray([3, 5, 7, 1, 9, 42])
    obj.update(3, -1)
    print(obj.sumRange(0, 3))
