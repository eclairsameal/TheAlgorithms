import DoublyLinkedList as d
import GroupDoubly as g

sc_dll = d.DoublyLinkedList()    # 宣告空的DoublyLinkedList物件

antica = g.GroupDoubly("L'Antica")    # 新增 3 個GroupDoubly節點
alstroe = g.GroupDoubly("ALSTROEMERIA")
hokako = g.GroupDoubly("放課後クライマックスガールズ")

for i in [antica, alstroe, hokako]:
    sc_dll.add_ending(i)    # 將GroupDoubly節點加到DoublyLinkedList裡
    sc_dll.print_from_head()
sc_dll.print_from_tail()