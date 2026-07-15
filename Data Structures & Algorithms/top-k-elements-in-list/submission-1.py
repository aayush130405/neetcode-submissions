class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        answer = []
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        sorted_pairs = sorted(freq.items(), reverse=True, key=lambda item: item[1])

        for i in range(k):
            answer.append(sorted_pairs[i][0])

        return answer
        