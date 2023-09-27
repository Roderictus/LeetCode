#https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(l1, l2):
    # l1.reverse()
    # l2.reverse()
    # l1= int("".join(map(str,l1)))
    # l2= int("".join(map(str,l2)))
    # sol = [int(x) for x in str(l1+l2)]
    # return sol

    def reverse_string_into_number(lista):
        number = 0
        for i in range(0, len(lista)):
            number += lista[len(lista)-i]








l1 = [2,4,3]
l2 = [5,6,4]
temporal = addTwoNumbers(l1,l2)
print(temporal)
