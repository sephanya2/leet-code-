class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_ptr = 0
        p_ptr = 0
        star_idx = -1
        match = 0
        
        while s_ptr < len(s):
            
            # Case 1: characters match OR '?'
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            
            # Case 2: '*' found
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                match = s_ptr
                p_ptr += 1
            
            # Case 3: mismatch but previous '*' exists
            elif star_idx != -1:
                p_ptr = star_idx + 1
                match += 1
                s_ptr = match
            
            # Case 4: mismatch and no '*'
            else:
                return False
        
        # Check remaining characters in pattern
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
        
        return p_ptr == len(p)