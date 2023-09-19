
def mergeAlternately(word1, word2):
    sol = ""
    largo = len(word1)+len(word2)
    for i in range(0,largo-1):
        try:
            sol = sol + word1[i]
        except:
            pass
        try:
            sol = sol + word2[i]
        except:
            pass
        print(sol)
    return sol





temp = mergeAlternately("aaaaaaa", "bb")
print(temp)