public class Solution {
    public int removeElement(int[] nums, int val) {
        int j = 0;
        if(nums.length == 0){
            return 0; 
        }
      //loop through every index and put them into the front if they are not equal to value, and shove all the numbers equal to value to the back of the array
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != val){
                nums[j] = nums[i];
                j++; 
            }
        }
        return j;     
    }
}
