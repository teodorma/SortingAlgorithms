def counting_sort(arr, exp, base):
    n = len(arr)
    output = [0] * n
    count = [0] * base

    for i in range(n):
        index = int(arr[i] // exp) % base
        count[index] += 1

    for i in range(1, base):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = int(arr[i] // exp) % base
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


def radix_sort_base10(arr):
    int_part = [int(num) for num in arr]
    frac_part = [(num - int(num)) for num in arr]

    max_num = max(int_part)
    exp = 1
    while max_num // exp > 0:
        counting_sort(int_part, exp, 10)
        exp *= 10

    frac_part_base10 = [int(frac * (10 ** 6)) for frac in frac_part]

    counting_sort(frac_part_base10, 1, 10 ** 6)

    for i in range(len(arr)):
        frac_part[i] = frac_part_base10[i] / (10 ** 6)
        arr[i] = int_part[i] + frac_part[i]


def radix_sort_base2_16(arr):
    int_part = [int(num) for num in arr]
    frac_part = [(num - int(num)) for num in arr]

    max_num = max(int_part)
    exp = 1
    while max_num // exp > 0:
        counting_sort(int_part, exp, 1 << 16)
        exp *= 1 << 16

    counting_sort(frac_part, 1 / (1 << 16), 1 << 16)

    for i in range(len(arr)):
        arr[i] = int_part[i] + frac_part[i]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def cube_sort(arr):
    n = len(arr)
    gap = n // 3

    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j - gap] > arr[j]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap //= 3


def bucket_sort(arr):
    if len(arr) <= 1:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    num_buckets = len(arr)

    if max_val == min_val:
        return arr

    bucket_range = (max_val - min_val) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = int((num - min_val) / bucket_range)
        index = min(index, num_buckets - 1)
        buckets[index].append(num)

    sorted_arr = [num for bucket in buckets for num in bucket.sort() or bucket]
    return sorted_arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


def native_sort(arr):
    arr.sort()
    return arr


def test_sorted(v):
    return all(v[i] <= v[i + 1] for i in range(len(v) - 1))