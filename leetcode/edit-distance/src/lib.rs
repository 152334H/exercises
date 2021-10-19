pub mod lib {
pub struct Solution {}
//use std::collections::HashMap;
impl Solution {
    #[allow(arithmetic_overflow)]
    pub fn min_distance(word1: String, word2: String) -> i32 {
        /* state - dp[(ind1, ind2)] = edit_distance
         * insert: dp[(ind1,ind2+1)] = edit_distance+1
         * delete: dp[(ind1+1,ind2)] = edit_distance+1
         * replace: dp[(ind1+1,ind2+1)] = edit_distance+1
         * valid: dp[(ind1+1,ind2+1)] = edit_distance
         */
        let s1 = word1.as_bytes();
        let s2 = word2.as_bytes();
        /*
        let mut dp = HashMap::new();
        dp.insert((0,0), 0);
        fn recur(dp: &mut HashMap<(usize,usize),i32>, s1: &[u8], s2: &[u8], state: (usize,usize)) -> i32 {
            if state.0.max(state.1) == usize::MAX { return 9999999 }
            macro_rules! getdp { ($state:expr) => {
                recur(dp, s1, s2, $state)
            } }
            if dp.contains_key(&state) { return dp[&state]; }
            let min = getdp!((state.0,state.1-1)).min(
                      getdp!((state.0-1,state.1))).min(
                      getdp!((state.0-1,state.1-1)) - 
                      if state.0 > 0 && state.1 > 0 &&
                      s1[state.0-1] == s2[state.1-1] { 1 } else { 0 });
            dp.insert(state, min+1);
            dp[&state]
        }
        recur(&mut dp, s1, s2, (s1.len(),s2.len()))
        */
        let mut prev_dp = vec![s1.len()+s2.len();s2.len()+1];
        for i in 0..=s2.len() {
            prev_dp[i] = s2.len()-i;
        }
        for i1 in (0..s1.len()).rev() {
            let mut dp = vec![s1.len()+s2.len();s2.len()+1];
            dp[s2.len()] = s1.len() - i1;
            for i2 in (0..s2.len()).rev() {
                let mut min = s1.len() + s2.len();
                if s1[i1] == s2[i2] {
                    min = min.min(prev_dp[i2+1]);
                    dp[i2] = min;
                }
                min = min.min(dp[i2+1]+1)
                    .min(prev_dp[i2]+1)
                    .min(prev_dp[i2+1]+1);
                dp[i2] = min;
            }
            prev_dp = dp;
        }
        prev_dp[0] as i32
    }
}
}
