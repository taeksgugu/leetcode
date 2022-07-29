class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        brackets={'}':'{',')':'(',']':'['}
        for bracket in s:
            if bracket in brackets.values(): #Opening bracket 
                stack.append(bracket)
            else:# Closing bracket
                if stack and brackets[bracket]==stack[-1] :  
                    stack.pop()
                else: 
                    return False
        
        if stack:
            return False
        return True
