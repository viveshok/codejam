
package main

import "os"
import "fmt"

func main() {
    if len(os.Args)!=2 {
        fmt.Printf("\nUsage: $ go run inputfile\n\n")
    } else {
        var numCases int
        fd, _ := os.Open(os.Args[1])
        fmt.Fscanf(fd, "%d\n", &numCases)
        for i:=0; i<numCases; i++ {
            var input1, input2 string;
            fmt.Fscanf(fd, "%s\n%s\n", &input1, &input2)
            fmt.Printf("\nCase %d: input1: %s, input2: %s\n", i, input1, input2)
        }
        fd.Close()
    }
}

