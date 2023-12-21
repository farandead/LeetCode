class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def getVal(self):
        return self.val
    def getNext(self):
        return self.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        listnode2 = ListNode(2,None)
        listnode1 = ListNode(1,listnode2)
        
        print(listnode1.getNext().getVal())

solution  = Solution()
print(solution.addTwoNumbers([1,2,3],[1,2,3]))
