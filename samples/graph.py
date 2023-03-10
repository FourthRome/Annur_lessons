from collections import defaultdict
import math


def min_distance(city_a, city_b, cities):
    """Поиск минимального расстояния с помощью алгоритма Дейкстры.

    В случае если хотя бы одного из городов нет в графе или они
    находятся в разных компонентах связности, возвращает math.inf;
    иначе возвращает минимальное расстояние между городами.
    """
    def comparator(a):
        """Функция для сравнения между собой кортежей из dict.items()."""
        return a[1]
    
    # 0. Убедимся, что города вообще есть в графе.
    if city_a not in cities or city_b not in cities:
        return math.inf

    # 1. Инициализируем веса всех вершин.
    weights = {}
    for key in cities:
        weights[key] = math.inf
    weights[city_a] = 0

    # 2. Сделаем шаг алгоритма, если не настала очередь конечной вершины.
    city_name = city_a  # имя рассматриваемого города
    city_weight = 0  # вес рассматриваемого города
    visited = set()  # уже рассмотренные города
    while weights and city_name != city_b:
        # 1. Исключим рассматриваемый город из дальнейших изменяющих операций.
        del weights[city_name]
        visited.add(city_name)
        
        # 2. Обходим соседей, обновляем их веса.
        for neighbour, distance in cities[city_name].items():
            if neighbour in visited:
                continue
            new_distance = city_weight + distance
            weights[neighbour] = min(weights[neighbour], new_distance)

        # 3. Выбираем город с минимальным весом из оставшихся.
        city = min(weights.items(), key=comparator)  # неоптимально, но кратко
        city_name = city[0]
        city_weight = city[1]
        if city_weight == math.inf:
            # Обошли всю компоненту связности, но не встретили нужный город.
            break
    return weights[city_b]
    

if __name__ == "__main__":
    # Неориентированный граф дорог между городами.
    # Пример задания графа:
    # 3
    # moscow lisbon 102
    # lisbon peterburg 54
    # samara oslo 38
    # Требуется найти кратчайшее расстояние между городами по запросу.
    # Пример запроса:
    # 1
    # moscow peterburg
    # > 156

    # Возможный, но малополезный вариант обработки ввода.
    # n = int(input())
    # [input().split() for _ in range(n)]

    # Пример желаемой структуры данных после обработки:
    # cities = {
    #     "moscow": {
    #         "lisbon": 102,
    #     },
    #     "lisbon": {
    #         "moscow": 102,
    #         "peterburg": 54,
    #     },
    #     "peterburg": {
    #         "lisbon": 54,
    #     },
    #     "samara": {
    #         "oslo": 38,
    #     },
    #     "oslo": {
    #         "samara": 38,
    #     },
    # }

    # 1. Ввод графа с клавиатуры (детали определяются спецификой графа —
    # является ли он ориентированным, взвешенным, имеют ли вершины веса и т.д.).
    n = int(input())
    cities = defaultdict(dict)
    for _ in range(n):
        tokens = input().split()
        cities[tokens[0]][tokens[1]] = int(tokens[2])
        cities[tokens[1]][tokens[0]] = int(tokens[2])
    
    # 2. Поиск кратчайшего пути между заданными вершинами.
    m = int(input())
    for _ in range(m):
        tokens = input().split()
        result = min_distance(*tokens, cities)
        if result != math.inf:
            print(result)
        else:
            print(f"There is no road between {tokens[0]} and {tokens[1]}!")
