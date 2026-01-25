class Solution:
    def isValid(self, s: str) -> bool:
        stack = []; mapping = {'(':')','{':'}','[':']'}
        for i in s:
            if i in mapping.keys():
                stack.append(i)
            else:
                opening = stack.pop() if stack else None
                if not opening or i != mapping[opening]:
                    return False
        return True if not stack else False