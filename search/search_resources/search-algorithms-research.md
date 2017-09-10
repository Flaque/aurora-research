# Search Algorithms Research

## Search Algorithm Vocab
Progressive search- techniques that can be used to efficiently implement other computationally burdensome techniques
Fast Match- quick, but not always accurate
Naive string matching- the most basic search algorithm. O(nm)
Approximate string matching- also known as fuzzy searching
## Types of Search Algorithms
### Forward-Backward Word-Life Algorithm
Used for speech recognition. Progressive search algorithm. Does not scale down well
### Boyer-Moore
String searching algorithm. Runs fasters as pattern length increases. Uses information from preprocessing to skip as many alignments as possible. Worst case O(n+m) if pattern does not exist in the text, O(nm) if pattern does exist
### Knuth-Morris-Pratt Algorithm
An improvement to naive string matching. It skips iterations for which no match is possible. Splits comparisons into true and false categories to speed up the algorithm. Worst case O(n)
### The Trie Data Structure
A special kind of tree, capable of storing a sequence of values in such a way that tracing the path from the root to any node yields a valid subset of that sequence. Significantly cuts down on search time. Compared to naive string matching the trie approach decreased run time by 99.93% on a 23MB text file
### Rabin-Karp Algorithm
String searching algorithm that uses hashing to find a set of pattern strings in a text. Best case O(n+m), worst case O(nm). Generally used for plagiarism detection
### Aho-Corasick Algorithm
Used for set matching. Worst case (n+m+z). Formed the basis of the original Unix command fgrep
### Fuzzy searching
Locates webpages that are likely to be relevant to a search argument. More powerful than exact searching. O(mn) worst case. Lots of open source algorithms available.
