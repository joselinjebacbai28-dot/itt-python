def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        segment = string[i : i + k]
        unique_segment = "".join(dict.fromkeys(segment))
        print(unique_segment)



