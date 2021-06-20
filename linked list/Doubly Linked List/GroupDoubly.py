import Group
class GroupDoubly(Group.Group):
    def __init__(self, name = None):
        super(GroupDoubly, self).__init__(name)
        self.previous = None
"""
因為是繼承所以要注意傳參數
一開始錯誤的例子
class GroupDoubly(Group):
# TypeError: module() takes at most 2 arguments (3 given)
    def __init__(self, name = None):
        super().__init__(self, name)
# TypeError: __init__() takes from 1 to 2 positional arguments but 3 were given
        self.previous = None
"""