package main

import "fmt"

//func main() {
//
//    var numCases int
//    _, err := fmt.Scanf("%d\n", &numCases)
//    if err != nil { panic(err) }
//
//    fmt.Printf("numcases: %v\n", numCases)
//
//    for i := 0; i < numCases; i++ {
//        var text, pattern string
//        _, err = fmt.Scanf("%v\n%v\n", &text, &pattern)
//        if err != nil { panic(err) }
//        _, err = fmt.Scanf("\n")
//        if err != nil { panic(err) }
//
//        skipTbl := skipTable(pattern)
//        solve(text, pattern, &skipTbl)
//    }
//}
//
//func solve(text, pattern string, skipTbl *[]int) {
//    plen := len(pattern)
//    for i := 0; i <= len(text)-plen; {
//        mismatch := false
//        match := true
//        var j int;
//        for j=0; j<plen; j++ {
//            if pattern[j] != text[i+j] {
//                if mismatch {
//                    match = false
//                    j++
//                    break
//                } else {
//                    mismatch = true
//                }
//            }
//        }
//
//        if match {
////            fmt.Printf("%d ", i)
//            fmt.Printf("\nMatch attempt (i=%d, j=%d, ", i, j)
//            fmt.Printf("inc=%d, next=%d) YES:\n", (*skipTbl)[j-1], i + (*skipTbl)[j-1])
//            fmt.Printf("%s\n%s\n%v\n", text, leftpad(pattern, i+plen), *skipTbl)
//        } else {
//            fmt.Printf("\nMatch attempt (i=%d, j=%d, ", i, j)
//            fmt.Printf("inc=%d, next=%d) NO:\n", (*skipTbl)[j-1], i + (*skipTbl)[j-1])
//            fmt.Printf("%s\n%s\n%v\n", text, leftpad(pattern, i+plen), *skipTbl)
//        }
//        i += (*skipTbl)[j-1]
//    }
//    fmt.Printf("\n")
//}

func main() {
	str := "abcdefabcdefabcdefghiabcdef"
	fmt.Printf("\nskipTable(\"%s\"):\n%v\n", str, skipTable(str))
}

func skipTable(pattern string) []int {
    fmt.Printf("\n%s\n", "abcdefabcdefabcdefghiabcdef")
    for i:=1; i<len(pattern); i++ {
        fmt.Printf("%s", pattern[i:])
        mismatch := false
        var j int
        var v rune
        for j, v = range pattern[i:] {
            if v != rune(pattern[j]) {
                if mismatch {
                    break
                } else {
                    mismatch = true
                }
            }
        }
        fmt.Printf("      %d\n", j)
    }

    return []int{}
}

func leftpad(str string, num int) string {
    format := fmt.Sprintf("%%%ds", num)
    return fmt.Sprintf(format, str)
}

func min(a, b int) int {
    if a<b {
        return a
    } else {
        return b
    }
}
