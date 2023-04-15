from functools import cmp_to_key


def compare(a, b):
    if a[0] != b[0]:
        return a[0] - b[0]
    else:
        return a[1] - b[1]


def gcd(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError(
                "Can't calculate gcd when one of the arguments is zero")
    while b:
        a, b = b, a % b
    # I forgot this return, and debug on stdin input
    # helped me catch it
    return a


if __name__ == "__main__":
    # This input section is for the purposes of initial testing
    n = int(input())
    values = [int(num) for num in input().split()]

    # with open("27A_7358.txt", "r") as file:
    # This will not finish in time:
    # with open("27B_7358.txt", "r") as file:
        # n = int(file.readline())
        # values = [int(num) for num in file.readlines()]

    # Tricky initialization
    gcd_vector = [values[0] for _ in range(n)]
    gcd_vector[0] = values[1]
    sum_vector = [0 for _ in range(n)]  # We should actually use np.zeros here

    for i, value in enumerate(values):
        for j in range(n):
            if j != i:
                gcd_vector[j] = gcd(gcd_vector[j], value)
                sum_vector[j] += value

    for value in zip(gcd_vector, sum_vector):
        print(value)

    results = sorted(
            zip(gcd_vector, sum_vector),
            key=cmp_to_key(compare),
            reverse=True)
    print(f"Maximum gcd: {results[0][0]}")
    print(f"Sum of the elements: {results[0][1]}")
