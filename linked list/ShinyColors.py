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

group_linked.print_list()    # 印出 Group_Linked_list 的所有數值