import Group as g

"""
---------- circle linked list ----------
建立循環 linked list
"""
antica = g.Group("L'Antica")    # 新增 3 個Group節點
alstroe = g.Group("ALSTROEMERIA")
hokako = g.Group("放課後クライマックスガールズ")
antica.next = alstroe    # 將Group節點連接一起
alstroe.next = hokako
hokako.next = antica     # 將末端接到第一個節點

ptr = antica
count = 1
n = 6    # 想印幾個節點
while count <= n:
    print(ptr.name)
    ptr = ptr.next
    count+=1