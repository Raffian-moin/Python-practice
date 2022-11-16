from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        for index1, num in enumerate(nums):
            for index2, value  in enumerate(nums):
                sum = value + num
                if sum == target and index1 != index2:
                    if index1 not in new_list:
                        new_list.append(index1)
                    if index2 not in new_list:
                        new_list.append(index2)
                sum = 0
        return new_list

solution = Solution()
print(solution.twoSum([3,2,4], 6))