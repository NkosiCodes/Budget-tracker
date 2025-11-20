# fruits = ["apple", "banana", "orange"]

# fruits.append("pear")

# for i in range(len(fruits)):
#     print(fruits[i])

# for fruit in fruits:
#     print(fruit)

numbers = [10, 20, 30, 40, 50]
numbers.append(numbers[len(numbers)-1]+10)
numbers.remove(numbers[2])
# print(numbers)

for number in numbers:
    print(number)