import Group_Linked_list as gll
import Group as g

# 宣告 Group_Linked_list 變數
group_linked = gll.Group_Linked_list()
# 設定 Group_Linked_list 變數 head的值
group_linked.head = g.Group("illumination  STARS")
#print(group_linked.head.name)
# 新增 3 個Group節點
antica = g.Group("L'Antica")
alstroe = g.Group("ALSTROEMERIA")
hokako = g.Group("放課後クライマックスガールズ")
# 將Group節點連接一起
antica.next = alstroe
alstroe.next = hokako
# 將新的Group節點串列接到head後
group_linked.head.next = antica
# 印出 Group_Linked_list 的所有數值
group_linked.print_list()