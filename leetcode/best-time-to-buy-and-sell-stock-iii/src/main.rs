struct Solution {}
impl Solution {
    /* this is almost identical to the previous buy-and-sell-stock problem I did...
     * ... but that one was rated Medium instead of Hard. Feeling confused.
     */
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut state = [-99999;5]; state[4] = 0;
        /* states: [1st item bought, 1st item sold, 2nd item bought, 2nd item sold,
         * bought nothing ]*/
        macro_rules! assign_max { ($lvalue:expr, $rvalue:expr) => {
            $lvalue = $lvalue.max($rvalue)
        } }
        for p in prices { // assign from 3 to 0 instead of the other way around.
            assign_max!(state[3], state[2]+p);
            assign_max!(state[2], state[1]-p);
            assign_max!(state[1], state[0]+p);
            assign_max!(state[0], -p);
        }
        *state.iter().max().unwrap()
    }
}
fn main() {
    for (i,o) in [(vec![3,3,5,0,0,3,1,4],6),
            (vec![1,2,3,4,5],4),
            (vec![7,6,4,3,1],0),
            (vec![1],0)] {
        assert_eq!(o, Solution::max_profit(i));
    }
}
