package main

import "fmt"

func main() {

	var x *int
	x = nil
	take(x)
	fmt.Println(x)

}

func take(x *int) {
	*x = 100

}
