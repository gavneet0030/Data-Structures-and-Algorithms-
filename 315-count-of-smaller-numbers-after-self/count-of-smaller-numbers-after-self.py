from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        indexed = list(enumerate(nums))

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    result[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                result[left[i][0]] += j
                merged.append(left[i])
                i += 1

            merged.extend(right[j:])
            return merged

        merge_sort(indexed)
        return result