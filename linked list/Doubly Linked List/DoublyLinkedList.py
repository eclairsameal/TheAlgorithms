import GroupDoubly as fd
class DoublyLinkedList():
    def __init__(self):
        self.head = None    # Linked List 的首位節點
        self.tail = None    # Linked List 的尾端節點
    def add_ending(self, new_node):
        """將新的節點追加到Linked list最後面"""
        if isinstance(new_node, fd.GroupDoubly):    # 判斷new_node 是不是 GroupDoubly 物件
            if self.head == None:    # 當Linked list 裡是空的話
                self.head = new_node
                new_node.next = None
                new_node.previous = None
                self.tail = new_node
            else:    # 當Linked list 裡有節點存在時
                self.tail.next = new_node    # 將tail指標的next指向new_node
                new_node.previous = self.tail    # 將new_node的previous指向tail指標
                self.tail = new_node    # 將tail指標指向new_node(將tail指標更新成new_node)
        return
    def print_from_head(self):
        """從頭開始列印Linked List"""
        ptr = self.head
        while ptr:
            print(ptr.name)
            ptr = ptr.next

    def print_from_tail(self):
        """從尾開始列印Linked List"""
        ptr = self.tail
        while ptr:
            print(ptr.name)
            ptr = ptr.previous