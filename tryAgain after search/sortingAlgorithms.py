def bubble_sort(data, column_index, reverse):
    """Sorts data using the bubble sort algorithm based on the specified column index."""
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (data[j][column_index] > data[j + 1][column_index]) != reverse:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def selection_sort(data, column_index, reverse):
    """Sorts data using the selection sort algorithm based on the specified column index."""
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if (data[j][column_index] < data[min_index][column_index]) != reverse:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


def insertion_sort(data, column_index, reverse):
    """Sorts data using the insertion sort algorithm based on the specified column index."""
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and (data[j][column_index] > key[column_index]) != reverse:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def merge_sort(data, column_index, reverse):
    """Sorts data using the merge sort algorithm based on the specified column index."""
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid], column_index, reverse)
    right = merge_sort(data[mid:], column_index, reverse)
    return merge(left, right, column_index, reverse)


def merge(left, right, column_index, reverse):
    """Helper function to merge two halves in merge sort."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if (left[i][column_index] <= right[j][column_index]) != reverse:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(data, column_index, reverse):
    """Sorts data using the quick sort algorithm based on the specified column index."""
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2][column_index]
    left = [x for x in data if (x[column_index] < pivot) != reverse]
    middle = [x for x in data if x[column_index] == pivot]
    right = [x for x in data if (x[column_index] > pivot) != reverse]
    return quick_sort(left, column_index, reverse) + middle + quick_sort(right, column_index, reverse)


def counting_sort(data, column_index, reverse):
    if not data or not all(isinstance(row[column_index], int) for row in data):
        print("Error: Invalid data format for counting sort.")
        return []
    min_value = min(data, key=lambda x: x[column_index])[column_index]
    max_value = max(data, key=lambda x: x[column_index])[column_index]

    count = [0] * (max_value - min_value + 1)

    for row in data:
        count[row[column_index] - min_value] += 1

    output = []
    if reverse:
        for i in range(len(count) - 1, -1, -1):
            output.extend([row for row in data if row[column_index] == (min_value + i)] * count[i])
    else:
        for i in range(len(count)):
            output.extend([row for row in data if row[column_index] == (min_value + i)] * count[i])

    return output


def radix_sort(data, column_index, reverse):
    """Sorts data using the radix sort algorithm based on the specified column index."""
    for row in data:
        row[column_index] = int(row[column_index])

    max_value = max(data, key=lambda x: x[column_index])[column_index]
    exp = 1
    while max_value // exp > 0:
        data = counting_sort_for_radix(data, column_index, exp, reverse)
        exp *= 10
    return data


def counting_sort_for_radix(data, column_index, exp, reverse):
    count = [0] * 10
    output = [0] * len(data)

    for i in range(len(data)):
        index = (data[i][column_index] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    if reverse:
        for i in range(len(data) - 1, -1, -1):
            index = (data[i][column_index] // exp) % 10
            output[count[index] - 1] = data[i]
            count[index] -= 1
    else:
        for i in range(len(data) - 1, -1, -1):
            index = (data[i][column_index] // exp) % 10
            output[count[index] - 1] = data[i]
            count[index] -= 1

    return output


def bucket_sort(data, column_index, reverse):
    """Sorts data using the bucket sort algorithm based on the specified column index."""
    if not data:
        return data

    for row in data:
        row[column_index] = int(row[column_index])

    min_value = min(row[column_index] for row in data)
    max_value = max(row[column_index] for row in data)

    bucket_count = 10
    bucket_size = (max_value - min_value + 1) // bucket_count
    buckets = [[] for _ in range(bucket_count)]

    for i in range(len(data)):
        value = data[i][column_index]
        index = (value - min_value) // bucket_size if bucket_size > 0 else 0
        if index >= bucket_count:
            index = bucket_count - 1
        buckets[index].append(data[i])

    sorted_data = []
    for bucket in buckets:
        sorted_data.extend(sorted(bucket, key=lambda x: x[column_index], reverse=reverse))

    return sorted_data


def gnome_sort(data, column_index, reverse):
    """Sorts data using the gnome sort algorithm based on the specified column index."""
    n = len(data)
    index = 0  # Start from the first index

    while index < n:
        # If we're at the start or the current element is in the right order, move forward
        if index == 0 or (data[index][column_index] >= data[index - 1][column_index]) != reverse:
            index += 1
        else:
            # Swap the elements if they are in the wrong order
            data[index], data[index - 1] = data[index - 1], data[index]
            index -= 1  # Move one step back

    return data


def cycle_sort(data, column_index, reverse):
    """Sorts data using the cycle sort algorithm based on the specified column index."""
    writes = 0
    for cycle_start in range(len(data) - 1):
        item = data[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, len(data)):
            if (data[i][column_index] < item[column_index]) != reverse:
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
                if (data[i][column_index] < item[column_index]) != reverse:
                    pos += 1
            while data[pos][column_index] == item[column_index]:
                pos += 1
            data[pos], item = item, data[pos]
            writes += 1
    return data


def hybrid_merge_sort(data, column_index, threshold=32, reverse=False):
    """Sorts data using a hybrid merge sort algorithm with insertion sort for small arrays."""
    if len(data) <= threshold:
        # Use insertion sort for small arrays
        return insertion_sort(data, column_index, reverse)
    
    mid = len(data) // 2
    left = hybrid_merge_sort(data[:mid], column_index, threshold, reverse)
    right = hybrid_merge_sort(data[mid:], column_index, threshold, reverse)
    
    return merge(left, right, column_index, reverse)

# You can call this like:
# sorted_data = hybrid_merge_sort(data, column_index)
