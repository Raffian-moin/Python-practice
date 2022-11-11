def getSum(num):
    if num > 0:
        return num + getSum(num-1)
    return 0
    

result = getSum(10)
print(result)