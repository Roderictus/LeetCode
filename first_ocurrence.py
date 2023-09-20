def strStr(haystack, needle):
    sol = -1
    try:
        for j in range(0, len(haystack)):
            if haystack[j] == needle[0]:
                k = j
                #print(f"esto es j {j}")
                for i in range(0, len(needle)):
                    if i == len(needle) -1 and haystack[k] == needle[-1]:
                        sol = j
                        return sol
                    elif needle[i] == haystack[k]:
                        k = k+1
                    else:
                        break
    except:
        return sol
    return sol

temp = strStr("aab", "abbab")
print(temp)