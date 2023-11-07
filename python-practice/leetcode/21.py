'''
Given two sorted linked lists, merge them into a single sorted linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(list1: ListNode, list2: ListNode):
        dummy = ListNode() # Placeholder node used to simplify the code for handling the merged list.
        tail = dummy # Initially set to dummy, and it keeps track of the last node in the merged list.

        while list1 and list2: # Use a while loop to iterate through both list1 and list2.
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # After while loop, remaining list might still have remaining elements.
        if list1:
            tail.next = list1
        elif list2:
            tail.next= list2
    
        # Return the next of the dummy node, which is the merged list
        return dummy.next

# Create linked lists list1 and list2 with individual nodes
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)

list2 = ListNode(3)
list2.next = ListNode(4)
list2.next.next = ListNode(5)

# Merge the lists and store the result in merged_list
merged_list = Solution.mergeTwoLists(list1, list2)

# Print the merged list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next

'''
Compare node values and merge (Line 15-22):
If list1.val is less than list2.val, it means that the current node in list1 should come before the current node in list2 in the merged list.
In this case, we update tail.next to point to the current node in list1, and then we move list1 to its next node.

If list2.val is less than or equal to list1.val, it means that the current node in list2 should come before or at the same position as the current node in list1.
In this case, we update tail.next to point to the current node in list2, and then we move list2 to its next node.

In either case, tail is updated to the node that was just added to the merged list.
'''