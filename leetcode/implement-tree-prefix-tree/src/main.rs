/* The Trie here is a Radix Tree, making things overcomplicated & slow
 * But on the flip side, memory usage beats 100% of users.
 */
use std::collections::HashMap;
struct Edge {
    s: Vec<char>,
    target: Trie
}
impl Edge {
    fn new() -> Self { Edge { s: Vec::new(), target: Trie::new() } }
    fn from(s: &[char]) -> Self { Edge { s: s.to_owned(), target: Trie::new() } }
}
struct Trie { edges: HashMap<char,Edge> }
enum Search<'a> {
    NullQuery,  // `word` was ""
    NoFirstChar,// `self.edges[word[0]]` doesn't exist
    PrefixTooLong(&'a mut Edge),    // This is ONLY returned when `word` is a prefix of the prefix itself.
    PrefixUnmatched(&'a mut Edge),  // If `self.edges[word[0]]` is not a prefix of `word`
    Found(&'a mut Edge),    // If a matching prefix was found for `word`
}
macro_rules! callrecur { ($s:expr,$i:ident,$w:expr) => {
    $s.$i(&$w.chars().collect::<Vec<char>>()[..])
} }
impl Trie {
    fn new() -> Self { Trie { edges: HashMap::new() } }
    
    // The 3 main functions are implemneted recursively, but to save memory,
    // String is converted to &str first via a helper macro, callrecur!()
    fn insert(&mut self, word: String) { callrecur!(self, insert_r, word) }
    fn search(&mut self, word: String) -> bool { callrecur!(self, search_r, word) }
    fn starts_with(&mut self, word: String) -> bool { callrecur!(self, starts_with_r, word) }
   
    // 4 Additional helper functions: add_leaf, add_edge, find_edge, helper
    /* add_leaf will add a "null" node to a node. This is to distinguish between nodes that are
     * merely junctions (not representing added words) and nodes that are also endpoints.  */
    fn add_leaf(&mut self) { self.edges.entry('\0').or_insert_with(Edge::new); }
    // add_edge will create an edge with the string `word`, adding a terminating leaf if requested.
    fn add_edge(&mut self, word: &[char], addnull: bool) -> Option<Edge> {
        let res = self.edges.insert(word[0],Edge::from(word)); //entry().insert is nightly only :(
        if addnull { self.edges.get_mut(&word[0]).unwrap().target.add_leaf() }
        res // returns the original value of self.edges[word[0]] if it existed
    }
    // find_edge will search for a prefix matching with `word`.
    fn find_edge(&mut self, word: &[char]) -> Search {
        if word.is_empty() { Search::NullQuery } else {
            let c = word[0];
            if let Some(substr) = self.edges.get_mut(&c) {
                if substr.s.len() > word.len() {
                    if &substr.s[..word.len()] != word {
                        Search::PrefixUnmatched(substr)
                    } else { Search::PrefixTooLong(substr) }
                } else if substr.s != &word[..substr.s.len()] {
                        Search::PrefixUnmatched(substr)
                } else { Search::Found(substr) }
            } else { Search::NoFirstChar }
        }
    }
    /* helper() handles insertion for Search::Prefix*.
     * Basically split the existing prefix as necessary, adding/moving relevant nodes */
    fn helper(&mut self, word: &[char], prefix_is_longer: bool) {
        let c = word[0]; // first char
        let e = self.edges.get(&c).unwrap(); // same edge from self.find_edge(word)
        let diffi = if prefix_is_longer { word.len() } else {
            e.s.iter().zip(word).enumerate().filter(|(_,(c1,c2))| c1 != c2)
                .map(|(i,_)| i).next().unwrap() // i.e. "get index of first non-matching char"
        }; // e.s[diffi] is always valid. word[diffi] not so.
        /* the next part is a little bit confusing.
         * the current edge will be cut at `diffi`, with the original edge being shortened to
         * &word[..diffi] == &e.s[..diffi], connected to a node that has edge &e.s[diffi..], and
         * also &word[diffi..] if the latter is not "".
         * The _original_ node of the original edge will be moved to the edge for &e.s[diffi..].
         */
        let mut subsubstr = Edge::from(&e.s[diffi..]); // the latter half 
        let old_edge = self.add_edge(&word[..diffi], prefix_is_longer).unwrap();
        let new_trie = &mut self.edges.get_mut(&c).unwrap().target;
        subsubstr.target = old_edge.target;
        new_trie.edges.insert(subsubstr.s[0],subsubstr);
        if !prefix_is_longer { new_trie.add_edge(&word[diffi..], true); }
    }
    // insert a word into the Trie. Recurse if a matching prefix is found.
    fn insert_r(&mut self, word: &[char]) {
        match self.find_edge(word) {
            Search::NullQuery => self.add_leaf(),
            Search::NoFirstChar => { self.add_edge(word, true); },
            // for the Prefix* cases, if I capture (e), &mut self will be stuck in .find_edge()
            Search::PrefixUnmatched(_) => self.helper(word,false),
            Search::PrefixTooLong(_) => self.helper(word,true),
            Search::Found(e) => e.target.insert_r(&word[e.s.len()..]),
        }
    }
    // search for a word. Very simple recursion.
    fn search_r(&mut self, word: &[char]) -> bool {
        match self.find_edge(word) {
            Search::NullQuery => self.edges.contains_key(&'\0'),
            Search::Found(e) => e.target.search_r(&word[e.s.len()..]),
            _ => false
        }
    }
    // Prefix searching is subtly different from word searching. NullQuery is always valid here.
    fn starts_with_r(&mut self, word: &[char]) -> bool {
        match self.find_edge(word) {
            Search::NullQuery => true,
            Search::PrefixTooLong(e) => &e.s[..word.len()] == word,
            Search::Found(e) => e.target.starts_with_r(&word[e.s.len()..]),
            _ => false
        }
    }
}

fn main() {
    let mut obj = Trie::new();
    obj.insert("apple".to_string());
    assert!(obj.search("apple".to_string()));
    assert!(!obj.search("app".to_string()));
    assert!(obj.starts_with("app".to_string()));
    obj.insert("app".to_string());
    assert!(obj.search("app".to_string()));
}
