class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]

        for i in range(1,len(nums)):
            temp_max = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    temp_max = max(temp_max, dp[j])

            dp.append(temp_max+1)

        return max(dp)