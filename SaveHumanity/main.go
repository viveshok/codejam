package main

import "fmt"
//import "os"

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

        fmt.Printf("Case %d: text: %s, pattern: %s, skipTable: %v\n", i, text, pattern, skipTable(pattern))
    }
}

func skipTable(pattern string) []int {
    length := len(pattern)
    fss_ := fss(pattern, length)
    ret := make([]int, length)
    for i:=0; i<fss_; i++ {
        ret[i] = i
    }
    for i:=fss_; i<length; i++ {
        ret[i] = fss_
    }
    return ret
}

// First Similar Suffix, one mismatch allowed
func fss(pattern string, length int) int {
    for i:=1; i<length-1; i++ {
        mismatchUsed := false
        match := true
        for j:=0; j<length-i && match; j++ {
            if pattern[j] != pattern[i+j] {
                if mismatchUsed {
                    match = false
                } else {
                    mismatchUsed = true
                }
            }
        }
        if match { return i }
    }
    return length-1
}
