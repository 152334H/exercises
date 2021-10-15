struct Solution {}
const MAXLEN: usize = 5000;
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut dp = [[-999999999;3];MAXLEN+5];
        /* dp[day][state], where state is encoded by:
         *   0 - can currently buy
         *   1 - can currently sell
         *   2 - in cooldown
         */
        dp[0][0] = 0;
        for (i,&p) in prices.iter().enumerate() {
            dp[i+1][0] = dp[i][2].max(dp[i][0]); // either finish cooldown or just wait
            dp[i+1][1] = dp[i][1].max(dp[i][0]-p); // either buy now or just wait
            dp[i+1][2] = dp[i][1]+p // must be a sell.
        }
        *dp[prices.len()].iter().max().unwrap()
    }
}
fn main() {
    for (i,o) in [(vec![1,2,3,0,2], 3),
            (vec![1],0), (vec![1,2],1),
            (vec![1,2,4], 3)] {
        let res = Solution::max_profit(i.clone());
        if res != o { println!("{:?} {} {}", i,o,res); }
            }
}
