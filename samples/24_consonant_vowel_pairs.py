if __name__ == "__main__":
    with open("24_7356.txt", "r") as input:
        str = input.read().strip()
        pairs_count = 0
        prev_is_consonant = False
        str_len = 0
        max_str_len = 0
        left_idx = 0

        for idx, ch in enumerate(str):
            if ch in ("C", "D", "F"):
                prev_is_consonant = True
            elif ch in ("A", "O"):
                if prev_is_consonant:
                    pairs_count += 1
                    if pairs_count > 5:
                        while (str[left_idx] in ("A", "O")):
                            left_idx += 1
                            str_len -= 1
                        while (str[left_idx] in ("C", "D", "F")):
                            left_idx += 1
                            str_len -= 1
                        pairs_count -= 1
                prev_is_consonant = False
            else:
                raise RuntimeError("Unexpected symbol in file")
            str_len += 1
            max_str_len = max(max_str_len, str_len)
    print(max_str_len)
