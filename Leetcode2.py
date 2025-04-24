#142
class listnode(object):
    def __init__(self):
        self.val = x
        self.next =None
class solution(object):
    def detectcycle(self,head):
        if  head is None  or head.next is  None:
            return None
        fast = head
        slow = head
        while(fast is not None and fast.next is None):
            fast = fast.next.next
            slow = slow.next
            if(fast==slow):
                break
        if(fast is None and fast.next is None):
            return None 
        slow = head
        while(fast!=slow):
            slow=slow.next
            fast=fast.next
        return slow 