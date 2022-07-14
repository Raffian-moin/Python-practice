def myFunc() :
    print('yay hoo')

myFunc()

# function with return
def sum(a, b) :
    return a + b

result = sum(3, 4)
print(result)

# keyword arguments

def testFunc(discount, price) :
    return price - price * discount

result1 = testFunc(price = 100, discount = 0.1)

print(result1)

# keyword argument is used to specify the argument name while calling the function
# it increases the readability

# recursive function

def recursiveFunc(count) :
    print(count)
    count += 1
    if (count < 10) :
       recursiveFunc(count);

recursiveFunc(5)

# find sum of 1-100
def findSum(n) :
    if (n > 0) :
       return  n + findSum(n - 1)
    else :
        return 0

result = findSum(100)

print(result);
