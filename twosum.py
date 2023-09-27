def twosum(nums, target):
    tempnums = nums.copy()
    for i in range(0, len(nums)):
        tempnum = nums[i]
        tempnums[tempnums.index(tempnum)] = "a"
        if target - nums[i] in tempnums:
            for numero in tempnums:
                if target - nums[i] == numero:
                    lista = [i, tempnums.index(numero)]
                    return lista

class Solution(object):
    def twoSum(self, nums, target):
        tempnums = nums.copy()
        for i in range(0, len(nums)):
            tempnum = nums[i]
            tempnums[tempnums.index(tempnum)] = "a"
            if target - nums[i] in tempnums:
                for numero in tempnums:
                    if target - nums[i] == numero:
                        lista = [i, tempnums.index(numero)]
                        return lista



#nums = [2,7,11,15]
#nums = [3,3]
nums = [3,2,4]
temp = twosum(nums,6)
print(temp)
