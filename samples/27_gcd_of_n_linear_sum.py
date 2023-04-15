from functools import cmp_to_key


def compare(a, b):
    return a[0] - b[0]


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
    #     n = int(file.readline())
    #     values = [int(num) for num in file.readlines()]

    # Tricky initialization
    gcd_vector = [values[0] for _ in range(n)]
    gcd_vector[0] = values[1]

    for i, value in enumerate(values):
        for j in range(n):
            if j != i:
                gcd_vector[j] = gcd(gcd_vector[j], value)

    indices = [i for i in range(n)]
    results = sorted(
            zip(gcd_vector, indices),
            key=cmp_to_key(compare),
            reverse=True)
    max_gcd = results[0][0]
    print(f"Maximum gcd: {max_gcd}")

    max_sum = 0
    # Note that I don't use range based for below
    for result in results:
        if result[0] != max_gcd:
            # We have checked all combinations that give
            # the maximum gcd
            break
        candidate_sum = sum(values) - values[result[1]]
        max_sum = max(max_sum, candidate_sum)

    print(f"Max sum of the elements with this gcd: {max_sum}")
