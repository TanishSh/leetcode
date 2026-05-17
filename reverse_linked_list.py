# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        curr = head
        while curr is not None:
            arr.append(curr)
            curr = curr.next
        
        reversed_arr = arr[::-1]
        
        for i, val in enumerate(reversed_arr): 
            if i+1 < len(reversed_arr):
                val.next = reversed_arr[i+1]
            else:
                val.next = None

        if len(reversed_arr) > 0:
            return reversed_arr[0]

    

        

        
        