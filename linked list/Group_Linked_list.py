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
        new_group = g.Group(new_name)    # 先建立新的節點
        new_group.next = self.head    # 將原本的節點接到新的節點後
        self.head = new_group         # 將新的節點設為head

    def add_ending(self, new_name):
        """將新的節點追加到Linked list最後面"""
        new_group = g.Group(new_name)    # 先建立新的節點
        if self.head == None:        # 如果為True的話，表示Linked list是空的
            self.head = new_group    # 直接將head指向新的節點
            return
        last_ptr = self.head         # 先將最後節點的指標指向hand
        while last_ptr.next:         # 移動最後節點的指標直到Linked list的最後
            last_ptr = last_ptr.next
        last_ptr.next = new_group    # 將最後節點的next 指向新的節點