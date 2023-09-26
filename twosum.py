def twosum(nums, target):
    sol = []
    for i in range(0,len(nums)):
        print(nums[i])
        nums_minus = nums.copy()
        nums_minus[i] = "a"
        #print(nums_minus)
        #print(nums)

        if target - nums[i] in nums_minus:
            print(f"target {target} - nums[i] {nums[i]} i = {i}")
            sol.append(i)
            sol.append(nums.index(target - nums_minus[i]))
            return sol





#nums = [2,7,11,15]
nums = [3,3]
temp = twosum(nums,6)
print(temp)
