class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in range(len(s)):
            if not stack:
                if s[i] in close_to_open.values():
                    stack.append(s[i])
                else:
                    return False
            else:
                if s[i] in close_to_open.values():
                    stack.append(s[i])
                else:
                    if stack[-1] == close_to_open[s[i]]:
                        stack.pop()
                    else:
                        return False

        if not stack:
            return True
        else:
            return False 