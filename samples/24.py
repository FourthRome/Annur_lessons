if __name__ == "__main__":
    s = input()  # ABCXZZBCXZZYABC
    sub = "XZZY"
    sub_idx = 0

    count = 0
    max_count = count
    for ch in s:
        if ch == sub[sub_idx]:
            sub_idx += 1
            if sub_idx == len(sub):
                max_count = max(count, max_count)
                count = 3
                sub_idx = 0
            else:
                count += 1
        else:
            count += 1
            sub_idx = 0
    max_count = max(count, max_count)
    print(max_count)
