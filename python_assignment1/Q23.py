#Q23 - Write a code that displays the sum of all the even numbers from the given list

numbers = [12, 75, 150, 180, 145, 525, 50]
even_numbers_sum = 0
for number in numbers:
    if number % 2 == 0:
        even_numbers_sum += number
print("Even numbers sum :",even_numbers_sum)