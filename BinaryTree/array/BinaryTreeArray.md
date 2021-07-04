# Binary Tree - Array

利用Array建立二元樹時，會從根節點開始由上到下，同一層的話是從左到右來儲存節點的資料,節點為空值時則保留Array空間。

```
節點的索引: index
左子節點的索引: (2 * index) + 1
右子節點的索引: (2 * index) + 2
父節點的索引: (index - 1) / 2
```

完全二元樹: 使用Array來儲存二元樹資料結構是不錯的方法，特別是堆積樹。

稀缺二元樹(缺了很多節點的二元樹): 使用Array來儲存二元樹資料結構，會浪費很多儲存空間。 

**Example**

使用number_list 裡的數字來建立二元樹。
```python
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
```
