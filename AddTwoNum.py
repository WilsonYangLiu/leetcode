import math
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    for lst, idx in [(l1, 0), (l2, 1)]:
        Sum = list()
        Sum.append(0)
        for i in range(len(lst)):
            Sum[idx] += math.pow(10, i)
        print (Sum[0], Sum[1])
        
st = '(2 -> 4 -> 3) + (5 -> 6 -> 4)'
lst = st.replace(' ', '').split('+')
for i in range(len(lst)):
    l = lst[i][1:-1].split('->')
    for j in range(len(l)):
        l[j] = int(l[j])
addTwoNumbers(l[0], l[1])
