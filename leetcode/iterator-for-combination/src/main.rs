use iterator_for_combination::CombinationIterator;
fn main() {
    let mut itr = CombinationIterator::new("abc".to_string(), 2);
    assert_eq!("ab".to_string(), itr.next());    // return "ab"
    assert_eq!(itr.has_next(), true);
    assert_eq!(itr.next(), "ac".to_string());
    assert_eq!(itr.has_next(), true);
    assert_eq!(itr.next(), "bc".to_string());
    assert_eq!(itr.has_next(), false);
}
