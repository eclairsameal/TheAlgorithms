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
        last_ptr = self.head         # 先將最後節點的指標指向head
        while last_ptr.next:         # 移動最後節點的指標直到Linked list的最後
            last_ptr = last_ptr.next
        last_ptr.next = new_group    # 將最後節點的next 指向新的節點
    
    def add_between(self, pre_node, new_name):
        """將新的節點插入到Linked list的中間"""
        if pre_node == None:
            print("沒有前一個節點")
            return
        new_group = g.Group(new_name)    # 先建立新的節點
        new_group.next = pre_node.next   # 新的節點先指向後面的節點
        pre_node.next = new_group        # 將前節點的next指向新的節點
    def remove_node(self, rmname):
        ptr = self.head    # 暫時指向Linked list的指標
        if ptr:
            if ptr.name == rmname:            # 想刪除的節點是head
                self.head = self.head.next    # 直接將head指向head的下一個節點
                return
        while ptr:
            if ptr.name == rmname:
                break
            prev = ptr        # 設一個前一節點的指標
            ptr = ptr.next
        if ptr == None:       # 當ptr為Linked list的末端
            return            # 找不到刪除的資料所以返回
        prev.next = ptr.next  # 找到想刪除的節點所以將前一節點指向下一節點