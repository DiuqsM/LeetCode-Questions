class solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        #check if they have the same length 
        if(len(s) != len(t)):
            return False;

        word1 = {}; 
        word2 = {}; 

        #I want to iterate though all the characters in both words once 
        # compare count the amount of character in both words 
        # compare both dictionaries after counting all the characters in both words 
        for x in range(len(s)): 
            if(s[x] in word1): 
                word1[s[x]] += 1
            else:
                word1[s[x]] = 1

            if(t[x] in word2): 
                word2[t[x]] += 1
            else: 
                word2[t[x]] = 1
        
        return (word1 == word2)
    
    # Time Complexity: O(N)
    # space Complexity: O(N)

    # -------------------------------------------------------------------
    # more time efficient solution:
    # sort both words and compare them
    def are_anagrams(s, t):
        return sorted(s) == sorted(t)


    # more space Efficinet Solution
    # instead of using dictionary, they used an array to count 
    # Space: O(1)
    def are_anagrams(s, t):
        # Check if the strings have the same length
        if len(s) != len(t):
            return False

        # Array for counting character frequencies (assuming lowercase letters only)
        counts = [0] * 26

        # Iterate through all characters in both strings
        for x in range(len(s)):
            # This is to balance the count of letters
            counts[ord(s[x]) - ord('a')] += 1  # Increment count for s
            counts[ord(t[x]) - ord('a')] -= 1  # Decrement count for t

        # If all counts are zero, the two words are anagrams
        return all(count == 0 for count in counts)
    

