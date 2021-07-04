def createBinaryTree(tree, data):
    for i in range(len(data)):
        tree_index = 0    # 索引 = 0 代表根節點
        if i == 0:    # 當儲放第一筆資料時
            tree[tree_index] = data[i]  # 將第一筆資料放在根節點
        else:
            while tree[tree_index]:    # 當while結束時表示找到儲存資料的索引
                if data[i] > tree[tree_index]:    # 資料大於索引資料向右找
                    tree_index = (2 * tree_index) + 2    # 向右找
                else:
                    tree_index = (2 * tree_index) + 1    # # 向左找
        tree[tree_index] = data[i]
        print("{} -> {}".format(data[i], tree))    # 顯示建立過程
                    
number_list = [10, 21, 5, 9, 13, 28]    # 王者歸來的例子
k = 3    # 樹高
# number_list = []
binary_tree_array = [0] * (2**(k) -1)    # 利用樹高計算最多會有幾個節點
createBinaryTree(binary_tree_array, number_list)
for i, t in enumerate(binary_tree_array):
    print("index[{}] = {}".format(i, t)) 