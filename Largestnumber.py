numbers = [10, 45, 78, 2, 34, 89, 21]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("The largest number in the list is:", largest)
