class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        k = str(x)
        if len(k) % 2 == 1:
            for i in range(len(k)//2 + 1):
                if k[i] != k[-(i+1)]:
                    return False
                    break
                else:
                    qq = 0
        else:
            for i in range(len(k)//2):
                if k[i] != k[-(i+1)]:
                    return False
                    break 
                else:
                    qq = 0
        
        if qq == 0:
            return True
        