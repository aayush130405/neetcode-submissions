class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        answer = []

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        sorted_pair = sorted(freq.items(), reverse=True, key=lambda item: item[1])

        for i in range(k):
            answer.append(sorted_pair[i][0])

        return answer