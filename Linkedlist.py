class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class LinkedList:
    def __init__ (self):
        
        self.Head=None
    def insert(self,val):
        if(not self.Head):
            new_node=Node(val)
            self.Head=new_node
        else:
            temp=self.Head
            while(temp.next):
                temp=temp.next
            new_node=Node(val)
            temp.next=new_node
        print("{} is succesfully inserted" .format(val))
    def display(self):
        res=[]
        temp=self.Head
        
        while(temp):
            res.append(temp.data)
            temp=temp.next
        print("----->".join(map(str,res)))

a=LinkedList()
a.insert(100)
a.insert(200)
a.insert(300)
a.insert(400)
a.display()
