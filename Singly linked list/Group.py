class Group():
  """節點"""
  def __init__(self, name = None):
    self.data = name
    self.next = None

# 實作節點

illumina = Group("illumination  STARS")
antica = Group("L'Antica")
alstroe = Group("ALSTROEMERIA")
hokako = Group("放課後クライマックスガールズ")

illumina.next = antica
antica.next = alstroe
alstroe.next = hokako

ptr = illumina # 建立指標節點

# 遊歷節點
while ptr:
  print(ptr)
  ptr = ptr.next
