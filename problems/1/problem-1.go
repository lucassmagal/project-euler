package problem_1

func Sum_divisors(n int) int {
    result := []int{}
    sum := 0

    for i:=1; i<n; i++ {
        if i%3==0 || i%5==0 {
            result = append(result, i)
        }
    }

    for _, i := range result {
        sum += i
    }

    return sum
}