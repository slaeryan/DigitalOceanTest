package main

import (
	"fmt"

	"github.com/shirou/gopsutil/host"
)

func main() {
	platform, family, version, _ := host.PlatformInformation()

	// almost every return value is a struct
	fmt.Printf(platform, " ")
	fmt.Printf(family, " ")
	fmt.Printf(version, " ")

	// convert to JSON. String() is also implemented
	fmt.Println(platform)
}
