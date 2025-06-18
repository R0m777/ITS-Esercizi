def merge_intervals(intervals:list[list[int]]) -> list[int]:
    intervals.sort()

    if not intervals :
        return []
    
    if len(intervals) == 1:
        return intervals
    
    merged_list = [intervals[0]]

    for interval in intervals[1:]:
        last_merged = merged_list[-1]

        if interval[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], interval[1])

        else:
            merged_list.append(interval)

    return merged_list


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals)) # restituisce [[1, 6], [8, 10], [15,18]]
intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals)) # restituisce [[1, 5]]