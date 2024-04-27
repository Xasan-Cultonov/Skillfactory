# Кортежи
# data = (4, 5, 6, 7, 8, True, "Hello")
# # data[0] = 6 - NO
# print(data[1:6])
#
# # print(data.count(60))
# print(data)

data = (4, 5, 6, 7, 8, True, "Hello")

for i in data:
    print(i)

nums = [3, 4, 6]

new_data = tuple(nums)
word = tuple("Hello word")

print(word)