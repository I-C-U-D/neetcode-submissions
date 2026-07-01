class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        nums = sorted(nums)
        k_freq = defaultdict(list)

        for item in nums:
            if item not in k_freq[nums.count(item)]:
                k_freq[nums.count(item)].append(item)
        
        k_freq_sorted = sorted(k_freq)
        k_freq_sorted.reverse()
        
        output = []
        for item in k_freq_sorted:
            if len(output) < k:
                output += k_freq[item]

        return output