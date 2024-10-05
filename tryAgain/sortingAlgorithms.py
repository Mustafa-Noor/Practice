def bubble_sort(data, column_index):
    """Sorts data using the bubble sort algorithm based on the specified column index."""
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][column_index] > data[j + 1][column_index]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def selection_sort(data, column_index):
    """Sorts data using the selection sort algorithm based on the specified column index."""
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j][column_index] < data[min_index][column_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

def insertion_sort(data, column_index):
    """Sorts data using the insertion sort algorithm based on the specified column index."""
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j][column_index] > key[column_index]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def merge_sort(data, column_index):
    """Sorts data using the merge sort algorithm based on the specified column index."""
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid], column_index)
    right = merge_sort(data[mid:], column_index)
    return merge(left, right, column_index)

def merge(left, right, column_index):
    """Helper function to merge two halves in merge sort."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][column_index] <= right[j][column_index]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(data, column_index):
    """Sorts data using the quick sort algorithm based on the specified column index."""
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2][column_index]
    left = [x for x in data if x[column_index] < pivot]
    middle = [x for x in data if x[column_index] == pivot]
    right = [x for x in data if x[column_index] > pivot]
    return quick_sort(left, column_index) + middle + quick_sort(right, column_index)

def counting_sort(data, column_index):
    """Sorts data using the counting sort algorithm based on the specified column index."""
    min_value = min(data, key=lambda x: x[column_index])[column_index]
    max_value = max(data, key=lambda x: x[column_index])[column_index]
    count = [0] * (max_value - min_value + 1)
    output = [0] * len(data)
    for i in range(len(data)):
        count[data[i][column_index] - min_value] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(data) - 1, -1, -1):
        output[count[data[i][column_index] - min_value] - 1] = data[i]
        count[data[i][column_index] - min_value] -= 1
    return output

def radix_sort(data, column_index):
    """Sorts data using the radix sort algorithm based on the specified column index."""
    max_value = max(data, key=lambda x: x[column_index])[column_index]
    exp = 1
    while max_value // exp > 0:
        data = counting_sort_for_radix(data, column_index, exp)
        exp *= 10
    return data

def counting_sort_for_radix(data, column_index, exp):
    """Helper function for radix sort to perform counting sort on specific digit."""
    count = [0] * 10
    output = [0] * len(data)
    for i in range(len(data)):
        index = (data[i][column_index] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(len(data) - 1, -1, -1):
        index = (data[i][column_index] // exp) % 10
        output[count[index] - 1] = data[i]
        count[index] -= 1
    return output

def tim_sort(data, column_index):
    """Sorts data using the tim sort algorithm based on the specified column index."""
    min_run = 32
    n = len(data)
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(data[start:end + 1], column_index)
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min((left + 2 * size - 1), n - 1)
            if mid < right:
                merge(data, left, mid + 1, right, column_index)
        size *= 2
    return data

def bucket_sort(data, column_index):
    """Sorts data using the bucket sort algorithm based on the specified column index."""
    n = len(data)
    buckets = [[] for _ in range(n)]
    for i in range(n):
        index = int(data[i][column_index] * n)
        buckets[index].append(data[i])
    for i in range(n):
        buckets[i] = insertion_sort(buckets[i], column_index)
    output = []
    for bucket in buckets:
        output.extend(bucket)
    return output

def pigeonhole_sort(data, column_index):
    """Sorts data using the pigeonhole sort algorithm based on the specified column index."""
    min_value = min(data, key=lambda x: x[column_index])[column_index]
    max_value = max(data, key=lambda x: x[column_index])[column_index]
    size = max_value - min_value + 1
    holes = [[] for _ in range(size)]
    for row in data:
        holes[row[column_index] - min_value].append(row)
    output = []
    for hole in holes:
        output.extend(hole)
    return output

def cycle_sort(data, column_index):
    """Sorts data using the cycle sort algorithm based on the specified column index."""
    writes = 0
    for cycle_start in range(len(data) - 1):
        item = data[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, len(data)):
            if data[i][column_index] < item[column_index]:
                pos += 1
        if pos == cycle_start:
            continue
        while data[pos][column_index] == item[column_index]:
            pos += 1
        data[pos], item = item, data[pos]
        writes += 1
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(data)):
                if data[i][column_index] < item[column_index]:
                    pos += 1
            while data[pos][column_index] == item[column_index]:
                pos += 1
            data[pos], item = item, data[pos]
            writes += 1
    return data
