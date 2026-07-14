class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_with_length = []
        for i in strs:
            length = f'{len(i)}#'
            strs_with_length.append(length + i)
        
        s = "".join(strs_with_length)
        return s

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i != len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])    
            answer.append(s[j+1 : length+j+1])
            i = length + j + 1
        return answer
            
        
