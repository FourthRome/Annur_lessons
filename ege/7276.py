from functools import cmp_to_key


def cmp_flights(a, b):
    # If there was no additional question in
    # the problem description, this would be enough
    # return a[1] - b[1]
    if a[1] != b[1]:
        return a[1] - b[1]
    else:
        return a[0] - b[0]


if __name__ == "__main__":
    L, N = [int(val) for val in input().split()]
    flights = []
    for _ in range(N):
        # Try this two lines (one at a time) and see the errors:
        # flights.append(int(val) for val in input().split())
        # flights.append((int(val) for val in input().split()))
        flights.append(tuple(int(val) for val in input().split()))
    flights.sort(key=cmp_to_key(cmp_flights))
 
    right_border = -1
    max_flights = 0
    min_last_departure_time = -1
    for flight in flights:
        if flight[0] >= right_border:
            right_border = flight[1]
            min_last_departure_time = flight[0]
            max_flights += 1
    
    print(max_flights, min_last_departure_time)
