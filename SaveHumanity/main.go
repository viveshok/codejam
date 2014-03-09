package main

// Using suffix tree, credits to Prof. Carl Kingsford, CMU
import "fmt"

type Node struct {
    children map[rune]*Node
    suffixLink *Node
}

func newNode() *Node {
    n := new(Node)
    n.children = make(map[rune]*Node)
    return n
}

func newNodeWithSuffix(suffixLink *Node) *Node {
    n := newNode()
    n.suffixLink = suffixLink
    return n
}

func buildSuffixTrie(s string) *Node {
    if len(s) == 0 {
        panic("Can't build suffix tree of empty string!")
    }
    root := newNode()
    root.suffixLink = root
    longest := newNodeWithSuffix(root)
    root.children[rune(s[0])] = longest

    for _, c := range s[1:] {
        current := longest
        var previous *Node
        for _, present := current.children[c]; !present; _, present = current.children[c] {
            r1 := newNode()
            current.children[c] = r1

            if previous != nil {
                previous.suffixLink = r1
            }

            previous = r1
            current = current.suffixLink
        }

        if current == root {
            previous.suffixLink = root
        } else {
            previous.suffixLink = current.children[c]
        }
        longest = longest.children[c]
    }

    return root
}

func main() {
    var numCases int
    _, err := fmt.Scanf("%d\n", &numCases)
    if err != nil { panic(err) }

    fmt.Printf("numcases: %v\n", numCases)

    for i := 0; i < numCases; i++ {
        var text, pattern string
        _, err = fmt.Scanf("%v\n%v\n\n", &text, &pattern)
        if err != nil { panic(err) }

        fmt.Printf("\ntext:    %v\npattern: %v\n", text, pattern)
        fmt.Printf("suffix trie: %v\n", buildSuffixTrie(text))
    }
}

