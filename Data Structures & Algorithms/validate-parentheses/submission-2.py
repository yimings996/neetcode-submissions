class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cp = { ")" : "(", "]" : "[", "}" : "{" }
        
        for i in s:
            if i in cp:
                if stack and stack.pop() == cp[i]:
                    continue
                else:
                    return False
                
            else:
                stack.append(i)
        
        return not stack