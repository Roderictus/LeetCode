def strStr(haystack, needle):
    sol = -1
    for j in range(0, len(haystack)):
        print(haystack[j])



        # if haystack[j] == needle[0]:
        #     for i in range(0, len(needle)):
        #         if needle[i] == haystack[j+i]:
        #             print(j,i)
        #             print(needle[i])
        #             if needle[i] == needle[-1]:
        #                 sol = j
        #                 return sol
        #             else:
        #                 pass
        #         else:
        #             pass
        # else:
        #     print("no")
        return sol

temp = strStr("enelaguaclara", "ela")
print(temp)