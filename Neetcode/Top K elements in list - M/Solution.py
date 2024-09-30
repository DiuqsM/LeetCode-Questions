def topKFrequent(nums: list[int], k: int) -> list[int]:
    diction = {} 
    retunList = []
    # count the numbers in a dictionary 
    for x in nums:
        if(x in diction):
            diction[x] += 1
        else: 
            diction[x] = 1

    # O(n log(n))
    # key=lambda key: rec[key] -> sorting the values
    # key=lambda key: key -> sorting the key 
    s = sorted(diction, key=lambda x: diction[x], reverse=True)

    for i in range(k):
        retunList.append(s[i])

    return retunList

# testing 
list = [1, 1, 1, 2, 3, 3, 3]
print(topKFrequent(list, 2))

# time complexity: O(n log(n))
# space complxity: O(n)