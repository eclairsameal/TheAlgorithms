import Group_Linked_list as gll
import Group as g

group_linked = gll.Group_Linked_list()    # 宣告 Group_Linked_list 變數
group_linked.head = g.Group("illumination  STARS")    # 設定 Group_Linked_list 變數 head的值
#print(group_linked.head.name)

antica = g.Group("L'Antica")    # 新增 3 個Group節點
alstroe = g.Group("ALSTROEMERIA")
hokako = g.Group("放課後クライマックスガールズ")
antica.next = alstroe    # 將Group節點連接一起
alstroe.next = hokako

group_linked.head.next = antica    # 將新的Group節點串列接到head後
print("初始的Linked list: ")
group_linked.print_list()    # 印出 Group_Linked_list 的所有數值

"""
---------- 實作 add_beginning(self, new_name) ----------
新增 "Straylight" 到第一個節點
"""
print("新增 Straylight 到第一個節點後的Linked list: ")
group_linked.add_beginning("Straylight")
group_linked.print_list()

"""
---------- 實作 add_ending(self, new_name) ----------
新增 "noctchill" 到最後一個節點
"""
print("新增 noctchill 到第一個節點後的Linked list: ")
new_group_linked = gll.Group_Linked_list()    # 宣告 Group_Linked_list 變數
new_group_linked.add_ending("noctchill")
new_group_linked.print_list()