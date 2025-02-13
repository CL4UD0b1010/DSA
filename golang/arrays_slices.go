package main

import "fmt"

func main() {

	arr := [5]int{1, 2, 3, 4, 5}
	slice := arr[1:4]

	slice2 := []int{}

	fmt.Println(slice, len(slice2), cap(slice))

}
