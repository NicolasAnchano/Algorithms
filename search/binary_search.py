def binary_search(array, target_value):
    start = 0
    end = len(array) - 1
    while  start < end:
        mid = (end + start) // 2
        value = array[mid]
        if value == target_value:
            return mid
        elif value < target_value:
            start = mid + 1
        else:
            end = mid - 1
    if array[start] != target_value:
        # devuelvo -1 si no existe el valor
        return -1
    return start
