public class Solution_quick {
    public int removeDuplicates(int[] nums) {
        //creates the first pointer 
        int[][] map = {{0,nums[0]}}; 

      //have the second pointer iterate through the array 
        for(int i = 0; i < nums.length; i++){
            //skip to the next different number
            if(nums[i] != map[0][1])
            //first updates the position of the first pointer 
            map[0][0]++; 

            //swap the first pointer and the second pointer 
            map[0][1] = nums[i]; 
            nums[map[0][0]] = nums[i];
        }
        return map[0][0] + 1;
    }
}
