pub struct Solution {}
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        *prices.into_iter().fold([0,i32::MIN],|state,price|{
            let [buy,sell] = state;
            [buy.max(sell+price),sell.max(buy-price)]
        }).iter().max().unwrap()
    }
}
