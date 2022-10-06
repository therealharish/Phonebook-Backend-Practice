class Solution {
    public int minimumDifference(int[] nums) {
        int n = nums.length;
        int t = 0;
        for(int i : nums) t += i;
        HashMap<Integer, TreeSet<Integer>> map = new HashMap<>();
        
        //get all sets for first n/2 elements and store size of set as key and sum of set as sorted list
        for(int i = 0; i < (1 << (n/2)); i++){
            int sum = 0;
            int cnt = 0;
            int j = i;
            int set = 0;
            while(j > 0){
                if((j & 1) == 1){
                    sum += nums[cnt];
                    set++;
                }
                cnt++;
                j >>= 1;
            }
            if(!map.containsKey(set)) map.put(set, new TreeSet<>());
            map.get(set).add(sum);
        }
        
        //do the same with rest n/2 elements and track result from previous map.
        // if we take x elements from rest then we muse pick n/2-x from first n/2 and if x elements of second half are summing as s1 then look for remaining total/2-s for required set size from previous calculation. diffrence will be minimum when sum is very close to middle(total/2).
        int res = Integer.MAX_VALUE;
        for(int i = 0; i < (1 << (n/2)); i++){
            int sum = 0;
            int cnt = (n/2);
            int j = i;
            int set = 0;
            while(j > 0){
                if((j & 1) == 1){
                    sum += nums[cnt];
                    set++;
                }
                cnt++;
                j >>= 1;
            }
            // get the list of remaining required set size
            TreeSet<Integer> x = map.get((n/2) - set);
            // get the remaining sum of set close to middle
            int d = (t/2) - sum;
            // check with floor and ciel values as if difference is not 0 then they will be probable candidates for minimum difference.
            Integer left = x.floor(d);
            if(left != null) res = Math.min(res, Math.abs(t - 2 * (left + sum)));
            Integer right = x.ceiling(d);
            if(right != null) res = Math.min(res, Math.abs(t - 2 * (right + sum)));
            if(res == 0) return 0;
        }
        return res;
    }
}