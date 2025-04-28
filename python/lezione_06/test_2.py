
def rounded_average(numbers:list[int]) -> int:
    if not numbers:
        return 0
    return round(sum(numbers) / len(numbers))
    

print(rounded_average([1, 1, 2, 2]))


