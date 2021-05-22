import Group_Linked_list as gll
import Group as g

group_linked = gll.Group_Linked_list()
group_linked.head = g.Group("illumination  STARS")
#print(group_linked.head.name)
antica = g.Group("L'Antica")
alstroe = g.Group("ALSTROEMERIA")
hokako = g.Group("放課後クライマックスガールズ")

antica.next = alstroe
alstroe.next = hokako

group_linked.head.next = antica

group_linked.print_list()