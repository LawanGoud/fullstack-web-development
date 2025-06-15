dividend = input()
dividend = int(dividend)

divisor = input()
divisor = int(divisor)

quotient = dividend // divisor

remainder = dividend - (divisor * quotient)
print(remainder)