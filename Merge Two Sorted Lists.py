class Solution:
    def mergeTwoLists(self, list1,list2):
        dummy=ListNode()
        temp=dummy
        while list1 and list2:
            if list1.val<list2.val:
                temp.next=ListNode(list1.val)
                list1=list1.next
            else:
                temp.next=ListNode(list2.val)
                list2=list2.next
            temp=temp.next
        temp.next=list1 or list2
        return dummy.next
