test_cases = int(input())
# element_count = input()
array = []

while test_cases:
    element_count = input()
    for index in range(int(element_count)):
        element = int(input())
        array.append(element)
    even = 0
    odd = 0
    for index, value in enumerate(array):
        print(f"index1- {index}  value-{value}")
        if index % 2 != value % 2:
            if value % 2 == 1:
                odd = odd+1
            else:
                even = even+1

    if even == odd:
        print(even)
    else:
        print(-1)
    test_cases -=1

#     t = int(input())
# while t:
#     t-=1
#     n = int(input())
#     arr = list(map(int,input().split()))
#     odd = 0
#     even = 0
#     for i in range(n):
#         if i%2!=arr[i]%2:
#             if i%2==0:
#                 even+=1
#             else:
#                 odd+=1
#     if even==odd:
#         print(even)
#     else:
#         print(-1)