class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for i in strs:
            length = f'{len(i)}#'
            s.append(length + i)
        return "".join(s)

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            answer.append(s[j+1 : length+j+1])

            i = length + j + 1

        return answer
