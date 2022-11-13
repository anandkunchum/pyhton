#Q24 - Write a code to take 3 numbers as an input from the user and display the greatest no as output.
str_input = input("Enter any 3 numbers with seperated by space:")
input_numbers_list = str_input.split(" ")
max_number = 0
for number in input_numbers_list:
    if int(number) > max_number:
        max_number = int(number)
print("Greatest number: ",max_number)