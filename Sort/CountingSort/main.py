import CountSort


def main():
    original_list_1 = [0, 2, 5, 3, 7, 9, 10, 3, 7, 6]
    cs1 = CountSort.CountSort(original_list_1)
    print("Original List 1: ")
    print(original_list_1)
    print("Basic counting sorted list of counts: ")
    basic_counting_sort_count_list = cs1.basic_counting_sort_count()
    print(basic_counting_sort_count_list)
    print("Sorting results based on count list: ")
    print(cs1.basic_counting_sort_result(basic_counting_sort_count_list))

    print("----------"*4)
    original_list_2 = [101, 109, 107, 103, 108, 102, 103, 110, 107, 103]
    print("Original List 2: ")
    print(original_list_2)
    cs2 = CountSort.CountSort(original_list_2)
    cs2_optimize_count_list = cs2.optimize_counting_sort_count()
    print("Optimize counting sorted list of counts: ")
    print(cs2_optimize_count_list)
    print("將優化後的計數排序列表轉換成每個數字在結果數組中首次出現的位置: ")
    print(cs2.optimize_counting_sort_result(cs2_optimize_count_list.copy()))

    print("----------" * 4)
    original_list_3 = [1, 4, 1, 2, 5, 2, 4, 1, 8]
    print("Original List 3: ")
    print(original_list_3)
    cs3 = CountSort.CountSort(original_list_3)
    cs3_count_list = cs3.basic_counting_sort_count()
    print("Basic counting sorted list of counts:")
    print(cs3_count_list)
    print("將優化後的計數排序列表轉換成每個數字在結果數組中首次出現的位置: ")
    cs3_sum_count_list = cs3.counting_sort_sum_count(cs3_count_list.copy())
    print(cs3_sum_count_list)
    print("對應原本數組的位址表: ")
    # 將優化後的計數排序列表轉換成位置
    cs3_position_list = cs3.sum_count_to_position(cs3_sum_count_list.copy())
    print(cs3_position_list)
    print("利用位址表來產生排序: ")
    print(cs3.position_to_sort_result(cs3_position_list.copy()))

    print("----------" * 4)
    original_list_4 = [-1, 4, -1, -2, 5, -2, 4, -1, 8]
    print("Original List 4: ")
    print(original_list_4)
    cs4 = CountSort.CountSort(original_list_4)
    cs4_optimize_count_list = cs4.optimize_counting_sort_count()
    print("Optimize counting sorted list of counts:")
    print([i for i in range(cs4.original_list_min, cs4.original_list_max+1)])
    print(cs4_optimize_count_list)
    # print("將優化後的計數排序列表轉換成每個數字在結果數組中的位置: ")
    # print(cs4.optimize_counting_sort_result(cs4_optimize_count_list.copy()))
    print("將優化後的計數排序列表轉換成每個數字在結果數組中首次出現的位置: ")
    print([i for i in range(cs4.original_list_min, cs4.original_list_max+1)])
    cs4_optimize_sum_count_list = cs4.counting_sort_sum_count(cs4_optimize_count_list.copy())
    print(cs4_optimize_sum_count_list)
    print("對應原本數組的位址表: ")
    # 將優化後的計數排序列表轉換成位置
    cs4_optimize_position_list = cs4.optimize_sum_count_to_position(cs4_optimize_sum_count_list.copy())
    print(cs4_optimize_position_list)
    print("利用位址表來產生排序: ")
    print(cs4.position_to_sort_result(cs4_optimize_position_list.copy()))


if __name__ == '__main__':
    main()
