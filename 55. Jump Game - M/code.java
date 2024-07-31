class Solution {
    public boolean canJump(int[] nums) {
        int reachable = 0; 
        for(int i = 0; i < nums.length; i++){
            if(i > reachable){
                //This checks if the current position i is farther than what we can reach (reachable). If it is, 
                //it means we can't jump to this position from any of the previous positions, so we return false.
                return false;
            }
            //This updates the reachable variable to the farthest position we can reach from the current position
            reachable = Math.max(reachable, i + nums[i]);
        }
        return true; 
    }
}