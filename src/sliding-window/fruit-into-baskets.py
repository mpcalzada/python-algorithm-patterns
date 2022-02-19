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

def totalFruitTwo(tree):
        count, i = {}, 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            print(f"{count=}")
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
        return j - i + 1


if __name__ == '__main__':
    print(totalFruit([1, 2, 1, 3, 2, 2]))
    print(totalFruitTwo([1, 2, 1, 3, 2, 2]))
