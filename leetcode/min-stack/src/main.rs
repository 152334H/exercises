/*Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:

    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.
*/
fn main() {
    let mut min_stack = min_stack::MinStack::new();
    min_stack.push(-2);
    min_stack.push(0);
    min_stack.push(-3);
    assert_eq!(-3,min_stack.get_min()); // return -3
    min_stack.pop();
    assert_eq!(0,min_stack.top());    // return 0
    assert_eq!(-2,min_stack.get_min()); // return -2

    min_stack = min_stack::MinStack::new();
    min_stack.push(0);
    min_stack.push(1);
    min_stack.push(0);
    assert_eq!(0,min_stack.get_min());
    min_stack.pop();
    assert_eq!(0,min_stack.get_min());
}
