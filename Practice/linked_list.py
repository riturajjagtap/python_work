class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def add_at_beginning(self,item):
        n = Node(item)
        if self.is_empty():
            self.head=n
            print(item," is the very first item added in the list.")
        else:
            n.next=self.head
            self.head=n
            print(item, " added at beginning of list.")

    def add_node(self,item):
        if self.is_empty():
            self.add_at_beginning(item)
        else:
            n = Node(item)
            tmp=self.head
            while(tmp.next!=None):
                tmp=tmp.next
            tmp.next=n
            print(item, " added at the end of list.")

    def display(self):
        if self.is_empty():
            print("Nothing to display. List is empty.")
        else:
            tmp=self.head
            while(tmp!=None):
                print(tmp.data,end=" ")
                tmp=tmp.next

    def remove_from_beginning(self):
        flag=0
        if self.is_empty():
            print("Nothing to remove from List. The list is empty.")
            flag=1
        elif self.head.next==None:
            self.head=None
            p
            flag=1
            print("Deleted the only item in the list. Now the list is empty.")
        else:
            d=self.head.data
            self.head=self.head.next
            print("\n",d," deleted from the beginning of the list.")
            flag=1
        if(flag==0):
            print("Item not found in the list.")

    def remove(self,item):
        flag=0
        if(self.is_empty() or self.head.next == None):
            self.remove_from_beginning(item)
        else:
            tmp=self.head
            while(tmp.next!=None):
                if(tmp.next.data==item):
                    tmp.next=tmp.next.next
                    print("\n",item," deleted from the list.")
                    flag=1
                else:
                    tmp=tmp.next
        if(flag==0):
            print("Item not found in the list.")

def Main():
    l=Linked_List()
    for i in range(10,101,10):
        l.add_node(i)
    l.display()
    l.remove(100)
    l.display()
    l.remove(60)
    l.display()
    l.remove_from_beginning()
    l.display()

if __name__=="__main__":
        Main()