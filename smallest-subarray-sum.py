# This solution has a O(n * log(n)) = O(log(n)) algorithm complexity
def smallest_subarray_sum(s, arr):
    smallest_count = len(arr) + 1
    for i in range(len(arr)):
        print("Getting i")
        window_sum = 0
        count = 0
        for j in range(i, len(arr)):
            print(arr[j])
            count += 1
            window_sum += arr[j]
            if(window_sum >= s):
                smallest_count = min(smallest_count, count)
                print(f"{smallest_count=}, {count}")
                break
    return smallest_count


if __name__ == '__main__':
    print(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2]))
