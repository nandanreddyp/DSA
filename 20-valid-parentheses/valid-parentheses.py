class Solution:
    def isValid(self, s: str) -> bool:
        stack = []; mapping = {'(':')','{':'}','[':']'}
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack or i != mapping[stack.pop()]:
                    return False
        return not stack