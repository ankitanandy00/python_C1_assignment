numbers_input = input("Enter a sequence of comma-separated numbers: ")

numbers_list = [num.strip() for num in numbers_input.split(',')]

numbers_tuple = tuple(numbers_list)

print("List:", numbers_list)
print("Tuple:", numbers_tuple)
