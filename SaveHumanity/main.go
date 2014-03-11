package main

import "fmt"

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
func getIndices(n *Node, k int) []int {
    result := []int{}
    for c, child := range n.children {
        if c == '$' {
            result = append(result, k)
        } else {
            result = append(result, getIndices(child, k+1)...)
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
    } else if next, ok := n.children[rune(p[0])]; ok {
        return find(next, p[1:], k)
    } else { // burn a mismatch
        result := []int{}
        for _, child := range n.children {
            result = append(result, find(child, p[1:], k-1)...)
        }
        return result
    }
}

func main() {
    var numCases int
    _, err := fmt.Scanf("%d\n", &numCases)
    if err != nil { panic(err) }

    fmt.Printf("numcases: %v\n", numCases)

    for i := 0; i < numCases; i++ {
        var text, pattern string
        _, err = fmt.Scanf("%v\n%v\n", &text, &pattern)
        if err != nil { panic(err) }
        _, err = fmt.Scanf("\n")
        if err != nil { panic(err) }

        for _, i := range find(buildSuffixTrie(text), pattern, 1) {
            fmt.Printf("\ntext:    %v\n", text)
            shift := len(text)-len(pattern)-i
            fmt.Printf("pattern: %v\n", leftpad(pattern, shift))
//            fmt.Printf("%v ", shift)
        }
        fmt.Printf("\n")
    }
}

func prettyPrint(n *Node) string {
    result := "["
    i := 1
    for c, child := range n.children {
        if c == '$' {
            result += string(c)
        } else {
            result += string(c) + ":" + prettyPrint(child)
        }

        if i < len(n.children) {
            result += ", "
        }
        i++
    }
    return result + "]"
}

func leftpad(str string, num int) string {
    format := fmt.Sprintf("%%%ds", num+len(str))
    return fmt.Sprintf(format, str)
}
