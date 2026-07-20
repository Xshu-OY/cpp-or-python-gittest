class Node:
    def __init__(self,val:int):
        self.val=val
        self.next=None

def insert(n:Node,P:Node):
    n1=n.next
    n.next=P
    P.next=n1

def remove(n:Node):
    if n.next==None:
        return
    P=n.next
    n1=P.next
    n.next=n1

def access(head:Node,index:int)->Node|None:
    for i in range(index):
        if head==None:
            return None
        head=head.next
    return head

def find(head:Node,target:int)->Node|None:
    if head==None:
        return None
    while head!=None:
        if head.val==target:
            return head
        head=head.next

def findIndex(head:Node,target:int)->int:
    index=0
    while head:
        if head.val==target:
            return index
        head=head.next
        index+=1
    return -1
    

if __name__=="__main__":
    n0=Node(1)
    n1=Node(2)
    n2=Node(3)
    n3=Node(4)

    n0.next=n1
    n1.next=n2
    n2.next=n3  

    print(access(n0,2))
    print(find(n0,3))
    print(findIndex(n0,3))






