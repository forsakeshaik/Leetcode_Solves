class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for brack in s:
            if brack in ['(', '{', '[']:
                stack.append(brack)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if curr == '(':
                    if brack != ')':
                        return False
                elif curr == '[':
                    if brack != ']':
                        return False
                elif curr == '{':
                    if brack != '}':
                        return False
        if stack:
            return False
        return True       
