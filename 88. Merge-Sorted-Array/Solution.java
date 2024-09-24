public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        ArrayList<Integer> array = new ArrayList<>();
        //adds both arrays to the arraylist
        for(int i = 0; i < m; i++){
            array.add(nums1[i]);
        } 
        for(int i = 0; i < n; i++){
            array.add(nums2[i]); 
        }
        //sort the array list
        Collections.sort(array);

        //copy all the items from the array into nums1
        for(int i = 0; i < (m + n); i++){
            nums1[i] = array.get(i); 
        }
    }
}
