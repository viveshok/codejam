package main

import "testing"
import "reflect"

func Test_skipTable(t *testing.T) {
    if tmp := skipTable("xyzwxyz"); !reflect.DeepEqual(tmp, []int{0, 1, 2, 3, 4, 4, 4}) {
        t.Errorf("skipTable(\"xyzwxyz\") == %v ?!", tmp)
    } else if tmp := skipTable("1234567"); !reflect.DeepEqual(tmp, []int{0, 1, 2, 3, 4, 5, 6}) {
        t.Errorf("skipTable(\"1234567\") == %v ?!", tmp)
    } else {
        t.Log("skipTable passed test")
    }
}

func Test_fss(t *testing.T) {
    if tmp := fss("abcdef", 6); tmp != 5 {
        t.Errorf("fss(\"abcdef\", 6) == %v) ?!", tmp)
    } else if tmp:=fss("abcabc", 6); tmp != 3 {
        t.Errorf("fss(\"abcabc\", 6) == %v) ?!", tmp)
    } else if tmp:=fss("abcaxc", 6); tmp != 3 {
        t.Errorf("fss(\"abcaxc\", 6) == %v) ?!", tmp)
    } else {
        t.Log("fss passed test")
    }
}
