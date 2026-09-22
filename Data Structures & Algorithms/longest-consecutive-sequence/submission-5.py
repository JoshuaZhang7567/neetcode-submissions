class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = sorted(list(set(nums)))
    

        max_length = 0
        length = 0

        if nums == []:
            return 0

        for i in range(len(nums_set)-1):
            length += 1
            if nums_set[i+1] != nums_set[i]+1:
                if max_length < length:
                    max_length = length
                length = 0
        
        if max_length < length+1:
            max_length = length+1

        return max_length

        