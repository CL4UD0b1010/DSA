package main

import "fmt"

func main() {

	x := create()
	fmt.Println(x)

}

func create() *int {
	x := 10
	return &x

}
