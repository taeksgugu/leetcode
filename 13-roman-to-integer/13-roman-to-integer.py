class Solution(object):
    def romanToInt(self, s):
        dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        answer = 0
        past = 'I'
        for current in s[::-1]:
            answer = answer - dictionary[current] if dictionary[current] < dictionary[past] else answer + dictionary[current]
            past = current
            
        return answer

    