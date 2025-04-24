#141
class listnode(object):
    def __init__(self):
        self.val = x
        self.next =None
class solution(object):
    def hascycle(self,head):
        fast=head
        slow=head
        while(fast is not None and fast.next is not None):
            slow=slow.next
            fast=fast.next
            if(fast==slow):
                return True
        return False