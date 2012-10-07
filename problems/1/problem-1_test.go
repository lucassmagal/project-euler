package problem_1

import "testing"

func Test_Sum_divisors(t *testing.T) {
    if Sum_divisors(10) != 23 {
        t.Errorf("Expected input for Sum_divisors(10) is 23. Got %d",
                 Sum_divisors(10))
    }

    if Sum_divisors(1000) != 233168 {
        t.Errorf("Expected input for Sum_divisors(10) is 23. Got %d",
                 Sum_divisors(1000))
    }
}