class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit_product = 1
        digit_sum = 0

        while n > 0:
            digit = n % 10  #Extracts the last digit
            digit_product *= digit   #Multiplies to total product
            digit_sum += digit   #Add to total sum
            n //= 10   #Removes the last digit
        return digit_product - digit_sum