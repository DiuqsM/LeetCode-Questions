class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        diction = {} 
        # [key, value]
        # key = element
        # value = index

        # sets up the dictionary 
        for i in range(len(nums)):
            diction[nums[i]] = i

        for x in range(len(nums)):
            # use the complement to find the other number 
            complement = target - nums[x]
            # the index cannot be itself 
            if((complement in diction) and (x != diction[complement])):
                return [x, diction[complement]]
        
    # testing
    list1 = [3,4,5,6]
    print(twoSum(list1, 7))

    # Time complexity: O(N)
    # Space xomplexity: O(N)