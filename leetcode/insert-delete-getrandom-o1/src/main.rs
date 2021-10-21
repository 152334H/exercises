/*Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

 

Constraints:

    -231 <= val <= 231 - 1
    At most 2 * 105 calls will be made to insert, remove, and getRandom.
    There will be at least one element in the data structure when getRandom is called.
*/
use insert_delete_getrandom_o1::lib::RandomizedSet;
fn main() {
    let mut randomised_set = RandomizedSet::new();
    assert_eq!(true, randomised_set.insert(1)); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    assert_eq!(false,randomised_set.remove(2)); // Returns false as 2 does not exist in the set.
    assert_eq!(true, randomised_set.insert(2)); // Inserts 2 to the set, returns true. Set now contains [1,2].
    println!("{}", randomised_set.get_random()); // getRandom() should return either 1 or 2 randomly.
    assert_eq!(true, randomised_set.remove(1)); // Removes 1 from the set, returns true. Set now contains [2].
    assert_eq!(false, randomised_set.insert(2)); // 2 was already in the set, so return false.
    println!("{}", randomised_set.get_random()); // Since 2 is the only number in the set, getRandom() will always return 2.

     
}
