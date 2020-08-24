class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    def pushBeg(self,newdata):
        new_node=Node(newdata)
        new_node.next=self.head
        self.head=new_node
    def pushEnd(self,newdata):
        new_node=Node(newdata)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def pushBef(self,prevnode,newdata):
        if prevnode is None:
            print("The node does not exists")
            return
        new_node=Node(newdata)
        new_node.next=prevnode.next
        prevnode.next=new_node
    def deleteNode(self,key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
        while temp is not None:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            return
        prev.next=temp.next
        temp=None
if __name__=='__main__':
    llist=LinkedList()
    llist.head=Node(int(input()))
    second=Node(int(input()))
    third=Node(int(input()))
    llist.head.next=second
    second.next=third
    print("1.Insert at beginning\n2.Insert after the node\n3.Insert at the end\n4.Delete a node")
    opt=int(input())
    if opt==1:
        llist.pushBeg(int(input()))
        llist.printList()
    elif opt==2:
        llist.pushBef(llist.head.next,int(input()))
        llist.printList()
    elif opt==3:
        llist.pushEnd(int(input()))
        llist.printList()
    elif opt==4:
        llist.deleteNode(int(input()))
        llist.printList()
    else:
        print("Option Invalid")
