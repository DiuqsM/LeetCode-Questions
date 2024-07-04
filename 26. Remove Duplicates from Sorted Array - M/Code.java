class Solution {
    public int removeDuplicates(int[] nums) {
        //set the pointer to 0
        int j = 0; 
        for(int i = 0; i < nums.length; i++){
            //if the current element is not equal to the pointer element, 
            //increment the pointer and set the current element to the pointer 
            if(nums[i] != nums[j])
            j++; 
            nums[j] = nums[i];
        }
        //return the length of the array
        return j + 1;
    }
}