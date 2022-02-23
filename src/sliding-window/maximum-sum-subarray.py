# This solution has a O(n) algorithm complexity
def max_sub_array_of_size_k(k, arr):
    last_max = 0
    initial_position = 0
    max_sum = 0
    for i in range(len(arr)):   # O(n) 
        max_sum += arr[i]
        if((initial_position + k - 1) == i):
            last_max = max(last_max, max_sum)
            max_sum -= arr[initial_position]
            initial_position+=1

    return last_max

# Another aproach with O(n * k) algorithm complexity
#def max_sub_array_of_size_k(k, arr):
#    max_sum = 0
#
#    for i in range(len(arr) -k + 1): # O(n)
#        interval_sum = 0
#        for j in range(i, i + k):    # O(k)
#            interval_sum += arr[j]
#        max_sum = max(max_sum, interval_sum)
#
#    return max_sum


if __name__ == '__main__':
    print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
