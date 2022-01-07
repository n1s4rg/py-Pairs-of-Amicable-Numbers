#function to calculate SquareRoot of number
def calcSqrt(num):
    result = (num)**(1/2)
    return result

#function to calculate sum of proper divisors
def divisorSum(num) :
    result = 0
    for i in range(2, int(calcSqrt(num)) + 1):
        if num % i == 0:
            if (i == int(num / i)):
                result = result + i
            else:
                result = result + (i + int(num / i))

    return (result + 1)

def numIsAmicable(x,y):
    if divisorSum(x)!=y:
        return False

    return (divisorSum(y) == x)


x = 2620
y = 2924

if (numIsAmicable(x,y)):
    print("The relationship Exist !!")
else :
    print("The relationship does not Exist !!")