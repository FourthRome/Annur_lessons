if __name__ == "__main__":
    # 1. String prefixes and multilining
    oneline_string = "a normal string with\nsome\rescape\tsequences"
    raw_string = r"I don't know\nany\rescape\tsequences"
    multiline_string = '''Well,
    there is some extra padding
and some\nescape sequences'''

    # print(oneline_string)
    # print(raw_string)
    # print(multiline_string)

    # 2. Concatenation
    naive_string = "a very " + "inefficient way " + "of getting one string " + "from several strings"
    weird_string = ("this is a very long string, "
                   "but, surprisingly enough, "
                   "this whole construction "
                   "is still "
                   "just "
                   "one "
                   "string")
    
    building_blocks = [
        "the most",
        "common",
        "way",
        "to",
        "build"
    ]
    building_blocks.append("a string from several strings")
    the_right_string = " ".join(building_blocks)

    # print(naive_string)
    # print(weird_string)
    # print(the_right_string)

    # 3. String formatting
    ugly_string = "I have " + str(2) + " apples"
    oldschool_string = "I have {} oranges".format(3)
    new_kid_string = f"I have {42 + 42 + 42} answers"

    # print(ugly_string)
    # print(oldschool_string)
    # print(new_kid_string)
