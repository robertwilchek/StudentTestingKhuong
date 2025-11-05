public class task2 {

    public static int sum(int[] nums) {
        int total = 0;
        // Set to less than nums.length which will stop at last index
        // Less than AND equal to length of array will go out of bounds
        for (int i = 0; i < nums.length; i++) { 
            total += nums[i];
        }
        return total;
    }

    public static void main(String[] args) {
        int[] data = {2, 3, 5};
        System.out.println(sum(data)); 
    }
}