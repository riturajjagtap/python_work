import linked_list

class manual_stack(Linked_List):
    def __init__(self):
        self.top=None
        super(manual_stack,self).__init__()

    def push(self,item):
        super(manual_stack,self).add_at_beginning(item)

    def pop(self):
        super(manual_stack,self).remove_from_beginning()

    def is_empty(self):
        return super(manual_stack, self).is_empty()

    def display(self):
        super(manual_stack,self).display()

def Main():
    l=manual_stack()
    for i in range(10,101,10):
        l.push(i)
    l.display()
    '''
    l.remove(100)
    l.display()
    l.remove(60)
    l.display()
    l.remove_from_beginning()
    l.display()
'''

if __name__=="__main__":
        Main()