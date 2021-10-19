pub mod lib {
pub struct Solution {}
impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        let mut state = (0,-9999999);
        /* [0] - can buy
         * [1] - can sell */
        for p in prices {
            state = (state.0.max(state.1+p),
                state.1.max(state.0-p-fee));
        }
        state.0.max(state.1)
    }
}
}
