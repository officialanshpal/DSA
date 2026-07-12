# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Dummy head acts as a placeholder for the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Continue loop as long as there are nodes to process or a carry remains
        while l1 or l2 or carry:
            # Get values from the current nodes, defaulting to 0 if a list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and updated carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the single-digit value
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes if available
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy_head.next