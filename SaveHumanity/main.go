package main

import "os"
import "fmt"

import "../utils"

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("\nUsage: $ go run main.go inputfile\n\n")
	} else {
		var numCases int

		fd, err := os.Open(os.Args[1])
		utils.Check(err)

		_, err = fmt.Fscanf(fd, "%d\n", &numCases)
		utils.Check(err)

		for i := 0; i < numCases; i++ {
			var input1, input2 string
			_, err = fmt.Fscanf(fd, "%v\n%v\n", &input1, &input2)
			utils.Check(err)
			_, err = fmt.Fscanf(fd, "\n")
			utils.Check(err)

			fmt.Printf("Case %d: input1: %s, input2: %s, matches: %v\n", i, input1, input2, matches(input1, input2))
		}
		fd.Close()
	}
}

func matches(text string, pattern string) *[]int {
	target_weight := weight(pattern)
    length := len(pattern)

    sum := 0
    for i := 0; i<length; i++ {
       sum += int(text[i])
    }

    ret := make([]int, 100000)

    delta := target_weight-sum
    if delta*delta<=625 && match(text[0:length], pattern, 1) {
        ret = append(ret, 0)
    }

    for i := length; i<=len(text)-1; i++ {
        sum += int(text[i])-int(text[i-length])
        delta = target_weight-sum
        if delta*delta<=625 && match(text[i-length+1:i], pattern, 1) {
            ret = append(ret, i-length+1)
        }
    }

    return &ret
}

func match(str1 string, str2 string, diff int) bool {
    for i, v := range str1 {
        if v!=rune(str2[i]) {
            if diff<1 {
                return false
            } else {
                diff -= 1
            }
        }
    }
    return true
}

func weight(str string) int {
    ret := 0
	for _, c := range str {
        ret += int(c)
	}
    return ret
}
