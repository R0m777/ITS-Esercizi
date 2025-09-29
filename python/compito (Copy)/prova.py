def dedup_stable(nums: list[int]) -> list[int]:
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    return sorted(result)

    
    
    
  
print(dedup_stable([3,4,1,6,4]))