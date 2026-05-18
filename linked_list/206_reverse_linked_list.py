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
        
        reversed_arr = arr[::-1] # reverse the list
        
        for i, val in enumerate(reversed_arr):  # get the index and the values of reversed 
            if i+1 < len(reversed_arr): # make sure next index is less than length
                val.next = reversed_arr[i+1] # next pointer points to the next in reverse list
            else:
                val.next = None

        if len(reversed_arr) > 0: # only return head if length > 0
            return reversed_arr[0] 

    

        

        
        