class NumArray:

    def __init__(self, nums):
        self.original_len = len(nums)
        
        # Ближайшую к размеру массива степень двойки положим в self.len.
        self.len = 1
        while self.len < self.original_len:
            self.len *= 2
        
        # В self.tree положим дерево слой за слоем, начиная с корня.
        # При этом фактически заполняем массив, начиная с индекса 1,
        # чтобы было удобнее считать индексы дочерних и
        # родительских узлов.
        # внутренние узлы
        self.tree = [None] * self.len
        # листовые узлы с исходным массивом
        self.tree.extend(nums)
        # искусственные листовые узлы
        self.tree.extend([0] * (self.len - self.original_len))
        
        # self.ranges используем для быстрого определения, какой диапазон
        # индексов оригинального массива покрывается очередным узлом.
        # Диапазоны представляем в виде (left_border, right_border),
        # где left_border и right_border включены в покрываемый диапазон,
        # либо None, если узел покрывает только искусственно добавленные узлы
        # (покрывает "индексы" за пределами исходного массива).
        self.ranges = [None] * self.len
        self.ranges.extend([(i, i) for i in range(self.original_len)])
        self.ranges.extend([None] * (self.len - self.original_len))
        
        # Инициализируем первые self.len элементов в self.tree и self.ranges
        # корректными значениями.
        for idx in range(self.len - 1, 0, -1):
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]
            # Если левое поддерево покрывает в т.ч. валидные индексы
            if self.ranges[2 * idx]:
                # Если правое поддерево покрывает в т.ч. валидные индексы
                if self.ranges[2 * idx + 1]:
                    self.ranges[idx] = (
                        self.ranges[2 * idx][0],
                        self.ranges[2 * idx + 1][1]
                    )
                else:
                    self.ranges[idx] = self.ranges[2 * idx]


    def update(self, index: int, val: int) -> None:
        # Обновляем значение в листе и во всех его предках.
        self.tree[self.len + index] = val
        idx = (self.len + index) // 2
        while idx:
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]
            idx //= 2


    def sumRange(self, left: int, right: int) -> int:
        return self.sumIntersectingRange(left, right, 1)


    def sumIntersectingRange(self, left, right, node_idx):
        # В зависимости от типа пересечения искомого отрезка с покрываемым
        # данным узлом возвращаем один из трёх вариантов.
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
