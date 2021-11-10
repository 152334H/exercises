use best_time_to_buy_and_sell_stock_ii::Solution;
fn main() {
    for (inp,out) in [
        (vec![7,1,5,3,6,4], 7),
        (vec![7,6,4,3,1], 0),
        (vec![1,2,3,4,5], 4),
    ] {
        assert_eq!(Solution::max_profit(inp), out);
    }
}
