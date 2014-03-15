package main

import "fmt"
import "sort"

type Node struct {
    children map[rune]*Node
}

func newNode() *Node {
    n := new(Node)
    n.children = make(map[rune]*Node)
    return n
}

func buildSuffixTrie(s string) *Node {
    if len(s) == 0 {
        panic("Can't build suffix tree of empty string!")
    }

    s += "$"
    root := newNode()

    for i := range s {
        current := root
        for _, c := range s[i:] {
            if _, ok := current.children[c]; !ok {
                current.children[c] = newNode()
            }
            current = current.children[c]
        }
    }
    return root
}

// return length of all suffixes in sub-trie
func getIndices(n *Node, acc int) []int {
    result := []int{}
    for c, child := range n.children {
        if c == '$' {
            result = append(result, acc)
        } else {
            result = append(result, getIndices(child, acc+1)...)
        }
    }
    return result
}

// return indices of match (from the end, end of pattern!)
func find(n *Node, p string, k int) []int {
    if k < 0 { // used all mismatch
        return []int{}
    } else if len(p) == 0 { // match!
        return getIndices(n, 0)
    } else {
        result := []int{}
        for char, child := range n.children {
            if char == rune(p[0]) {
                result = append(result, find(child, p[1:], k)...)
            } else {
                result = append(result, find(child, p[1:], k-1)...)
            }
        }
        return result
    }
}

func main() {
    var numCases int
    _, err := fmt.Scanf("%d\n", &numCases)
    if err != nil { panic(err) }

    for i := 0; i < numCases; i++ {
        var text, pattern string
        _, err = fmt.Scanf("%v\n%v\n", &text, &pattern)
        if err != nil { panic(err) }
        _, err = fmt.Scanf("\n")
        if err != nil { panic(err) }

        prelim := find(buildSuffixTrie(text), pattern, 1)
        results := make([]int, len(prelim))
        for i, v := range prelim {
            results[i] = len(text)-len(pattern)-v
        }
        sort.Ints(results)
        for _, v := range results {
            fmt.Printf("%v ", v)
        }
        fmt.Printf("\n")
    }
}

func (n *Node) toSuffixArray(prefix string) []string {

    result := []string{}

    if len(n.children) == 0 {
        return []string{prefix}
    } else {
        for char, child := range n.children {
            result = append(result, child.toSuffixArray(prefix+string(char))...)
        }
        return result
    }
}

func leftpad(str string, num int) string {
    format := fmt.Sprintf("%%%ds", num+len(str))
    return fmt.Sprintf(format, str)
}
