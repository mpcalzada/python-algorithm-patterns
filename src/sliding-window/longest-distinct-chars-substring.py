# This solution has a O(n + n) = O(n) time complexity and O(k) space complexity because of the HashMap
def longest_substring_with_k_distinct(str1, k):
    window_start = 0
    max_count = 0
    found_chars = {}
    window_count = 0
    for w in str1:
        window_count += 1
        count = found_chars.get(w, 0) + 1
        found_chars[w] = count
        #print(f"Adding {w} into {found_chars}")
        while(len(found_chars) > k):
            remove = str1[window_start]
            #print(f"Removing {remove} from {found_chars=}")
            minus_count = found_chars[remove] - 1
            window_start += 1
            if(minus_count == 0):
                del found_chars[remove]
                window_count -= 1
                max_count = max(max_count, window_count)
            else:
                found_chars[remove] = minus_count
    return max_count


if __name__ == '__main__':
    print(longest_substring_with_k_distinct("araaci", 2))
    print(longest_substring_with_k_distinct("araaci", 1))
    print(longest_substring_with_k_distinct("cbbebi", 3))
