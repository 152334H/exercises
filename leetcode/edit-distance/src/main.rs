/*Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.
*/
use edit_distance::lib::Solution;
fn main() {
    for (w1,w2,out) in [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "", 0),
        ("", "a", 1),
        ("b", "", 1)
    ] {
        assert_eq!(Solution::min_distance(w1.to_string(), w2.to_string()), out);
    }
}
