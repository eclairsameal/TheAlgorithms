import Group as g
class Group_Linked_list():
    def __init__(self):
        self.head = None
    
    def print_list(self):
        """print Linked list"""
        ptr = self.head
        while ptr:
            print(ptr.name)
            ptr = ptr.next
    
    def add_beginning(self, new_name):
        """將新的節點插入第一個節點"""
        new_group = g.Group(new_name)
        new_group.next = self.head
        self.head = new_group