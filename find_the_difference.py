def findTheDifference(s, t):
    for i in range(len(sorted(list(t)))):
        try:
            if sorted(list(s))[i] != sorted(list(t))[i]:
                return sorted(list(t))[i]
        except:
            return sorted(list(t))[-1]








temp = findTheDifference("aca", "caca")
#temp = findTheDifference("a", "aa")
print(temp)

# tres = set(t) - set(s)
# sol = [item for item in tres]
# if sol[0] != "":
#     return sol[0]
# else