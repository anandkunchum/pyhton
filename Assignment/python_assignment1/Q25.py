#Q25. Write a program to display only those numbers from a list that satisfy the following conditions
#- The number must be divisible by five
#- If the number is greater than 150, then skip it and move to the next number
#- If the number is greater than 500, then stop the loop
# numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]
display_numbers = []
end_of_the_loop = False
position = 0
number = 0
while not end_of_the_loop:
    number = numbers[position]
    if number > 500:
        end_of_the_loop = True
    if number <= 150 and number % 5 == 0:
        display_numbers.append(number)
    position += 1
print(display_numbers)
