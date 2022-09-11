if __name__ == "__main__":
    words = input().split()
    if words:
        words_counts = {}
        most_common = words[0].lower()
        most_common_count = 1

        for word in words:
            word_lower = word.lower()
            if word_lower not in words_counts:
                words_counts[word_lower] = 0
            words_counts[word_lower] += 1
            
            if words_counts[word_lower] > most_common_count:
                most_common = word_lower
                most_common_count = words_counts[word_lower]
        print(most_common)
        