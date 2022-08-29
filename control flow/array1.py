# numbers = [1, 2, 3, 4, 5];

# d = 2;

# temp = [];

# temp = numbers[2:] + numbers[0:2]

# print(temp)

# for (index, number) in enumerate(numbers) :
#     if (index < d ) :
#         temp.append(number)
#     # print(number, index)

# print(temp)

numer_list  = [0, 1, 1, 2, 3, 4, 4]

new_list = []
current_index = 0

new_list.append(numer_list[0])

# print(new_list)

for index, number in enumerate(numer_list) :
    if (new_list[current_index] != number) :
        # print(new_list[current_index])
        new_list.append(numer_list[current_index])
        current_index = current_index + 1

print(new_list)
