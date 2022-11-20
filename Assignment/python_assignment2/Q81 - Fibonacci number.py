
#Q81. Write a Python program to find the n-th Fibonacci Number.

given_num = int(input('Enter any number for n :'))
fibonacci_number = 0
fibonacci_series_list = [0,1]
for number in range(2,given_num):
    result = fibonacci_series_list[number-1] + fibonacci_series_list[number-2]
    fibonacci_series_list.append(result)
print(fibonacci_series_list)
print('nth fibonacci number :',fibonacci_series_list[given_num-1])