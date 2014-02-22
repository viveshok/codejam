
package main

import "os"
import "fmt"

import "./utils"

func main() {
    if len(os.Args)!=2 {
        fmt.Printf("\nUsage: $ go run main.go inputfile\n\n")
    } else {
        var numCases int

        fd, err := os.Open(os.Args[1])
        utils.Check(err)

        _, err = fmt.Fscanf(fd, "%d\n", &numCases)
        utils.Check(err)

        for i:=0; i<numCases; i++ {
            var input1, input2 string;
            _, err = fmt.Fscanf(fd, "%s\n%s\n", &input1, &input2)
            utils.Check(err)
            fmt.Printf("\nCase %d: input1: %s, input2: %s\n", i, input1, input2)
        }
        fd.Close()
    }
}

