target = int(input().strip())
nums = list(map(int, input().split()))

def twoSum(nums, target):
    hash_map = {}  # number -> index
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[nums[i]] = i

result = twoSum(nums,target)
if result:
    print(result[0], result[1])
else:
    print("No solution")
