# divide and conquer
class Solution(object):
    def commonPrefix(self, str1, str2):
        result = ''
        i, j = 0, 0
        
        while i <= len(str1) - 1 and j <= len(str2) - 1:
            if str1[i] != str2[j]: # 공통 글자인지 확인
                break
            result += str1[i]
            i, j = i + 1, j + 1
        return result
    
    def longestCommonPrefixHelp(self, strs, low, high):
        if low == high:
            return strs[low]
        
        if high > low:
            mid = low + (high - low) // 2
            
            str1 = self.longestCommonPrefixHelp(strs, low, mid)
            str2 = self.longestCommonPrefixHelp(strs, mid + 1, high)
            
            return self.commonPrefix(str1, str2)
        
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return
        return self.longestCommonPrefixHelp(strs, 0, len(strs) - 1)