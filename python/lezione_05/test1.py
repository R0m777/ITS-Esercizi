def find_disappeared_numbers(nums:list[int]) -> list[int]:
    n = len(nums)
    
    all_nums = set(range(1, n)) 
    
    nums_set = set(nums)
    
    missing_nums = list(all_nums - nums_set) 
    missing_nums.sort()
    
    return missing_nums

print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))