class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        sumOdd = 0
        sumEven = 0

        odd = 1
        even = 2

        for i in range(n):
            sumOdd += odd
            odd +=2

            sumEven += even 
            even += 2

        return math.gcd(sumOdd, sumEven)

      