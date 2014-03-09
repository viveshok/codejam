package main

import "fmt"

// Modified KMP algorithm

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

        fmt.Printf("\ntext:    %v\npattern: %v\n", text, pattern)
        fmt.Printf("shifts: %v\n", fuzzyKMP(text, pattern, 1))
    }
}

func fuzzyKMP(text string, pattern string, k int) []int {
    n := len(text)
    m := len(pattern)
    result := make([]int, 0, n)
    pi := computeFuzzyPrefix(pattern, k)
    q := 0

    for i := 0; i < n-m+1; i++ {
        match := true
        for q < m && i+q < n {
            if pattern[q] == text[i+q] {
                q++
            } else {
                q = pi[q]
                match = false
                break
            }
        }
        if match {
            result = append(result, i)
        }
    }
    return result
}

func computeFuzzyPrefix(pattern string, k int) []int {
    // place for improvment; worst case O(m^3), maybe possible in O(m)
    m := len(pattern)
    pi := make([]int, m)
    for i := 1; i <= m; i++ {
        var j int
        for j = 1; j <= i; j++ {
            if fuzzyCompare(pattern[j:i], pattern[:i-j], k) {
                break
            }
        }
        pi[i-1] = i-j
    }
    return pi
}

func fuzzyCompare(a string, b string, k int) bool {
    if len(a) != len(b) {
        panic("in func compare; strings are of different length!")
    }

    for i, v := range a {
        if rune(b[i]) != v {
            if k == 0 {
                return false
            } else {
                k--
            }
        }
    }

    return true
}



//func leftpad(str string, num int) string {
//    format := fmt.Sprintf("%%%ds", num)
//    return fmt.Sprintf(format, str)
//}
//
//func min(a, b int) int {
//    if a<b {
//        return a
//    } else {
//        return b
//    }
//}
