from typing import List


class CountSort:
    def __init__(self, _o_list: List[int]):
        """

        Args:
            _o_list (List[int]): 想排序的 list
        """
        self.original_list = _o_list
        self.original_list_max = max(self.original_list)
        self.original_list_min = min(self.original_list)

    def basic_counting_sort_count(self) -> List[int]:
        """
        產生 counting sort 演算法累加後的計數數組（最基礎的方法）
        Returns:
            List[int]: 計數數組
        """
        count_list = [0] * (self.original_list_max + 1)
        # print(count_list)
        for n in self.original_list:
            count_list[n] += 1
        return count_list.copy()

    def basic_counting_sort_result(self, count_list: List[int]) -> List[int]:
        """
        利用計數數組（count_list）產生 original_list 排序後的結果
        Args:
            count_list: counting sort 演算法累加後的計數數組

        Returns:
            List[int]: 利用計數數組產生排序後的結果
        """
        result_list = [0] * len(self.original_list)
        j = 0
        for i in range(len(count_list)):
            while count_list[i] > 0:
                result_list[j] = i
                count_list[i] -= 1
                j += 1
        return result_list.copy()

    def optimize_counting_sort_count(self) -> List[int]:
        """
        產生 counting sort 演算法累加後的計數數組（解決基礎版空間浪費）
        當想排序的數組裡數值很大，沒有小的數值的狀況，可以節省空間
        Returns:
            List[int]: 計數數組
        """
        count_list = [0] * (self.original_list_max - self.original_list_min + 1)
        # print(count_list)
        for n in self.original_list:
            count_list[n - self.original_list_min] += 1
        return count_list.copy()

    def optimize_counting_sort_result(self, count_list: List[int]) -> List[int]:
        """
        利用計數數組（count_list）產生 original_list 排序後的結果
        Args:
            count_list: counting sort 演算法累加後的計數數組（optimize_counting_sort）
        Returns:
            List[int]: 利用計數數組產生排序後的結果
        """
        result_list = [0] * len(self.original_list)
        j = 0
        for i in range(len(count_list)):
            while count_list[i] > 0:
                result_list[j] = i + self.original_list_min  # 補上被減去的最小值
                count_list[i] -= 1
                j += 1
        return result_list.copy()

    @staticmethod
    def counting_sort_sum_count(count_list: List[int]) -> List[int]:
        """
        將優化後的計數排序列表轉換成每個數字在結果數組中首次出現的位置
        Examples:
            count_list = [0, 3, 2, 0, 2, 1, 0, 0, 1]
            結果數組中首次出現的位置: [0, 3, 5, 5, 7, 8, 8, 8, 9]
        Args:
            count_list: counting sort 演算法累加後的計數數組（optimize_counting_sort）
        Returns:
            List[int]: 數字在結果數組中的位置數組
        """
        # print(count_list)
        sum_count_list = [sum(count_list[:i+1]) for i in range(len(count_list))]
        return sum_count_list.copy()

    def sum_count_to_position(self, sum_count_list: List[int]) -> List[int]:
        """
        利用首次出現的位置的list轉換成對應原本數組的位址表（非空間優化的版本）
        Examples:
            sum_count_list = [0, 3, 5, 5, 7, 8, 8, 8, 9]
            對應原本數組的位址表: [0, 5, 1, 3, 7, 4, 6, 2, 8]
        Args:
            sum_count_list: 首次出現的位置的list（counting_sort_sum_count）
        Returns:
            List[int]: 數字在結果數組中的位置數組
        """
        position_list = [0] * len(self.original_list)
        for i in range(len(self.original_list)-1, -1, -1):
            position_list[i] = sum_count_list[self.original_list[i]] - 1
            sum_count_list[self.original_list[i]] -= 1  # 找到一個所以要減一
        return position_list

    def optimize_sum_count_to_position(self, sum_count_list: List[int]) -> List[int]:
        """
        利用首次出現的位置的list轉換成對應原本數組的位址表（空間優化的版本）
        Examples:
            sum_count_list = [2, 5, 5, 5, 5, 5, 7, 8, 8, 8, 9]
            對應原本數組的位址表: [2, 5, 3, 0, 7, 1, 6, 4, 8]
        Args:
            sum_count_list: 首次出現的位置的list（counting_sort_sum_count）
        Returns:
            List[int]: 數字在結果數組中的位置數組
        """
        position_list = [0] * len(self.original_list)
        # print(list(range(len(self.original_list)-1, -1, -1)))
        for i in range(len(self.original_list)-1, -1, -1):
            position_list[i] = sum_count_list[self.original_list[i] - self.original_list_min] - 1
            sum_count_list[self.original_list[i] - self.original_list_min] -= 1  # 找到一個所以要減一
        return position_list

    def position_to_sort_result(self, position_list: List[int]) -> List[int]:
        """
        利用計數數組（position_list）產生 original_list 排序後的結果
        Args:
            position_list: 對應原本數組的位址表(optimize_sum_count_to_position or sum_count_to_position)
        Returns:
            List[int]: 利用對應原本數組的位址表產生排序後的結果
        """
        result_list = [0] * len(self.original_list)
        for i in range(len(position_list)):
            result_list[position_list[i]] = self.original_list[i]
        return result_list.copy()