def totalFruit(fruits):
    """
    :type fruits: List[int]
    :rtype: int
    """
    window_start = 0
    max_count = 0
    count = 0
    current_fruits = {}
    for window_end in fruits:
        count += 1
        current_fruits[window_end] = current_fruits.get(window_end, 0) + 1
        while(len(current_fruits) > 2):
            count -= 1
            max_count = max(max_count, count)
            delete_key = fruits[window_start]
            window_start += 1
            current_fruits[delete_key] = current_fruits[delete_key] - 1
            if(current_fruits[delete_key] == 0):
                del current_fruits[delete_key]
    return max(max_count, count)


if __name__ == '__main__':
    print(totalFruit([1, 2, 3, 2, 2]))
