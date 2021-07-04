# BinaryTree
二元樹

一種樹狀的資料結構，每個節點可以存3個值。

```
數據本身(data)
左邊指標(left)
右邊指標(right)
```

## 組成結構

最上方的的節點稱為根節點(root node)。

每個節點最多可以有2個子節點(左邊指標跟右邊指標)，可以只有一個或沒有節點。

沒有子節點被稱為葉節點(leaves node)。

二元樹的深度(depth)可以用層來定義，根節點為第1層，第i層最多會有2**(i-1)的節點。

## 樹的分類

Full Binary Tree (滿二元樹):除了葉節點以外，每個節點都有兩個子節點。

Complete Binary Tree (完全二元樹):各層節點全滿，除了最後一層，最後一層節點全部靠左。

Perfect Binary Tree (完美二元樹):各層節點全滿。同時也是 full binary tree 和 complete binary tree 。

Balanced Binary Tree (平衡二元樹):每個節點的左右兩子樹高度差都不超過一的二元樹。

## 實作 Binary Tree

實作 Binary Tree 一般分為兩種:

1. [陣列]()

2. [鏈結串列(Linked List)]()

## 參考

[演算法筆記](http://web.ntnu.edu.tw/~algo/BinaryTree.html)
