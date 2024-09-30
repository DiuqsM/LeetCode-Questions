
def groupAnagrams(strs: list[str]) -> list[list[str]]:

    returnList = [[strs[0]]] 

    # iterate though strs 
    for x in range(1, len(strs)): 

        # iterate though returnList to check if the current strs[x] belongs to that group 
        for i in range(len(returnList)):
            if(isAnagram(returnList[i][0], strs[x])): 
                print('appended ' + strs[x] + " in " + returnList[i][0] + " at " + str(i))
                returnList[i].append(strs[x])
                break

            # after the last group have been checked and there is still not anagram, make a new group 
            elif(i == len(returnList) - 1):
                print('new ' + strs[x] + " at " + str(i))
                returnList.append([strs[x]])
                break

    return returnList

        

def isAnagram(s: str, t: str) -> bool:
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

# testing 
input = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(input))