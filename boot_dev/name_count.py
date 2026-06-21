def count_names(list_of_lists: list[list[str]], target_name: str) -> int:
    count = 0
    for sublist in list_of_lists:
        for name in sublist:
            if name == target_name:
                count+=1
    return count