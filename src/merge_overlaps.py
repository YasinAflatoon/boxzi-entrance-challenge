def merge_overlaps(ranges):
    if not ranges:
        return []

    ranges.sort(key=lambda x: x[0])

    merged = [ranges[0]]

    for current in ranges[1:]:
        previous = merged[-1]

        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)

    return merged


intervals = [(2, 7), (1, 6), (8, 10)]
print(merge_overlaps(intervals))