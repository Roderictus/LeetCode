def runningSum(nums):
        listasol = []
        sol = 0
        for num in nums:
            sol = sol + num
            listasol.append(sol)

        return listasol

#nums = [ 1,2,3,4]
nums = [1,1,1,1,1]
temp = runningSum(nums)
print(temp)