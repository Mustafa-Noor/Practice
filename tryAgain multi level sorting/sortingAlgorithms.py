def bubble_sort(data, sort_criteria):
    """Sorts data using the bubble sort algorithm based on the specified sort criteria."""
    n = len(data)
    for col_index, reverse in sort_criteria:
        for i in range(n):
            for j in range(0, n - i - 1):
                # Adjust the comparison for the current column and reverse flag
                if (data[j][col_index] > data[j + 1][col_index]) != reverse:
                    data[j], data[j + 1] = data[j + 1], data[j]
    return data


def selection_sort(data, sort_criteria):
    """Sorts data using the selection sort algorithm based on the specified sort criteria."""
    n = len(data)
    for col_index, reverse in sort_criteria:
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                # Adjust the comparison for the current column and reverse flag
                if (data[j][col_index] < data[min_index][col_index]) != reverse:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
    return data


def insertion_sort(data, sort_criteria):
    """Sorts data using the insertion sort algorithm based on the specified sort criteria."""
    for col_index, reverse in sort_criteria:
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and (key[col_index] < data[j][col_index]) != reverse:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
    return data


def merge_sort(data, sort_criteria):
    """Sorts data using the merge sort algorithm based on the specified sort criteria."""
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid], sort_criteria)
    right = merge_sort(data[mid:], sort_criteria)
    return merge(left, right, sort_criteria)


def merge(left, right, sort_criteria):
    """Helper function to merge two halves in merge sort based on sort criteria."""
    result = []
    while left and right:
        for col_index, reverse in sort_criteria:
            if (left[0][col_index] <= right[0][col_index]) != reverse:
                result.append(left.pop(0))
                break
            else:
                result.append(right.pop(0))
                break
    result.extend(left or right)
    return result


def quick_sort(data, sort_criteria):
    """Sorts data using the quick sort algorithm based on the specified sort criteria."""
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if any((x[col_index] < pivot[col_index]) != reverse for col_index, reverse in sort_criteria)]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if any((x[col_index] > pivot[col_index]) != reverse for col_index, reverse in sort_criteria)]
    return quick_sort(left, sort_criteria) + middle + quick_sort(right, sort_criteria)


def counting_sort(data, sort_criteria):
    """Sorts data using the counting sort algorithm based on the specified sort criteria."""
    if not data or not all(isinstance(row[col_index], int) for col_index, _ in sort_criteria for row in data):
        print("Error: Invalid data format for counting sort.")
        return []
    
    min_value = min(data, key=lambda x: x[sort_criteria[0][0]])[sort_criteria[0][0]]
    max_value = max(data, key=lambda x: x[sort_criteria[0][0]])[sort_criteria[0][0]]
    count = [0] * (max_value - min_value + 1)

    for row in data:
        count[row[sort_criteria[0][0]] - min_value] += 1

    output = []
    for i in range(len(count)):
        output.extend([row for row in data if row[sort_criteria[0][0]] == (min_value + i)] * count[i])

    return output


def radix_sort(data, sort_criteria):
    """Sorts data using the radix sort algorithm based on the specified sort criteria."""
    for col_index, _ in sort_criteria:
        for row in data:
            row[col_index] = int(row[col_index])

        max_value = max(data, key=lambda x: x[col_index])[col_index]
        exp = 1
        while max_value // exp > 0:
            data = counting_sort_for_radix(data, col_index, exp)
            exp *= 10
    return data


def counting_sort_for_radix(data, column_index, exp):
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


def bucket_sort(data, sort_criteria):
    """Sorts data using the bucket sort algorithm based on the specified sort criteria."""
    if not data:
        return data

    for col_index, _ in sort_criteria:
        for row in data:
            row[col_index] = int(row[col_index])

        min_value = min(row[col_index] for row in data)
        max_value = max(row[col_index] for row in data)

        bucket_count = 10
        bucket_size = (max_value - min_value + 1) // bucket_count
        buckets = [[] for _ in range(bucket_count)]

        for i in range(len(data)):
            value = data[i][col_index]
            index = (value - min_value) // bucket_size if bucket_size > 0 else 0
            if index >= bucket_count:
                index = bucket_count - 1
            buckets[index].append(data[i])

        sorted_data = []
        for bucket in buckets:
            sorted_data.extend(sorted(bucket, key=lambda x: x[col_index]))  # Ascending order

    return sorted_data


def gnome_sort(data, sort_criteria):
    """Sorts data using the gnome sort algorithm based on the specified sort criteria."""
    n = len(data)
    index = 0  # Start from the first index

    while index < n:
        # If we're at the start or the current element is in the right order, move forward
        if index == 0 or all((data[index][col_index] >= data[index - 1][col_index]) != reverse for col_index, reverse in sort_criteria):
            index += 1
        else:
            # Swap the elements if they are in the wrong order
            data[index], data[index - 1] = data[index - 1], data[index]
            index -= 1  # Move one step back

    return data


def cycle_sort(data, sort_criteria):
    """Sorts data using the cycle sort algorithm based on the specified sort criteria."""
    writes = 0
    for cycle_start in range(len(data) - 1):
        item = data[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, len(data)):
            if any((data[i][col_index] < item[col_index]) != reverse for col_index, reverse in sort_criteria):
                pos += 1
        if pos == cycle_start:
            continue
        while data[pos][col_index] == item[col_index]:
            pos += 1
        data[pos], item = item, data[pos]
        writes += 1
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(data)):
                if any((data[i][col_index] < item[col_index]) != reverse for col_index, reverse in sort_criteria):
                    pos += 1
            while data[pos][col_index] == item[col_index]:
                pos += 1
            data[pos], item = item, data[pos]
            writes += 1
    return data


def hybrid_merge_sort(data, sort_criteria, threshold=32):
    """Sorts data using a hybrid merge sort algorithm with insertion sort for small arrays."""
    if len(data) <= threshold:
        return insertion_sort(data, sort_criteria)
    
    mid = len(data) // 2
    left = hybrid_merge_sort(data[:mid], sort_criteria, threshold)
    right = hybrid_merge_sort(data[mid:], sort_criteria, threshold)
    
    return merge(left, right, sort_criteria)

# Example usage:
# sorted_data = bubble_sort(data, [(0, False), (1, True)])  # Sort by column 0 ascending and column 1 descending
