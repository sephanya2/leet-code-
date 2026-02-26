class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        
        from collections import Counter
        word_count = Counter(words)
        
        result = []
        
        # We try starting from each possible offset
        for i in range(word_len):
            left = i
            right = i
            curr_count = {}
            count = 0
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1
                    
                    # If word appears more than allowed
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # If valid window
                    if count == total_words:
                        result.append(left)
                else:
                    # Reset window
                    curr_count.clear()
                    count = 0
                    left = right
        
        return result