class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        
        seen_digit = False
        seen_dot = False
        seen_exp = False
        
        for i in range(len(s)):
            char = s[i]
            
            if char.isdigit():
                seen_digit = True
            
            elif char in ['+', '-']:
                # Sign allowed only at start OR just after exponent
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            
            elif char == '.':
                # Dot not allowed after exponent or twice
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            
            elif char in ['e', 'E']:
                # Exponent must appear once and after a number
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False  # Need digit after exponent
            
            else:
                return False
        
        return seen_digit